# Selenium/WebDriver 覚え書き


+ [Selenium with Python マニュアル(英語)](http://selenium-python.readthedocs.io/index.html)


## titleによるwait
```
    WebDriverWait(driver, 10).until(
        EC.title_contains('ほげほげ'))
```

## xpathによる指定

### クラス名でspanタグを指定して、その中のcheckboxを取得する
'''
    element = driver.find_element_by_xpath(
        '//span[@class="CLASS NAME"]//input[@type="checkbox"]')
'''


### クラス名の一部で inputを取得する
'''
    element = driver.find_element_by_xpath(
        '//input[contains(@class, "CLASS NAME")]')
'''

+ [(MSDN)contains 関数 (XPath)](https://msdn.microsoft.com/ja-jp/library/ms256195(v=vs.120).aspx)
