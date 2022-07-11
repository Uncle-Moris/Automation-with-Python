from time import sleep
import asyncio
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def checking_the_share_price(name: str):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.gpw.pl/akcje')
    search = driver.find_element(By.XPATH, '/html/body/section[2]/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/input')
    search.send_keys(f'{name}')
    sleep(1)
    #search.send_keys(Keys.RETURN)
    #price = driver.find_elements(By.XPATH, '/html/body/section[2]/div[2]/div[5]/div/div[1]/div[1]/div[3]/div[1]/div[2]/table/tbody/tr')
    sleep(2)
    price_of_share = driver.find_element(By.XPATH, '//tbody/tr[1]/td[8]')
    price_of_share.is_enabled()
    sleep(3)
    print(price_of_share.text)
    print(type(price_of_share))
    current_window = driver.current_window_handle
    window_names = driver.window_handles


    driver.quit()

checking_the_share_price('pge')
