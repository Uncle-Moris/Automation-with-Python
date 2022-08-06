from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://orteil.dashnet.org/cookieclicker/')
sleep(3)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]').click()

sleep(2)
while True:
    # option = input('Chose option: C - control, F - farm cookies :')
    # if option == 'F':
    counter = 0
    while True:
        counter += 1
        cookie = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[15]/div[8]/button').click()
        if counter == 1000:
            break

    for _ in range(10):
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[1]').click()
        except:
            print("Empty")

    n = 0
    for _ in range(10):
        product = f'product{n}'

        for _ in range(2):
            try:
                driver.find_element(By.XPATH, f'//*[@id="{product}"]').click()
            except:
                pass

        if n == 12:
            break
        n += 1

driver.quit()
