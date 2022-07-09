from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.olx.pl/')
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
sleep(300)