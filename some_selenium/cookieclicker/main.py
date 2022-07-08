from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://orteil.dashnet.org/cookieclicker/')
sleep(9)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]').click()
sleep(5)

while True:
    option = input('chose option: C to control, f - farm cookies')
    if option == 'F':
        counter = 0
        while True:
            counter += 1
            cookie = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[15]/div[8]/button').click()
            if counter == 10000:
                break
    if option == 'C':
        sleep(15)



sleep(3)

driver.quit()
