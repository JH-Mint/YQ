#定位方法、点击方法、输入方法、等待方法、打开方法
from selenium import webdriver
from NewYQ.config import *
from selenium.webdriver.support.ui import WebDriverWait
# 打开浏览器
class BasePage():
    def __init__(self):
        self.open = webdriver.Chrome()
        #打开乐清审核系统登录页面
        self.open.get(yqurl)
    #
    #定位方法封装  xpath
    def find_mele(self, args):
        ele = self.open.find_element_by_xpath(args)
        return ele


