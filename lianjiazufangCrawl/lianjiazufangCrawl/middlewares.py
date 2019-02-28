# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from settings import USER_AGENTS,PROXIES

class RandomUserAgent(object):
    def process_request(self,requset,spider):
        useragent = random.choice(USER_AGENTS)
        requset.headers.setdefault('User-Agent',useragent)


class RandomProxy(object):
    def process_request(self, request,spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = proxy['ip_port']
