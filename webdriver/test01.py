#  --*-coding:utf-8-*--

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

# idが ID01である table要素 で、1列目のテキストが"Panama"である行の
# 2列目の td要素を取得するサンプル

driver = webdriver.Firefox()

try:
    driver.implicitly_wait(10)
    driver.get('http://localhost/test.html')

    elements = driver.find_elements_by_xpath(
        '//table[@id="ID01"]//tr[.//td[1][text()="Panama"]]//td[2]')

    for element in elements:
        print(element.text)

finally:
    driver.close()
