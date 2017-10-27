#  --*-coding:utf-8-*--

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


driver = None

def setUpModule():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('http://localhost/test.html')


def tearDownModule():
    global driver
    driver.close()


class Test1(unittest.TestCase):
    def test_01(self):
        """idが ID01である table要素 で、1列目のテキストが"Panama"である行の
        2列目の td要素を取得するテスト
        """

        elements = driver.find_elements_by_xpath(
            '//table[@id="ID01"]//tr[.//td[1][text()="Panama"]]//td[2]')
        self.assertEqual(len(elements), 1)
        self.assertEqual(elements[0].text, '68')


    def test_02(self):
        """ <br/> は改行文字に、&nbsp; はスペースに、
        連続するスペースは１つのスペースとして戻されることのテスト """

        element = driver.find_element_by_id('ID02_1')
        self.assertEqual(element.text, 'TEXT1\nTEXT2 TEXT3')

        for id in ['ID02_2', 'ID02_3', 'ID02_4']:
            element = driver.find_element_by_id(id)
            self.assertEqual(element.text, 'TEXT1 TEXT2')
        

    def test_03(self):
        """ 複数のspanタグで構成された要素のtext()の値のテスト 
        """

        # 子要素のタグ内のテキストは結合される
        element = driver.find_element_by_id('ID03_1')
        self.assertEqual(element.text, 'TEXT1TEXT2')

        # spanタグの間空白がある場合、その空白も入る
        element = driver.find_element_by_id('ID03_2')
        self.assertEqual(element.text, 'TEXT1 TEXT2')

        # spanタグの間改行がある場合、空白が入る
        element = driver.find_element_by_id('ID03_3')
        self.assertEqual(element.text, 'TEXT1 TEXT2')


    def test_03(self):
        """ 複数のdivタグで構成された要素のtext()の値のテスト 
        """

        # divタグのテキストは改行で結合される。
        # HTMLでは空行があってもそれは無視される。

        element = driver.find_element_by_id('ID04_1')
        self.assertEqual(element.text, 'TEXT1\nTEXT2')

        element = driver.find_element_by_id('ID04_2')
        self.assertEqual(element.text, 'TEXT1\nTEXT2')

        
if __name__ == '__main__':
    unittest.main()
