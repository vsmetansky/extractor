import scrapy


class PageItem(scrapy.Item):
    url = scrapy.Field()
    fragments = scrapy.Field()


class FragmentItem(scrapy.Item):
    type = scrapy.Field()
    data = scrapy.Field()
