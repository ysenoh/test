# 概要
scrapy の動作等に関する簡単なテストと備忘録。  
大したことは書いてない。  
正しいかどうかも良くわからない。  

[Scrapy documentation](https://doc.scrapy.org/en/latest/index.html)

# インストール
cygwin環境にscrapyをインストールした際のメモ。

scrapy のインストール ([Installation guide](https://doc.scrapy.org/en/latest/intro/install.html))
```
pip3 install scrapy
```

ただし、gccによるコンパイルがあるらしく、その際にpython.h などが必要になるらしい。  
cygwinのインストーラを使用して、python3_devel をインストールしておく必要が有る。  

チュートリアル用のプロジェクトの作成 ([Scrapy Tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html))
```
scrapy startproject turtorial
```

turtorial というのは、ただのプロジェクト名で、特に意味があるわけではないらしい。  
ただし、これを実行するためには、通信系のライブラリがインストールされている必要があるらしく、以下のインストールが完了している必要があるらしい。  
本当に全て必要なのかは良くわからない。

```
pip3 install service_identity
pip3 install pyasn1 pyasn1-modules
pip3 install --upgrade google-auth-oauthlib
```

# scrapyの構成
正しいか良くわからないが、多分こうなんだろうということ等。  

+ scrapyの [CrawlSpider](https://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider)は、リンク先を追跡することで、webサイトのクロールを行う。  
  + 設定は settings.py に記述する。
    + これは scrapyコマンドから実行した場合。[API](https://doc.scrapy.org/en/latest/topics/api.html)で呼び出す場合は、読み込まれないはず。
  + 待ち時間は、[DOWNLOAD_DELAY](https://doc.scrapy.org/en/latest/topics/settings.html#download-delay) で設定する。デフォルトは待たない。
  + 探査する深さの上限は[DEPTH_LIMIT](https://doc.scrapy.org/en/latest/topics/settings.html#depth-limit) で設定する。デフォルトは制限なし。
+ scrapy は、webページの内容をパースして、1ページ1件として、CSV等の形式で出力するものである。
  + ただし、そのパース処理(下記のcallbackで指定)の中でwebページの内容をファイル等に出力するコードを書くことも可能である。
+ 追跡するルールなどは、CrawlSpiderのサブクラスで定義する。
  + このルールは、CrawlSpiderのサブクラスの
[allowed_domains](https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider.allowed_domains)、
[start_urls](https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider.start_urls)、
[rules](https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.CrawlSpider.rules) というクラス変数に設定する。
  + rulesには、[Rule](https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Rule)の配列を設定する。
  + Ruleは、条件が成立した場合に、どうするかを設定するものである。
    + 条件は、LinkExtractor で指定する。これは[LxmlLinkExtractor](https://doc.scrapy.org/en/latest/topics/link-extractors.html#module-scrapy.linkextractors.lxmlhtml)の別名である。
    + callbackを指定すると、そのcallback先でパース処理を行う。  
      callbackはメソッド名を文字列で渡す。(文字列ではなくシンボルとしても渡せるらしいがよくわからない)
    + follow に Trueを設定すると、その先のページも探査する。  
      デフォルトでは、callbackが指定されていない場合は Trueとして扱われるが、指定されている場合は、Falseとして扱われることに注意する。
+ scrapy crawl クロール名　で、クロールを実行できる
  + クロール名は、CrawlSpiderのサブクラスの nameというクラス変数に設定する。
+ CSV等で出力する項目は、[Item](https://doc.scrapy.org/en/latest/topics/items.html#item-objects) から継承したクラスで定義する
  + このクラスは標準的には items.py で定義するものらしい (多分、ファイル名はなんでも良い)
  + この項目値は、pythonのdict型(連想配列)の様にアクセスできるが、この定義により、間違った名前などを使用すると例外がraiseされる。
  + 定義は、その項目名を名前とするクラス変数に Field型のインスタンスを設定することにより行う。
  + これは、[django](https://docs.djangoproject.com/en/dev/topics/db/models/) のモデルとよく似たものらしい。
+ item情報の出力を処理する場合は、[pipeline](https://doc.scrapy.org/en/latest/topics/item-pipeline.html#item-pipeline)
を使用する。
  + 使用する pipelineのクラスは、[ITEM_PIPELINES](https://doc.scrapy.org/en/latest/topics/settings.html#item-pipelines) で指定する。
+ scrapy コマンドを使用しないで、scrapyを使用するには、[CrawlerProcess](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerProcess)を使用する。([Run Scrapy from a script](https://doc.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script))
  + この場合は、settings.py による、設定の初期化はされていないようである。
  + これは[Settings](https://doc.scrapy.org/en/latest/topics/api.html#scrapy.settings.Settings)に設定して、それをCrawlerProcessに引き渡すことで行う。
  + Settings も辞書型のように扱え、また辞書型のデータを与えても動作するらしいが、Settingsを使用すると名前の間違いなどを判定してくれるのだと思う。

# TEST01
複数のサイトに対して、sequentially にcrawl するテスト。  
scrapy は Twisted asynchronous networking library を使用しており、そのエンジンをreactorと呼ぶらしい。  
このreactorは、プロセス内では、一度止めると再起動できないらしい。  
そのため、逐次的に処理する場合は、defer.inlineCallbacks 修飾子を使用して、実行手順を示した上で、まとめて実行するらしい。  
詳細は [Running multiple spiders in the same process](https://doc.scrapy.org/en/latest/topics/practices.html#running-multiple-spiders-in-the-same-process) 参照

crawlするサイトを動的に変更するには、定義した　CrawlSpider　のサブクラス内に設定している、allowed_domains と　start_urls に設定すればよいらしい。

test01.py は、yahoo news と yahoo 天気を対象として、それらのURLとタイトルを out.csvに出力する。  
その際、yahoo newsからすべて読み込むまで、yahoo天気の読み込みは開始しない。  
サーバの負荷を考慮して、1sec待ち、読み込みの深さは1としている。  

- [test01.py](test01.py)
