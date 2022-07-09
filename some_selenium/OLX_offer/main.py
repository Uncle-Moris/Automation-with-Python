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
        self.driver.get('https://www.olx.pl/')

    def test_search_in_OLX(self):
        main_page = page.MainPage(self.driver)
        search_bar = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()




driver.find_element(By.XPATH,'/html/body/div[1]/section[1]/form/div/fieldset/div[1]/div/div[1]/input').send_keys('Mieszkania')
sleep(2)
# 'https://twitter.com/Goaloo_sports'