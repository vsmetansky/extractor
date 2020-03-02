import scrapy

from scraper.items import FragmentItem, PageItem

IMG_QUERY = '//img/@src'
TXT_QUERY = '//p/*/text() | //[substring-after(name(), "h") > 0]/*/text()'


class MediaSpider(scrapy.Spider):
    name = __name__

    def __init__(self, domain='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.domain = domain

    def start_requests(self):
        yield scrapy.Request(self.domain, self.parse)

    def parse(self, response):
        images = self.__get_fragments(response, 'image', IMG_QUERY)
        texts = self.__get_fragments(response, 'text', TXT_QUERY)

        return PageItem(url=self.domain, fragments=images+texts)

    def __get_fragments(self, response, type_name, query):
        return tuple(FragmentItem(type=type_name, data=val)
                     for val in response.xpath(query).getall())
