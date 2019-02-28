# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest
import json
from lagouCrawl.items import LagoucrawlItem

class LagoujobSpider(CrawlSpider):
    name = 'lagouJob'
    allowed_domains = ['www.lagou.com']

    def start_requests(self):
        url = 'https://www.lagou.com/jobs/positionAjax.json'
        requests = []
        for pn in range(1,5):
            params = {'first':'true','pn':str(pn),'kd':'爬虫'}
            request = FormRequest(url,callback=self.parse_item,formdata=params)
            requests.append(request)
        return requests

    def parse_item(self, response):
        json_data = json.loads(response.text)
        results = json_data['content']['positionResult']['result']
        for result in results:
            item = LagoucrawlItem()
            item['companyFullName'] = result['companyFullName']
            item['companySize'] = result['companySize']
            item['createTime'] = result['createTime']
            item['education'] = result['education']
            item['industryField'] = result['industryField']
            item['positionId'] = result['positionId']
            item['positionName'] = result['positionName']
            item['workYear'] = result['workYear']
            item['city'] = result['city']
            yield item
