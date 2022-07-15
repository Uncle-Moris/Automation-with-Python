from time import sleep
import unittest
import page
import pytest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def test_setup():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('http://www.kurs-selenium.pl/demo/')
    yield
    driver.quit()


def test_something(test_setup):
    WebDriverWait(driver, 10).until(driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/a[2]/div/div").click())
    driver.implicitly_wait(10)

