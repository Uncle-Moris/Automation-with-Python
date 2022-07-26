from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleHomePage:

    def __int__(self, driver):
        self.driver = driver
        self.search_input_name = 'q'
        self.search_button_name = 'btnK'

    def search_in_google(self, text):
        self.WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, '')))
        self.driver.find_element(By.NAME, self.search_button_name).click()

