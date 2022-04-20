import time

from selenium import webdriver
Ob = webdriver.Chrome(r'chromedriver')
class New_object():
    def New(self):
        # 进入Saas后台
        Ob.get("http://test-tech-web.leadinsight.cn/yueqingsys/project/projectManage")
        Ob.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[1]/div/div[1]/div[2]/input").send_keys("admin")
        print("输入账号admin")
        Ob.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[2]/div/div[1]/div[2]/input").send_keys("Admin123")
        print("已输入密码！")
        time.sleep(1)
        #登录
        Ob.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/div[3]/div/button/span").click()
        try:
            assert u"极简审批综合管理平台 - 首页" in Ob.title
            print("登录成功")
        except Exception as e:
            print("登录失败", format(e))
        time.sleep(3)
        Ob.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/i[2]").click()
        time.sleep(1)
        Ob.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/div/ul/li[1]/ul/li/span").click()
        time.sleep(2)
        Ob.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div/div[1]/div/div/button[1]/span").click()
