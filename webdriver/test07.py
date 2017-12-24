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

driver = webdriver.Firefox()
# driver = webdriver.Edge()
# driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get('http://localhost/test07.html')

# 5secのすきに、他のウィンドウをactiveにする
time.sleep(5)

element = driver.find_element_by_xpath('//input[@id="ID01"]')
element.send_keys('abc')
driver.execute_script('arguments[0].blur();', element)

WebDriverWait(driver, 5).until(EC.alert_is_present())
Alert(driver).accept()

driver.close()


