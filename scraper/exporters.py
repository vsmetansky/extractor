from scrapy.exporters import XmlItemExporter
from xml.sax.saxutils import XMLGenerator


class XmlPageItemExporter(XmlItemExporter):
    def __init__(self, file, **kwargs):
        self.item_element = 'page'
        self.root_element = 'data'
        self._configure(kwargs)
        if not self.encoding:
            self.encoding = 'utf-8'
        self.xg = XMLGenerator(file, encoding=self.encoding)

    def export_item(self, item):
        self._beautify_indent(depth=1)
        self.xg.startElement(self.item_element, {'url': item.get('url')})
        self._beautify_newline()
        self._export_xml_field('fragments', item.get('fragments'), depth=2)
        self._beautify_indent(depth=1)
        self.xg.endElement(self.item_element)
        self._beautify_newline(new_item=True)

    def _export_xml_field(self, name, serialized_value, depth):
        self._beautify_indent(depth=depth)
        if self.__list_like(serialized_value):
            self._beautify_newline()
            for value in serialized_value:
                self._export_xml_field('fragment', value, depth=depth+1)
            self._beautify_indent(depth=depth)
        else:
            self.xg.startElement(name, {'type': serialized_value.get('type')})
            self._xg_characters(str(serialized_value.get('data')))
            self.xg.endElement(name)
        self._beautify_newline()

    def __list_like(self, value):
        return isinstance(value, tuple) or isinstance(value, list)
