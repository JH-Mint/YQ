from selenium import webdriver
import time
from YQ.message import *
class login():
    def driver(self):
        driver = webdriver.Chrome(r'chromedriver')
        # 用get打开乐清pc页面
        driver.get(url)
        # 窗口最大化
        driver.maximize_window()
        # 输入建设单位登录账号  id = # class = .
        # driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("13565656565")
        driver.find_element_by_class_name("el-input__inner").send_keys(phone)
        time.sleep(1)
        # 登录
        driver.find_element_by_class_name("el-button--primary").click()
        time.sleep(2)
login = login()
login.driver()
# 进入咨询页面
class zixuntianbao(login):
    def zixun(self):
        zixun = webdriver.Chrome(r'chromedriver')
        zixun.find_element_by_xpath("/html/body/div/section/section/main/ul/li[1]/p").click()
zixun = zixuntianbao()
zixun.zixun()