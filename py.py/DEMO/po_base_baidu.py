# 百度 基础层
from selenium import webdriver

class BasePage:
    #构造方法
    def __init__(self):
        #打开浏览器
        self.open = webdriver.Chrome()
        # 加载百度页面
        self.open.get("https://www.baidu.com/?tn=27082910_8_hao_pg")

    # 封装定位元素
    def find_mele(self, args):
        ele = self.open.find_element_by_id(args)
        return ele