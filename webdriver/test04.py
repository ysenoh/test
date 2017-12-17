#  --*-coding:utf-8-*--

import sys
import io
import unittest
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import WebDriverException

sys.stderr = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def waitUntil(cond):
    t0 = time.time()

    try:
        WebDriverWait(driver, 0).until(cond)
        
    except WebDriverException:
        t1 = time.time()
        print('{0:.2f}'.format(t1-t0))



driver = webdriver.Firefox()

driver.implicitly_wait(10)
driver.get('http://localhost/test.html')

waitUntil(EC.presence_of_element_located((By.ID, "notexists"))) # 約10sec
waitUntil(EC.title_contains('HOME')) # 約0sec
driver.close()

