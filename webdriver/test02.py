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
from selenium.common import exceptions as Exceptions

sys.stderr = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

driver = None

def setUpModule():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)


def tearDownModule():
    global driver
    driver.close()


class TestOverwrite(unittest.TestCase):
    # 初期状態: <span id="ID01"><span id="ID02"></span></span> 
    # 2秒後この ID01のinnerHTML に 
    # <span id="ID02"><span class="CLASS">TEXT</span></span> 
    # を設定
    #
    # この場合、ID02の要素を取得しておいてから、classがCLASSである要素を
    # 取得できるのか確認するテスト(例外が発生する。test_03)


    def test_01(self):
        """ タイマーで遅れて表示される要素の取得。
        """

        driver.get('http://localhost/test02.html')
        element = driver.find_element_by_class_name('CLASS')
        self.assertEqual(element.text, 'TEXT')
        

    def test_02(self):
        """ タイマーで遅れて表示される要素の取得。
        xpathで上書きされる要素が存在する場合。
        """

        driver.get('http://localhost/test02.html')
        element = driver.find_element_by_xpath(
            '//span[@id="ID02"]/span[@class="CLASS"]')
        self.assertEqual(element.text, 'TEXT')


    def test_03(self):
        """ 取得した要素の親要素のinnerHTMLが上書きされている場合でも、
        その子要素を参照できるのか確認。
        """
        
        driver.get('http://localhost/test02.html')
        element1 = driver.find_element_by_id('ID02')

        # NoSuchElementException が発生する。
        # with self.assertRaises(Exceptions.NoSuchElementException):
        #     element1.find_element_by_class_name("CLASS")

        element1.find_element_by_class_name("CLASS")

        # is_enabledでも発生する
        with self.assertRaises(Exceptions.StaleElementReferenceException):
            element1.is_enabled()
        

class TestTimezone(unittest.TestCase):

    @unittest.skip("仕様がよくわからない")
    def test_01(self):

        # timezone設定がローカルと異なっている。
        # UTCとも違うらしい。(-60と出力される)

        driver.get('http://localhost/test02.html')
        element = driver.find_element_by_id('TZ_OFFSET')

        


if __name__ == '__main__':
    unittest.main()

