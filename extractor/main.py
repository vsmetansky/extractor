"""Main module of the package, runs and setups it."""

import argparse
import os

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

SETTINGS_PATH = 'extractor.scraper.settings'


def setup():
    """Prepares package for running."""
    os.environ['SCRAPY_SETTINGS_MODULE'] = SETTINGS_PATH


def read_args():
    """Reads command line argumens.

    Returns:
        Populated Namespace object.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'url', help='URL of website that you want to scrape.')
    parser.add_argument('-f', '--file-name', dest='file_name',
                        type=str, default='data.xml', help='Name of file for XML serialization.')
    parser.add_argument('-n', '--page-num', dest='page_num',
                        type=int, default=20, help='Number of pages that should be scraped.')

    return parser.parse_args()


def run():
    """Setups and runs 'media_spider'."""

    setup()
    args = read_args()

    process = CrawlerProcess(get_project_settings())
    process.crawl('media_spider', base_url=args.website,
                  page_num=args.page_num, file_name=args.file_name)
    process.start()
