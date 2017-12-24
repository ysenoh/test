#  --*-coding:utf-8-*--

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains


driver = None

def setUpModule():
    global driver
    driver = webdriver.Firefox()
    # driver = webdriver.Edge()
    # driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://localhost/test09.html')


def tearDownModule():
    global driver
    driver.close()


class MyTest(unittest.TestCase):
    def test01(self):
        element = driver.find_element_by_xpath(
            '//span[@id="ID01"]')
        self.assertEqual(element.text, 'TEST01')

        element = driver.find_element_by_xpath(
            '//span[.="TEST01"]')
        self.assertEqual(element.get_attribute('id'), 'ID01')

        element = driver.find_element_by_xpath(
            '//span[@id="ID02"]')
        self.assertEqual(element.text, '')

        element = driver.find_element_by_xpath(
            '//span[.="TEST02"]')
        self.assertEqual(element.get_attribute('id'), 'ID02')


if __name__ == '__main__':
    unittest.main()



