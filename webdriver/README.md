# Selenium/WebDriver 覚え書き


+ [Selenium with Python マニュアル(英語)](http://selenium-python.readthedocs.io/index.html)


## titleによるwait
```
    WebDriverWait(driver, 10).until(
        EC.title_contains('TITLEの一部'))
```

## xpathによる指定

クラス名でspanタグを指定して、その中のcheckboxを取得する
```
    element = driver.find_element_by_xpath(
        '//span[@class="完全なクラス名属性値"]//input[@type="checkbox"]')
```


クラス名の一部で inputを取得する
```
    element = driver.find_element_by_xpath(
        '//input[contains(@class, "クラス名属性値の一部")]')
```

+ [(MSDN)contains 関数 (XPath)](https://msdn.microsoft.com/ja-jp/library/ms256195(v=vs.120).aspx)


あるクラスか、別なクラスのspanタグのどちらか存在する方を取得する。
```
    element = driver.find_element_by_xpath(
        '//span[@class="クラス名1"]|//span[@class="クラス名2"]')
```

取得した要素以下から要素を取得する。
```
    parentElement = driver.find_element_by_xpath(
        '//span[@class="クラス名"]')
    childElement = parentEleme.find_element_by_xpath(
        './/input')
```
つまり、xpathの先頭 '.'を付加する。  
'//' で始めると、ドキュメント全体から検索されることに注意する。  



## Alert/Dialogの操作
```
    Alert(driver).accept()
    Alert(driver).dismiss()
```
