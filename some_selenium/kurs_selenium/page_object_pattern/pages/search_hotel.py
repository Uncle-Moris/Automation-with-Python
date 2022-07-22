from selenium.webdriver.common.by import By


class SearchHotelPage:

    def __int__(self, driver):
        self.driver = driver
        self.search_hotel_span

        driver.find_element(By.XPATH, "//span[text()='Search by Hotel or City Name']").click()
        driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys('Dubai')
        driver.find_element(By.XPATH, "//span[text()='Dubai']").click()
        driver.find_element(By.NAME, "checkin").send_keys("12/09/2022")
        driver.find_element(By.NAME, "checkout").send_keys("22/09/2022")
        driver.find_element(By.ID, "travellersInput").click()
        driver.find_element(By.ID, "adultInput").clear()
        driver.find_element(By.ID, "adultInput").send_keys("4")
        driver.find_element(By.ID, "childInput").clear()
        driver.find_element(By.ID, "childInput").send_keys("4")
        driver.find_element(By.XPATH, "//button[text()=' Search']").click()