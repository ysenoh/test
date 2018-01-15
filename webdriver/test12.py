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

# _blankで開いたタブの取得のテスト


driver = None

def setUpModule():
    global driver
    # driver = webdriver.Firefox()
    # driver = webdriver.Edge()
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)


def tearDownModule():
    driver.close()



class MyTest(unittest.TestCase):
    def test01(self):
        """ targetが _blankであるリンクのウィンドウ切り替えのテスト """

        driver.get('http://localhost/test12.html')

        numOfWins = len(driver.window_handles)

        driver.find_element_by_id('ID01').click()
        WebDriverWait(driver, 5).until(
            lambda d: len(d.window_handles) > numOfWins)

        parentWin = driver.current_window_handle
        driver.switch_to.window(driver.window_handles[-1])

        element = driver.find_element_by_id('TEXT1')
        self.assertEqual(element.text, 'CHILD WINDOW')
        
        driver.close()
        driver.switch_to.window(parentWin)

        element = driver.find_element_by_id('TEXT1')
        self.assertEqual(element.text, 'PARENT WINDOW')


    def test02(self):
        """ window.openで開いたウィンドウへの切り替えのテスト """

        driver.get('http://localhost/test12.html')

        numOfWins = len(driver.window_handles)

        driver.find_element_by_id('ID02').click()
        WebDriverWait(driver, 5).until(
            lambda d: len(d.window_handles) > numOfWins)

        parentWin = driver.current_window_handle
        driver.switch_to.window(driver.window_handles[-1])

        element = driver.find_element_by_id('TEXT1')
        self.assertEqual(element.text, 'CHILD WINDOW')
        
        driver.close()
        driver.switch_to.window(parentWin)

        element = driver.find_element_by_id('TEXT1')
        self.assertEqual(element.text, 'PARENT WINDOW')


if __name__ == '__main__':
    unittest.main()

