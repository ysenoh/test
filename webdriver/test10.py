#  --*-coding:utf-8-*--

import sys
import io
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


driver = None

def setUpModule():
    global driver
    driver = webdriver.Firefox()
    # driver = webdriver.Edge()
    # driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://localhost/test10.html')


def tearDownModule():
    driver.close()



class MyTest(unittest.TestCase):
    def test01(self):
        element = driver.find_element_by_xpath(
            '//span[.="日本語"]')

        self.assertEqual(element.get_attribute('id'), 'ID01')
        self.assertEqual(element.text, '日本語')

        element = driver.find_element_by_xpath(
            '//span[contains(., "日本")]')
        self.assertEqual(element.get_attribute('id'), 'ID01')

        element = driver.find_element_by_xpath(
            '//span[.="あいうえお"]')
        self.assertEqual(element.get_attribute('id'), 'ID02')

        element = driver.find_element_by_xpath(
            '//span[contains(., "あい")]')
        self.assertEqual(element.get_attribute('id'), 'ID02')

        element = driver.find_element_by_xpath(
            '//span[.="☺"]')
        self.assertEqual(element.get_attribute('id'), 'ID03')


if __name__ == '__main__':
    unittest.main()

