import unittest

from page.page_yueqing_homepage import *

class Page(unittest.TestCase):
    def test01(self):
        HomePage().search01()
    def test02(self):
        HomePage().search02()
if __name__ == "__main__":
    unittest.main()
