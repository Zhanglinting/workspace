import xml.sax


class MoviesHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.tag = ''
        self.type = ''
        self.format = ''
        self.year = ''

    def startElement(self, tag, attributes):
        self.tag = tag
        if tag == 'movie':
            print('***movie***')
            title = attributes['title']
            print('title:', title)

    def endElement(self, tag):
        if self.tag == 'type':
            print('type:', self.type)
        elif self.tag == 'format':
            print('format:', self.format)
        elif self.tag == 'year':
            print('year:', self.year)
        self.tag = ''

    def characters(self, content):
        if self.tag == 'type':
            self.type = content
        elif self.tag == 'format':
            self.format = content
        elif self.tag == 'year':
            self.year = content


if __name__ == '__main__':
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    handler = MoviesHandler()
    parser.setContentHandler(handler)
    parser.parse('movies')