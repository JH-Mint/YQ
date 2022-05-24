import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://baidu.s.3jdh.com/?query="
    def test01(self):
        open = self.driver
        open.get(self.url)
        try:
            assert open.find_element_by_id("k0w")
            print("找到了")
        except NoSuchElementException as e:
            print("未找到该元素",e)
if __name__ =="__main__":
    unittest.main()