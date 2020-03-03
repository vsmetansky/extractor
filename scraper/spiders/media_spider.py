from urllib.parse import urlparse

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy import Reques

from scraper.items import FragmentItem, PageItem

IMG_QUERY = '//img/@src'
TXT_QUERY = '//p/*/text() | //*[number(substring-after(name(), "h")) > 0]/*/text()'


class MediaSpider(scrapy.CrawlSpider):
    name = 'media_spider'

    def __init__(self, base_url='', page_num=1, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.allowed_domains = (
            urlparse(base_url).netloc,)
        self.start_urls = (self.base_url,)
        self.rules = (
            Rule(LinkExtractor(allow_domains=self.allowed_domains), callback=self.parse_item, follow=True, process_request=self.count_links),)

        self.extracted_num = 0
        self.page_num = page_num

    def count_links(self, request, response):
        if self.extracted_num < self.page_num:
            self.extracted_num += 1
            return request
        raise CloseSpider('Specified number of pages processed')        

    def parse_item(self, response):
        images = self.__get_fragments(response, 'image', IMG_QUERY)
        text = self.__get_fragments(response, 'text', TXT_QUERY)

        return PageItem(url=response.meta['link_text'], fragments=images+text)

    def __get_fragments(self, response, type_name, query):
        return tuple(FragmentItem(type=type_name, data=val)
                     for val in response.xpath(query).getall() if val and not val.isspace())
