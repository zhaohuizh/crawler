from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.item import Item

class CompaniesSpider(CrawlSpider):
  name = "companies"
  allowed_domains = "www.glassdoor.com"
  start_urls = [
    "http://www.glassdoor.com/Reviews/company-reviews.htm"
  ]
  rules = (Rule(SgmlLinkExtractor(allow=['/Reviews/company-reviews-SRCH_IP\d+\.htm']), callback = 'parse_item', follow = True),)
 
  def parse_item(self, response):
    sel = Selector(response)
    items = []
    lists = sel.xpath('//tt[@class="i-emp"]').extract()
    for com in lists:
      item = Item()
      item['title'] = com
      items.append(item)
    return (items)
