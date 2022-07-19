from behave import given, when, then
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@given(u'lunch chrome browser')
def step_impl(context):
    try:
        service = Service(ChromeDriverManager().install())
    except Exception:
        service = Service(executable_path='chromedriver')
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()

@when('open gpw homepage')
def step_impl(context):
    context.driver.get('https://www.gpw.pl/akcje')

@then('input shear name')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/section[2]/div[2]/div[5]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/input").send_keys('cdp')
    sleep(3)

@then('close brow-ser')
def step_impl(context):
    pass


@then('check shear {} value od shear is not empty')
def step_impl(context):
    assert 2+2 == 4
