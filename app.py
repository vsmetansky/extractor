import argparse

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


def read_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('website')
    parser.add_argument('-n', '--page-num',
                        dest='page_num', type=int, default=1)

    return parser.parse_args()


args = read_args()
process = CrawlerProcess(get_project_settings())

process.crawl('text_spider', domain=args.website, page_num=args.page_num)
process.start()
