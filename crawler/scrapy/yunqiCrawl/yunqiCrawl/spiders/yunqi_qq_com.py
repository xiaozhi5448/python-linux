# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yunqiCrawl.items import YunqiBookListItem,YunqiBookDetialItem

class YunqiQqComSpider(CrawlSpider):
    name = 'yunqi.qq.com'
    allowed_domains = ['yunqi.qq.com']
    start_urls = ['http://yunqi.qq.com/bk/so2/n30p1']

    rules = (
        Rule(LinkExtractor(
             allow=r'/bk/so2/n30p\d+'),
             callback='parse_book_list',
             follow=True),
    )

    def parse_book_list(self, response):
        books = response.xpath('.//div[@class="book"]')
        for book in books:
            novelId = book\
                .xpath('./div[@class="book_info"]/h3/a/@id').extract_first()
            novelImageUrl = book\
                .xpath('./a/img/@src').extract_first()
            novelLink = book\
                .xpath('./div[@class="book_info"]/h3/a/@href').extract_first()
            novelTitle = book\
                .xpath('./div[@class="book_info"]/h3/a/text()').extract_first()
            novelInfos = book\
                .xpath('./div[@class="book_info"]/dl/dd[@class="w_auth"]')
            if len(novelInfos) > 4:
                novelAuthor = novelInfos[0].xpath('./a/text()').extract_first()
                novelTypeB = novelInfos[1].xpath('./a/text()').extract_first()
                novelStatus = novelInfos[2].xpath('./text()').extract_first()
                novelUpdateTime = novelInfos[3].xpath('./text()')\
                    .extract_first()
                novelWordsCount = novelInfos[4].xpath('./text()')\
                    .extract_first()
            else:
                novelAuthor = ''
                novelTypeB = ''
                novelStatus = ''
                novelUpdateTime = ''
                novelWordsCount = ''
            bookItem = YunqiBookListItem(
                novelId=novelId,
                title=novelTitle,
                link=novelLink,
                author=novelAuthor,
                status=novelStatus,
                updateTime=novelUpdateTime,
                wordsCount=novelWordsCount,
                novelType=novelTypeB,
                imageUrl=novelImageUrl
            )
            yield bookItem
            newRequest = scrapy.Request(
                url=novelLink,
                callback=self.parse_book_detail
            )
            print 'send request',novelLink
            newRequest.meta['novelId'] = novelId
            yield newRequest

    def parse_book_detail(self, response):
        novelId = response.meta['novelId']
        tdlist = response.xpath('.//div[@class="num"]/table/tr/td')
        novelAllClick = tdlist[0]\
            .xpath('./text()').extract_first().split(u'：')[1]
        novelAllLike = tdlist[1]\
            .xpath('./text()').extract_first().split(u'：')[1]
        novelWeekLike = tdlist[2]\
            .xpath('./text()').extract_first().split(r'：')[1]
        bookDetialItem = YunqiBookDetialItem(
            novelId=novelId,
            allClick=novelAllClick,
            allLike=novelAllLike,
            weekLike=novelWeekLike
        )
        yield bookDetialItem
