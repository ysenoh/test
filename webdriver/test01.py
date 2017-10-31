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

sys.stderr = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

driver = None

def setUpModule():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('http://localhost/test.html')


def tearDownModule():
    global driver
    driver.close()


class TestXPath(unittest.TestCase):
    def test_01(self):
        """idが ID01である table要素 で、1列目のテキストが"Panama"である行の
        2列目の td要素を取得するテスト
        """

        elements = driver.find_elements_by_xpath(
            '//table[@id="ID01"]//tr[.//td[1][text()="Panama"]]//td[2]')
        self.assertEqual(len(elements), 1)
        self.assertEqual(elements[0].text, '68')


    def test_02(self):
        """ classと数値で絞り込んだ場合のテスト。
        """

        element = driver.find_element_by_xpath(
            '//div[@id="ID05"]/span[1]')
        self.assertEqual(element.text, 'TEXT1')

        element = driver.find_element_by_xpath(
            '//div[@id="ID05"]/span[@class="CLASS3"][1]')
        self.assertEqual(element.text, 'TEXT2')

        # '//div[@id="ID05"]/span[1][@class="CLASS3"]'だと
        # 要素が見つからず、タイムアウトになる。


    def test_03(self):
        """ 属性値の有無による判定
        """

        element = driver.find_element_by_xpath(
            '//div[@id="ID06"]/a[boolean(@href)]')
        self.assertEqual(element.text, 'ANCHOR1')

        element = driver.find_element_by_xpath(
            '//div[@id="ID06"]/a[not(boolean(@href))]')
        self.assertEqual(element.text, 'ANCHOR2')


    def test_04(self):
        """ xpathにおける text() と . の違いの確認
        """

        # text() は、その要素の直下のテキストのみ

        elements = driver.find_elements_by_xpath(
            '//div[@id="ID08"]//div[text()="ID08 TEXT"]')
        self.assertEqual(len(elements), 1)
        self.assertEqual(elements[0].get_attribute('id'), 'ID08_1')

        # . は、その子の要素も含む

        elements = driver.find_elements_by_xpath(
            '//div[@id="ID08"]//div[.="ID08 TEXT"]')
        self.assertEqual(len(elements), 2)
        self.assertSetEqual(
            set(elm.get_attribute('id') for elm in elements),
            {'ID08_1', 'ID08_2'})

        # <div id="ID08_3">ID08 TEXTA<span> SUB ELEMENT </span>TEXTB</div>
        # において、
        # text() 最初の1つのみのテキスト。"ID08 TEXTA"
        # text()[2]は2つめのテキスト。"TEXTB"

        elements = driver.find_elements_by_xpath(
            '//div[@id="ID08"]//div[text()="ID08 TEXTA"]')
        self.assertEqual(len(elements), 1)
        self.assertEqual(elements[0].get_attribute('id'), 'ID08_3')

        elements = driver.find_elements_by_xpath(
            '//div[@id="ID08"]//div[text()[2]="TEXTB"]')
        self.assertEqual(len(elements), 1)
        self.assertEqual(elements[0].get_attribute('id'), 'ID08_3')



class TestText(unittest.TestCase):
    def test_01(self):
        """ <br/> は改行文字に、&nbsp; はスペースに、
        連続するスペースは１つのスペースとして戻されることのテスト """

        element = driver.find_element_by_id('ID02_1')
        self.assertEqual(element.text, 'TEXT1\nTEXT2 TEXT3')

        for id in ['ID02_2', 'ID02_3', 'ID02_4']:
            element = driver.find_element_by_id(id)
            self.assertEqual(element.text, 'TEXT1 TEXT2')
        

    def test_02(self):
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


class TestFind(unittest.TestCase):
    def test_01(self):
        """ find_element_by_class_name は複数のクラスが指定されている場合の要素の取得。
        """
 
        element = driver.find_element_by_class_name("CLASS1")
        self.assertEqual(element.text, 'TEXT1')

        element = driver.find_element_by_class_name("CLASS2")
        self.assertEqual(element.text, 'TEXT1')

        

class TestAttribute(unittest.TestCase):
    def test_01(self):
        """ innerHTMLの取得。
        """

        element = driver.find_element_by_id('ID07')
        self.assertEqual(
            element.get_attribute('innerHTML'),
            '\n<span>TEXT</span>\n')


if __name__ == '__main__':
    unittest.main()
