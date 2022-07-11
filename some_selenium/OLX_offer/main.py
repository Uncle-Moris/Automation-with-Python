from time import sleep
import unittest
import page

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class OLXSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('https://www.olx.pl/')

    def test_search_in_OLX(self, name: str):
        main_page = page.MainPage(self.driver)
        search_bar = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        search_bar.send_keys(name)
        search_bar.click()
        sleep(5)
        self.driver.quit()



if __name__ == '__main__':
    OLXSearch.test_search_in_OLX(name='agava')