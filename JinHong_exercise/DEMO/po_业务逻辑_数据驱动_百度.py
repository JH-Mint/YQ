import time
import unittest

from ddt import ddt, data
from DEMO.po_po_baidu import *

class BaiduTest(unittest.TestCase):
    text01 = "软件测试"
    text02 = "硬件测试"
    # @data("软件测试","硬件测试")
    def test_01(self):
        BaiduPage().search(BaiduTest.text01)
    def test_02(self):
        BaiduPage().search(BaiduTest.text02)

    time.sleep(5)
if __name__ == '__main__':
    unittest.main()
