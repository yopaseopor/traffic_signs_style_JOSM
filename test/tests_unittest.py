import unittest
from tinycss.css21 import CSS21Parser
import requests
import os

class TestCSS(unittest.TestCase):
 
    def setUp(self):
        self.filename = 'Styles_Traffic_signs-style.mapcss'
 
    def test_css(self):
        f_mapcss = open(self.filename)
        css = f_mapcss.read()
        f_mapcss.close()
        stylesheet = CSS21Parser().parse_stylesheet(css)
        if stylesheet.errors:
           for error in stylesheet.errors:
               print error
        self.assertTrue(len(stylesheet.errors) == 0)

    def test_images(self):
        f_mapcss = open(self.filename)
        css = f_mapcss.read()
        f_mapcss.close()
        stylesheet = CSS21Parser().parse_stylesheet(css)
        print""
        for rule in stylesheet.rules:
            for declaration in rule.declarations:
                if declaration.name == 'icon-image':
                    if str(declaration.value[0].value).startswith('http://') or str(declaration.value[0].value).startswith('https://'):
                        resp = requests.get(declaration.value[0].value)
                        if resp.status_code != 200:
                            print 'problem geting image {} code {}'.format(declaration.value[0].value, resp.status_code)
                        self.assertTrue(resp.status_code == 200)
                    else:
                        self.assertTrue(os.path.isfile(declaration.value[0].value))


if __name__ == '__main__':
    unittest.main()
