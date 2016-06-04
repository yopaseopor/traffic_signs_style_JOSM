import unittest
from tinycss.css21 import CSS21Parser
import grequests
import os
from zipfile import ZipFile


class TestCSS(unittest.TestCase):
 
    def setUp(self):
        self.filename = 'Styles_Traffic_signs-style.mapcss'
        self.zipfile = 'Styles_Traffic_signs.zip'
 
    def test_css(self):
        f_mapcss = open(self.filename)
        css = f_mapcss.read()
        f_mapcss.close()
        stylesheet = CSS21Parser().parse_stylesheet(css)
        if stylesheet.errors:
           for error in stylesheet.errors:
               print error
        self.assertTrue(len(stylesheet.errors) == 0)

    def test_zip(self):
        z = ZipFile(self.zipfile, 'r')
        z.testzip()

    def test_images(self):
        f_mapcss = open(self.filename)
        css = f_mapcss.read()
        f_mapcss.close()
        stylesheet = CSS21Parser().parse_stylesheet(css)
        img_urls = []
        z = ZipFile(self.zipfile, 'r')
        for rule in stylesheet.rules:
            for declaration in rule.declarations:
                if declaration.name == 'icon-image':
                    if str(declaration.value[0].value).startswith('http://') or str(declaration.value[0].value).startswith('https://'):
                        img_urls.append(declaration.value[0].value)
                    else:
                        try:
                            t = z.read(declaration.value[0].value)
                        except Exception:
                            print 'error opening:{}'.format(declaration.value[0].value)
                        if len(t) == 0:
                            print 'file is empty:{}'.format(declaration.value[0].value)
                        self.assertTrue(len(t) != 0)
        rs = (grequests.get(u) for u in img_urls)
        responses = grequests.map(rs)
        for response in responses:
            if response.status_code != 200:
                print 'url not found:{}'.format(response.url)
            self.assertTrue(response.status_code == 200)
        self.assertTrue(len(responses) == len(img_urls))


if __name__ == '__main__':
    unittest.main()
