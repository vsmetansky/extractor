import logging

from scraper.exporters import XmlPageItemExporter
from scraper.types import IMAGE, TEXT


class XmlExportPipeline(object):
    """Serialize items to XML in specific format"""

    def open_spider(self, spider):
        self.file = open(spider.file_name, 'w')
        self.exporter = XmlPageItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class AverageCounterPipeline(object):
    """Count average occurance of fragments"""

    def open_spider(self, spider):
        self.images_num = self.text_num = 0
        self.logger = logging.getLogger(__name__)

    def close_spider(self, spider):
        self.logger.info(
            f'Average number of images: {self.images_num / spider.page_num}')
        self.logger.info(
            f'Average number of text sections: {self.text_num / spider.page_num}')

    def process_item(self, item, spider):
        images = tuple(filter(lambda x: x['type'] == IMAGE, item['fragments']))
        text = tuple(filter(lambda x: x['type'] == TEXT, item['fragments']))
        self.images_num += len(images)
        self.text_num += len(text)
        return item
