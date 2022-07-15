from time import sleep
import unittest
import page
import pytest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.common.exceptions import NoSuchElementException



@pytest.fixture
def test_setup():
    global driver
    global wait
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 10, 0.5, NoSuchElementException)
    driver.get('http://www.kurs-selenium.pl/demo/')
    yield
    driver.quit()


def test_something(test_setup):
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div[1]/a[2]/div/div")))
