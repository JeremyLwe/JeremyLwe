# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from lianjiazufangCrawl.items import LianjiazufangListItem

class LianjiazufangcrawlPipeline(object):

    def __init__(self,mongo_uri,mongo_db,replicaset):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.replicaset = replicaset

    @classmethod
    def from_crawler(cls,crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'),mongo_db=crawler.settings.get('MONGO_DATABASE','lianjiazufang'),replicaset=crawler.settings.get('REPLICASET'))

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri,replicaset=self.replicaset)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item,LianjiazufangListItem):
            self._process_zufanglist_item(item)
        else:
            self._process_zufangdetail_item(item)
        return item

    def _process_zufanglist_item(self,item):
        item['houseTitle'] = item['houseTitle'].strip()
        item['houseArea'] = item['houseArea'].strip()
        item['houseDivision'] = item['houseDivision'].strip()
        self.db.houselist.insert(dict(item))

    def _process_zufangdetail_item(self,item):
        self.db.housedetail.insert(dict(item))

