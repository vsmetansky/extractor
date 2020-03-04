from urllib.parse import urlparse

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider

from scraper.items import FragmentItem, PageItem

IMG_QUERY = '//img/@src'
TXT_QUERY = '//p/*/text() | //*[number(substring-after(name(), "h")) > 0]/*/text()'


class MediaSpider(CrawlSpider):
    name = 'media_spider'

    def __init__(self, base_url='', file_name='', page_num=1, *args, **kwargs):
        self.allowed_domains = (
            urlparse(base_url).netloc,)
        self.start_urls = (base_url,)
        self.rules = (
            Rule(LinkExtractor(allow_domains=self.allowed_domains),
                 callback=self.parse_item, follow=True),)
        self.extracted_num = 0
        self.page_num = page_num
        self.file_name = file_name
        super().__init__(*args, **kwargs)

    def count_links(self):
        if self.extracted_num < self.page_num:
            self.extracted_num += 1
        else:
            raise CloseSpider('Scraped all the pages!')

    def parse_item(self, response):
        self.count_links()
        images = self.__get_fragments(response, 'image', IMG_QUERY)
        text = self.__get_fragments(response, 'text', TXT_QUERY)
        return PageItem(url=response.url, fragments=images+text)

    def __get_fragments(self, response, type_name, query):
        return tuple(FragmentItem(type=type_name, data=val)
                     for val in response.xpath(query).getall() if val and not val.isspace())
