from selenium import webdriver
from selenium.webdriver.common.by import By
from some_selenium.google.pages.google_home_page import GoogleHomePage
from some_selenium.google.pages.google_result_page import GoogleResultPage

import pytest
from webdriver_manager.chrome import ChromeDriverManager


class TestGoogleSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_google_search(self, setup):
        self.driver.get("http://www.google.com")
        home_page = GoogleHomePage(self.driver)
        home_page.search_in_google("Selenium")
        result_page = GoogleResultPage(self.driver)
        result_page.open_first_result()
