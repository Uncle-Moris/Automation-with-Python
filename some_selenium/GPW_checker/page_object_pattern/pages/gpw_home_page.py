from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class GPWHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.home_gpw_url = 'https://www.gpw.pl/'
        self.stock_quotes_id = 'dropdownMenu1'
        self.shears_and_pda_xpath = "/html/body/header/nav[2]/div/div/div[1]/div/ul/li[1]/div/div/div/div[1]/div/div[1]/a[2]"
        self.input_shear_name = "/html/body/section[2]/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/input"
        self.searching_btn_xpath = '/html/body/section[2]/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/span/button'

    def set_shear(self, shear):
        self.driver.get(self.home_gpw_url)
        self.driver.find_element(By.XPATH, self.stock_quotes_id).click()

        self.driver.find_element(By.XPATH, self.shears_and_pda_xpath).click()
        self.driver.implicitly_wait(10)
        sleep(9)
        #self.driver.find_element(By.XPATH, '/html/body/section[2]/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/input').send_keys(shear)
        self.input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.input_shear_name)))
        self.input.send_keys(shear)
        self.driver.find_element(self.searching_btn_xpath).click()