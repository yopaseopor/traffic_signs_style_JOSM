import unittest
from tinycss.css21 import CSS21Parser

class TestCSS(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_css(self):
        f_mapcss = open('Styles_Traffic_signs-style.mapcss')
        css = f_mapcss.read()
        f_mapcss.close()
        #css = ''
        stylesheet = CSS21Parser().parse_stylesheet(css)
        if stylesheet.errors:
           for error in stylesheet.errors:
               print error
        self.assertTrue(len(stylesheet.errors)==0)
        

if __name__ == '__main__':
    unittest.main()
