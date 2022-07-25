from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.gpw.pl")
driver.find_element(By.ID, 'dropdownMenu1').click()
driver.find_element(By.XPATH,'/html/body/header/nav[2]/div/div/div[1]/div/ul/li[1]/div/div/div/div[1]/div/div[1]/a[2]').click()
driver.find_element(By.XPATH, '/html/body/section[2]/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/input').send_keys('cdp')
sleep(3)
driver.quit()



