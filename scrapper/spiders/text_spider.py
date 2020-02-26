import scrapy


class TextSpider(scrapy.Spider):
    name = 'text_spider'

    def __init__(self, domain='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.domain = domain

    def start_requests(self):
        yield scrapy.Request(self.domain, self.parse)

    def parse(self, response):
        for img in response.xpath('//img').getall():
            ...

        
