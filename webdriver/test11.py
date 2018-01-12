#  --*-coding:utf-8-*--

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
driver.get('http://localhost/test11.html')

elements = driver.find_elements_by_xpath('//tr//td[1]')
for element in elements:
    print(element.text)

driver.close()


