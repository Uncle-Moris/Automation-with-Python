from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



#if __name__ == '__main__':
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.gpw.pl/akcje')
    driver.maximize_window()
    yield
    driver.quit()


def test_site_title(test_setup):
    assert driver.title == 'Główny Rynek GPW - Akcje i PDAs'


