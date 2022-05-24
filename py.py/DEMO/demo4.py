from selenium import webdriver
from demo3 import *
#
class Location(Baidu):

    def Write(self):
        super().Bai()
        webpage.find_element_by_xpath("//*[@id='kw']").send_keys("baidu")
        time.sleep(3)
        webpage.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input").click()
#         # 想再这个类中调用 类名为 Baidu下的Op函数，并向下继续执行
#         # self.Location.Op()
#         #
#         # .find_element_by_xpath("//*[@id='kw']").send_keys("baidu")        time.sleep(3)
#        # W.find_element_by_xpath("//*[@id='hotsearch-refresh-btn']/span").click()
#
#         # search=driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("baidu")
L = Location()
L.Write()
