"""Declares classes that represent extracted data.

Exported classes:
    PageItem: A class that represents <page> tag and its contents.
    FragmentItem: A class that represents <fragment> tag and its contents.
"""

import scrapy


class PageItem(scrapy.Item):
    """Represents <page> tag and its contents."""

    url = scrapy.Field()
    fragments = scrapy.Field()


class FragmentItem(scrapy.Item):
    """Represents <fragment> tag and its contents."""

    type = scrapy.Field()
    data = scrapy.Field()
