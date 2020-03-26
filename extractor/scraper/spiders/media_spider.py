"""Provides 'scraper' with spider class for extracting text and media."""

import re
from urllib.parse import urlparse

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

from extractor.scraper.items import FragmentItem, PageItem
from extractor.scraper.types import IMAGE, TEXT

IMG_QUERY = '//img/@src'
TXT_QUERY = '//*[not(name()="script") and not(name()="style")]/text()'

STOP_MSG = 'Scraped all the pages!'


class MediaSpider(CrawlSpider):
    name = 'media_spider'

    def __init__(self, base_url, page_num, *args, **kwargs):
        self.allowed_domains = (
            urlparse(base_url).netloc,)
        self.start_urls = (base_url,)
        self.rules = (
            Rule(LinkExtractor(allow_domains=self.allowed_domains),
                 callback=self.parse_item, follow=True),)
        self.extracted_num = 0
        self.page_num = page_num
        super().__init__(*args, **kwargs)

    def count_links(self):
        if self.extracted_num < self.page_num:
            self.extracted_num += 1
        else:
            raise CloseSpider(STOP_MSG)

    def parse_item(self, response):
        self.count_links()
        images = self.__get_fragments(response, IMAGE, IMG_QUERY)
        text = self.__get_fragments(response, TEXT, TXT_QUERY)
        return PageItem(url=response.url, fragments=images+text)

    def __get_fragments(self, response, type_name, query):
        return tuple(FragmentItem(type=type_name, data=' '.join(re.split('\s+?', val.strip())))
                     for val in response.xpath(query).getall() if not val.isspace())
