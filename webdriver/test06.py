from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import WebDriverException


class text_to_be_equal_to_element_value(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = driver.find_element(
                *self.locator).get_attribute("value")

            return element_text == self.text

        except EC.StaleElementReferenceException:
                return False


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://localhost/test06.html')

print("test06:1")
WebDriverWait(driver, 30).until(
    text_to_be_equal_to_element_value(
        (By.ID, 'ID01'), ''))

print("test06:2")
WebDriverWait(driver, 30).until(
    text_to_be_equal_to_element_value(
        (By.ID, 'ID01'), 'TEXT'))

print("test06:3")
driver.close()
