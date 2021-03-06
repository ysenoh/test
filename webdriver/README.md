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
詳細については、各ExpectedConditionクラスの実装を見ると良い。  
具体的には、findなどで取得して、条件に合うか確認しており、waitはこれををポーリングで回しているだけっぽい。  

別件であるが、waitはfind系と異なり、xpathの書式が間違っていてもエラーにならない(例外が握りつぶされているらしい)事に注意する。  

+ [コード](test04.py) / [HTML](test.html)


# TEST05: selectの選択操作
option要素を取得してclick()すれば良い。

+ [コード](test05.py) / [HTML](test05.html)


# TEST06: inputのvalueの完全一致によるwait
text_to_be_present_in_element_value は、部分一致なので、完全一致でwaitする場合は、自作する必要が有る。  
テストコードは、初期状態ではinputのテキストボックスに TEXT と表示されており、3sec後に空になり、更に3sec後に再度TEXTと設定される。(WebDriverではなく、JavaScriptによる動作)  
それと連動して、webdriverのコードは、test06:1、test06:2、test06:3 と表示する。

+ [コード](test06.py) / [HTML](test06.html)


# TEST07: ブラウザの状態とfocus/blurの動作
少なくともFirefoxは、ブラウザがactive windowとして表示されていないと、focus/blurイベントが発生しないらしい。  
つまり、WebDriverによるテストで、ブラウザを下に隠してしまうと、動作が変わってしまう。  
EdgeやChromeでも、差はあれ、動作に影響があるようである。  
その対策として、明示的に blurを実行するようにコードを書いたが、FirefoxとEdgeでは動作しなかった。  

テストコードは、blurイベントでalertを表示するようにしている。  
テストコードは、そのまま実行すると、5secほど待って、一瞬alertが表示され、正常終了する。  
その5secの間に、Alt-tab操作などで、他のアプリをactiveにすると、alertが表示されず、タイムアウトする。  

+ [コード](test07.py) / [HTML](test07.html)

# TEST08: ブラウザのメソッドの戻り値を取得するテスト
driver.execute_script の戻り値として、メソッドの戻り値を取得することができる。  
ただし、その場合は、returnを付けて呼び出さないと、動作しないようである。  

+ [コード](test08.py) / [HTML](test08.html)


# TEST09: 不可視な要素とそのテキストの取得
親要素のスタイルが、display:none で表示されていない要素に対しては以下のように動作するようである。
1. その要素の取得は可能。(その内部のテキストも条件に使用できる)  
1. ただし、その要素の text は空文字列になる。  

+ [コード](test09.py) / [HTML](test09.html)


# TEST10: 日本語の使用
utf-8による、漢字とひらがなと絵文字の簡単なテスト。  

+ [コード](test10.py) / [HTML](test10.html)


# TEST11: Edgeのバグ？(xpathによるテーブルの複数のセルの取得)
xpathで、 //tr//td[1] と指定した時、FirefoxとChromeは全ての行の1列目を取得できるが、Edeのみ1行目の1列目を取得するようである。  
尚、//tr//td だと、Edgeでも全ての行のセルを取得するので、多分これはEdgeのバグではないか。  


+ [コード](test11.py) / [HTML](test11.html)


# TEST12: 子ウィンドウの操作
子ウィンドウが開くと、window_handles の長さが変わる。  
新規の子ウィンドウは一番最後に追加されるようである。  
戻るには、switch_to.window()を使用する。

動的にiframeを生成しても、それはウィンドウとしては扱われないらしい。  
該当するiframe要素を配列で取得し、その個数で判別する。  
戻るには、switch_to.default_content() を使用する。  

+ [コード](test12.py) / [HTML(親)](test12.html) / [HTML(子)](test12b.html)


# TEST13: alertのacceptの完了タイミング
Edgeの場合、alertのacceptの直後に find_element系の処理をすると、まだalertが表示されているものとして、UnexpectedAlertPresentException がraiseされることがある。  
ただし、alertが2回連続して表示される場合に、2回連続してacceptとしても、これは正常に動作するようである。  
多分、acceptはaccept可能になるまで内部的にwaitしており、既にacceptされたalertが表示されていても、それは無視されているのだと思う。  

実装の都合として、alertが連続して表示されるか、そうでないかを区別して、手順を組むことはしたくない。  
単純に、「alertが表示されなくなるまでwaitする」だと、そのwaitが入ったタイミングで既に2つめのalertが表示されている場合に、timeoutで終了してしまう可能性がある。  

alertが連続して表示される場合、そのテキストは異なっているものとし、alertが存在しないか、そのテキストが異なるまでwaitする条件オブジェクトを定義した。

なお、webdriverのAlertのコードを読むと、alertは個別には識別されておらず、driverに対して、カレントのalertの操作として実装されている。  
そのため、alertが表示されていないかは判別できても、あるalertが閉じたかどうかは判別できないようである。  
+ [コード](test13.py) / [HTML](test13.html)

## 追記
都合があって、上記の件はCreators updateを当てる前の環境での話だったのだが、当てたところ更におかしくなって、alertが表示された直後だとaccept出来ないことがあるという現象まで発生。  
Edgeの場合は 0.5secほどsleepするようにした。(このテストコードには書いてない)


# TEST14: XPathにおける特殊文字のエスケープ
XPath2.0ならば、' と " は、それを２つ重ねることでエスケープすることが出来るらしい。  
しかし、少なくとも主要なブラウザ(Firefox / Chrome / Edge)は XPath1.0までしか対応していないらしい。  
' か " の一方だけならば、もう一方をくくり文字として使用することで、そのまま記述することができる。  
混在する場合は、それらを別の文字列として記述し、それを XPathのConcat関数で結合することで対応できる。  

尚、 < や > などは、そのまま文字列内に記述出来るようである。

+ [コード](test14.py) / [HTML](test14.html)
