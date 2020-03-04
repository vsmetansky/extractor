from scraper.exporters import XmlPageItemExporter


class XmlExportPipeline(object):
    """Serialize items to XML in specific format"""

    def open_spider(self, spider):
        self.file = open('data.xml', 'w')
        self.exporter = XmlPageItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
