from selenium.webdriver.common.by import By

class GoogleHomePage:

    def __int__(self, driver):
        self.driver = driver
        self.search_input_name = 'q'
        self.search_button_name = 'btnK'

    def search_in_google(self, text):
        self.driver.find_element(By.NAME, self.search_input_name).send_keys(text)
        self.driver.find_element(By.NAME, self.search_button_name).click()
