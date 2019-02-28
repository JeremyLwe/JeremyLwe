from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lianjiazufangCrawl.spiders.shlianjiacom import ShLianjiaComSpider

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('sh.lianjia.com')
    process.start()