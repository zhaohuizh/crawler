from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from glassdoor.items import GlassdoorItem

class MySpider(CrawlSpider):
    name = "companies"
    allowed_domains = ["glassdoor.com"]
    start_urls = ["http://www.glassdoor.com/Reviews/company-reviews.htm"]   
    rules = (Rule (SgmlLinkExtractor(allow=("/Reviews/company-reviews-SRCH_IP\d+\.htm", ),), callback="parse_items", follow= True),)

    def parse_items(self, response):
        sel = Selector(response)
        items = []
        lists = sel.xpath('//tt[@class="i-emp"]/text()').extract()
        lists = list(set(lists))
        for com in lists:
            item = GlassdoorItem()
            item['name'] = com
            items.append(item)
        return (items)
