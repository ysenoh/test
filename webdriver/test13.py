#  --*-coding:utf-8-*--

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

TIME_TO_WAIT = 10

class alert_is_closed(object):
    def __init__(self, text):
        self.text = text


    def __call__(self, driver):
        try:
            return Alert(driver).text != self.text

        except EC.NoAlertPresentException:
            return True


def myAccept(driver):
    alert = Alert(driver)
    text = alert.text

    alert.accept()

    driver.implicitly_wait(0)

    try:
        WebDriverWait(driver, TIME_TO_WAIT).until(
            alert_is_closed(text))
        
    finally:
        driver.implicitly_wait(TIME_TO_WAIT)


# driver = webdriver.Firefox()
driver = webdriver.Edge()
# driver = webdriver.Chrome()

driver.implicitly_wait(TIME_TO_WAIT)
driver.get('http://localhost/test13.html')

myAccept(driver)
driver.find_element_by_xpath('//body')

driver.close()


