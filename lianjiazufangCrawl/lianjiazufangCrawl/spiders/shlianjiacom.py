# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from lianjiazufangCrawl.items import LianjiazufangListItem,LianjiazufangDetailItem
from scrapy.http import Request

class ShLianjiaComSpider(CrawlSpider):
    name = 'sh.lianjia.com'
    allowed_domains = ['sh.lianjia.com']
    start_urls = ['http://sh.lianjia.com/zufang/pg1/#contentList']

    rules = (
        Rule(LinkExtractor(allow=r'/pg\d+/#contentList'), callback='parse_house_list', follow=True),
    )

    def parse_house_list(self, response):
        houses = response.xpath(".//div[@class='content__list--item']")
        for house in houses:
            houseTitle = house.xpath("./div[@class='content__list--item--main']/p[1]/a/text()").extract_first()
            houseLink_zero = house.xpath("./div[@class='content__list--item--main']/p[1]/a/@href").extract_first()
            houseLink = 'http://sh.lianjia.com' + houseLink_zero
            houseAddress_1 = house.xpath("./div[@class='content__list--item--main']/p[2]/a[1]/text()").extract_first()
            houseAddress_2 = house.xpath("./div[@class='content__list--item--main']/p[2]/a[2]/text()").extract_first()
            houseAddress = houseAddress_1 + "-" + houseAddress_2
            houseArea = house.xpath("./div[@class='content__list--item--main']/p[2]/text()[2]").extract_first()
            houseDivision = house.xpath("./div[@class='content__list--item--main']/p[2]/text()[4]").extract_first()
            housePrice = house.xpath("./span[@class='content__list--item-price']/text()").extract_first()
            houseImageurl = house.xpath("./a/img/@src").extract_first()
            zufangListItem = LianjiazufangListItem(houseTitle=houseTitle,houseLink=houseLink,houseAddress=houseAddress,houseArea=houseArea,houseDivision=houseDivision,housePrice=housePrice,houseImageurl=houseImageurl)
            yield zufangListItem

            request = scrapy.Request(url=houseLink,callback=self.parse_house_detail)
            request.meta['houseTitle']=houseTitle
            yield request

    def parse_house_detail(self,response):
        houseTitle = response.meta['houseTitle']
        houseUpdate = response.xpath(".//div[@class='content__article__info']/ul/li[2]/text()").extract_first()
        houseTenancy = response.xpath(".//div[@class='content__article__info']/ul/li[5]/text()").extract_first()
        houseView = response.xpath(".//div[@class='content__article__info']/ul/li[6]/text()").extract_first()
        houseContactperson = response.xpath(".//div[@class='content__aside__list--title oneline']/span[1]/text()").extract_first()
        houseTelephone = response.xpath(".//div[@class='content__aside fr']/ul[2]/li/p[2]/text()").extract_first()
        zufangDetailItem = LianjiazufangDetailItem(houseTitle=houseTitle,houseUpdate=houseUpdate,houseTenancy=houseTenancy,houseView=houseView,houseContactperson=houseContactperson,houseTelephone=houseTelephone)
        yield zufangDetailItem
