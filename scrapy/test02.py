# -*- coding: utf-8 -*-

import sys
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
from scrapy.settings import Settings

class MySpider(CrawlSpider):
    name = 'mySpider'

    # 全てのページに対してそのパースを行い、更にそのリンク先も対象としている。
    rules = [Rule(LinkExtractor(), callback='parsePage', follow=True)]

    def parsePage(self, response):
        sel = response.selector
        item = MyItem()
        item['URL'] = response.url
        item['title'] = sel.xpath('/html/head/title/text()').extract()

        # LOG_LEVELをINFO以上にすると、何を読み込んでいるのか表示されないので、テスト用に表示している。
        # 処理としては必要ない
        print(response.url)

        # HTMLが必要な場合は、ここでファイルに保存する
        # print(response.body)

        return item


class MyItem(Item):
    URL = Field()
    title = Field()
    pass



# scrapy の設定をしている。(settings.pyの記述に相当)
# サーバに負荷を掛けないように、以下のようにしている。
#   robot.txtで判定している
#   ダウンロードの間隔として1secあける (DOWNLOAD_DELAY)
#   走査する深さは1 (DEPTH_LIMIT)
# debug情報が画面に流れるのが邪魔なので、LOG_LEVELはINFOにした。
# out.csv に、MyItem で定義した、URLとTitleの一覧が　utf-8でCSV出力されるようにしている。
#
# 設定の詳細については、https://doc.scrapy.org/en/latest/topics/settings.html 参照

settingVals = {
    'ROBOTSTXT_OBEY': True,
    'DOWNLOAD_DELAY': 1,
    'DEPTH_LIMIT': 1,
    'LOG_LEVEL': 'INFO',
    'FEED_URI': 'file:out.csv', 
    'FEED_FORMAT': 'csv',
    'FEED_EXPORT_ENCODING': 'UTF-8'}


if len(sys.argv) < 3:
    print('Usage: python3 test02.py domainName startUrl')
    sys.exit(1)


process = CrawlerProcess(Settings(settingVals))

MySpider.allowed_domains = [sys.argv[1]]
MySpider.start_urls = [sys.argv[2]]

process.crawl(MySpider)
process.start()
sys.exit(0)
