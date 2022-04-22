from selenium import webdriver


class BasePage():
    def __init__(self):
        self.open = webdriver.Chrome()
        self.open.get("http://test-tech-web.leadinsight.cn/yueqingpc/Login")
        # self.open.get("http://tech-web.leadinsight.cn/yueqingpc/Login")
        self.open.implicitly_wait(120)
    def find_element(self,args):
        ele = self.open.find_element_by_xpath(args)
        return ele