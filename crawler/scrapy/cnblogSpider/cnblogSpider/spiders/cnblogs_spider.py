#!/usr/local/env python
# encoding:utf-8
import scrapy
from scrapy import Selector
from cnblogSpider.items import CnblogspiderItem
class CnblogSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ['cnblogs.com']
    start_urls = [
        'https://www.cnblogs.com/qiyeboy/default.html?page=1'
    ]
    def parse(self, response):
        all_articles = response.xpath(".//*[@class='day']")
        for article in all_articles:
            title = article.xpath('.//*[@class="postTitle"]/a/text()').extract()[0]
            abstract = article.xpath('.//*[@class="postCon"]/div/text()').extract()[0]
            href = article.xpath('.//*[@class="postTitle"]/a/@href').extract()[0]
            day = article.xpath('.//*[@class="dayTitle"]/a/text()').extract()[0]
            # print title,'\n',day,'\n',href,'\n',abstract,'\n'
            item = CnblogspiderItem(url=href, title=title, abstract=abstract, day=day)
            request = scrapy.Request(url=href, callback=self.pase_body)
            request.meta['item'] = item
            yield request
        next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)

    def pase_body(self, response):
        item = response.meta['item']
        body = response.xpath(".//*[@class='postBody']")
        item['cimage_urls'] = body.xpath('.//img//@src').extract()
        yield item
