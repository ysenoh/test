# 概要
WebDriverの動作に関する簡単なテスト。  
大したことは書いてない。  
正しいかどうかも良くわからない。  

# TEST01: 基本的なテスト
unittest形式で書いてあります。

+ [コード](test01.py) / [HTML](test.html)

# TEST02: 
何だったか失念。  
無理そうなことをやって、やっぱり無理だったやつだと思う。  
unittest形式で書いてあります。  

+ [コード](test02.py) / [HTML](test02.html)



# TEST04: implicit_wait と waitの関係のテスト
untilによるwaitでは、implicit_waitが効く場合と効かない場合がある。  

+ [コード](test04.py) / [HTML](test.html)


# TEST05: selectの選択操作
option要素を取得してclick()すれば良い。

+ [コード](test05.py) / [HTML](test05.html)


# TEST06: inputのvalueの完全一致によるwait
text_to_be_present_in_element_value は、部分一致なので、完全一致でwaitする場合は、自作する必要が有る。  
テストコードは、初期状態ではinputのテキストボックスに TEXT と表示されており、3sec後に空になり、更に3sec後に再度TEXTと設定される。(WebDriverではなく、JavaScriptによる動作)  
それと連動して、webdriverのコードは、test06:1、test06:2、test06:3 と表示する。

+ [コード](test06.py) / [HTML](test06.html)
