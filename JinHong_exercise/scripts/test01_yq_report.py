import unittest

from page.page_yueqing_report import *
class YueQing (unittest.TestCase):
    number = "18246117779"
    def test01(self):
        Element().search(YueQing.number)

if __name__ == "__main__":
    unittest.main()