from selenium.webdriver.common.by import By

class GoogleResultPage:

    def __int__(self, driver):
        self.driver = driver
        self.search_result_xpath = "//h3[@class='LC2O1b']"

    def open_first_result(self):
        self.driver.find_element(By.XPATH, self.search_result_xpath)[0].click()
