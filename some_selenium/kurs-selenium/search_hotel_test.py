from time import sleep

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

try:
    service = Service(ChromeDriverManager().install())
except Exception:
    service = Service(executable_path='chromedriver')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://www.kurs-selenium.pl/demo/')
driver.find_element_by_xpath('/html/body/div[17]/div/input').send_keys("Dubai")
sleep(2)
driver.find_element_by_xpath()
driver.find_element_by_xpath()
driver.find_element_by_name()
driver.find_element_by_name()

'''
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
'''

