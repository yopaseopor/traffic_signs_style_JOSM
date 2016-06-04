import unittest
from tinycss.css21 import CSS21Parser
import requests


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
                    resp = requests.get(declaration.value[0].value)
                    if resp.status_code != 200:
                        print 'problem geting image {} code {}'.format(declaration.value[0].value, resp.status_code)
                        return False


if __name__ == '__main__':
    unittest.main()
