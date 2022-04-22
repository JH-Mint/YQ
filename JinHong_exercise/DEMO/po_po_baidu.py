# PO层：封装百度页面元素定位，元素对象以及页面操做
from DEMO.po_base_baidu import *

class BaiduPage(BasePage):
    # 元素定位
    # 输入框元素
    baidu_text_loc = "kw"
    # 百度一下按钮元素
    baidu_submit_loc = "su"
    # 得到对象元素
    # 得到输入框元素
    def get_text_obj(self):
        ele = self.find_mele(BaiduPage.baidu_text_loc)
        return ele
    # 得到百度一下按钮元素
    def get_submint_loc(self):
        ele = self.find_mele(BaiduPage.baidu_submit_loc)
        return ele
    # 页面操做
    def search(self, search_string):
        self.get_text_obj().send_keys(search_string)
        self.get_submint_loc().click()