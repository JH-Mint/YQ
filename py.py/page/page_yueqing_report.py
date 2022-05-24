from base.base_yueqing_report import *

class Element(BasePage):

    # 登录页面,手机号输入定位
    login_input = "//*[@id='app']/div/div[2]/form/div/input"
    # 登录按钮元素定位
    login_login = "//*[@id='app']/div/div[2]/form/button"

    # 首页元素
    def login01(self):
        ele = self.find_element(Element.login_input)
        return ele
    def login02(self):
        ele = self.find_element(Element.login_login)
        return ele
    def search01(self, text):
        self.login01().send_keys(text)
    def search02(self):
        self.login02().click()