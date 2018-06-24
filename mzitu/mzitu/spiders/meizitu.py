# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector,XmlXPathSelector
from ..items import MzituItem

class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['mzitu.com']
    # start_urls = ['http://mzitu.com/']

    def start_requests(self):
        url = 'http://www.mzitu.com/all/'
        yield Request(url=url,method='GET',callback=self.main_page)

    def main_page(self,response):
        # 取得所有套图地址
        hxs = Selector(response = response).xpath('//p[contains(@class,"url")]/a/@href').extract()
        for url in hxs:
            req = Request(url = url,
                          callback=self.fenye)
            yield req

    def fenye(self,response):
        # 取得图片路径和标题
        img_url = Selector(response=response).xpath('//div[@class="main-image"]//img/@src').extract_first().strip()
        title = Selector(response=response).xpath('//div[@class="main-image"]//img/@alt').extract_first().strip()
        yield MzituItem(img_url=img_url,title=title)
        # 取得下方导航条页面路径
        xhs = Selector(response=response).xpath('//div[@class="pagenavi"]/a/@href').extract()
        for url in xhs:
            req = Request(
                url=url,
                callback=self.fenye,
            )
            yield req




