from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from .gpw_home_page import GPWHomePage



class TestGPWSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()


    def test_gpw_search(self, setup):
        self.driver.get("https://www.gpw.pl")
        search = GPWHomePage(self.driver)
        assert driver.title == 'Główny Rynek GPW - Akcje i PDAs'


