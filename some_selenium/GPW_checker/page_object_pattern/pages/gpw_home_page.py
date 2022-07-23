from selenium.webdriver.common.by import By
from time import sleep

class GPWHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.input_shear_name = "/html/body/section[2]/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/input"

    def set_shear(self, shear):
        self.driver.find_element(By.XPATH, self.input_shear_name).click()
        self.driver.find_element(By.XPATH, self.input_shear_name).send_keys(shear)
        sleep(4)