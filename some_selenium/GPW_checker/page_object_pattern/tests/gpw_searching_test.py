import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from some_selenium.GPW_checker.page_object_pattern.pages.gpw_home_page import GPWHomePage
from time import sleep


class TestShearSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get("https://www.gpw.pl/akcje")
        find_shear = GPWHomePage(self.driver)
        find_shear.set_shear('dom')
