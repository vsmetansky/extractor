import argparse

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


def read_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('website')
    parser.add_argument('-n', '--page-num',
                        dest='page_num', type=int, default=10)

    return parser.parse_args()


def run():
    args = read_args()
    process = CrawlerProcess(get_project_settings())

    process.crawl('media_spider', base_url=args.website,
                  page_num=args.page_num)
    process.start()


if __name__ == '__main__':
    run()
