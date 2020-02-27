import scrapy

from scraper.items import FragmentItem, PageItem


class TextSpider(scrapy.Spider):
    name = 'text_spider'

    def __init__(self, domain='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.domain = domain

    def start_requests(self):
        yield scrapy.Request(self.domain, self.parse)

    def parse(self, response):
        images = tuple(FragmentItem(type='image', data=img_src)
                       for img_src in response.xpath('//img/@src').getall())
        texts = tuple(FragmentItem(type='text', data=text)
                      for text in response.xpath('//p/text()').getall())

        return PageItem(url=self.domain, fragments=images+texts)
