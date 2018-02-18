# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerRunner
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer

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



@defer.inlineCallbacks
def crawl(runner, crawl_targets):
    for domains, urls in crawl_targets:
        MySpider.allowed_domains = domains
        MySpider.start_urls = urls
        yield runner.crawl(MySpider)

    reactor.stop()



# crawlを sequentially に行う関数
# 1つのプロセス内で、reactorは再起動できないっぽい事に注意。
# https://doc.scrapy.org/en/latest/topics/practices.html#running-multiple-spiders-in-the-same-process

def runCrawlerSequentially(settingVals, crawl_targets):
    configure_logging()
    runner = CrawlerRunner(Settings(settingVals))
    crawl(runner, crawl_targets)
    reactor.run()


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

crawl_targets = [
    (['news.yahoo.co.jp'], ['https://news.yahoo.co.jp/']),
    (['weather.yahoo.co.jp'], ['https://weather.yahoo.co.jp/weather/'])]

runCrawlerSequentially(settingVals, crawl_targets)


