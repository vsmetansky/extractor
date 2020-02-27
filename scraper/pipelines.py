from scraper.exporters import XmlPageItemExporter


class XmlExportPipeline(object):
    """Serialize items to XML in specific format"""

    def open_spider(self, spider):
        self.file = open('data.xml', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self._export(self._exporter, item)
        return item

    @property
    def _exporter(self):
        exporter = XmlPageItemExporter(self.file)
        return exporter

    def _export(self, exporter, item):
        exporter.start_exporting()
        exporter.export_item(item)
        exporter.finish_exporting()
