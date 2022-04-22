
from selenium import webdriver
import time

from YQ.message import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#登录、咨询
class Login_Consult(object):
        webpage = webdriver.Chrome(r'chromedriver')
        webpage.implicitly_wait(120)
        # 用get打开乐清pc页面
        webpage.get( url )
        # 窗口最大化
        webpage.maximize_window()
        # 输入建设单位登录账号  id = # class = .
        # driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("13565656565")
        webpage.find_element_by_class_name("el-input__inner").send_keys( phone )
        # time.sleep(1)
        # 登录
        webpage.find_element_by_class_name("el-button--primary").click()
        # time.sleep(2)
        #登录断言
        try:
            assert u"首页" in webpage.title
            print("用户登录成功")
        except Exception as e:
            print("Exception found", format(e))
        # 咨询填报
        webpage.find_element_by_xpath("/html/body/div/section/section/main/ul/li[1]/p").click()
        # time.sleep(1)
        print("正在进行咨询填报")
        # 咨询填报内容输入
        # 项目名称
        webpage.find_element_by_class_name("el-input__inner").click()
        # time.sleep(1)
        webpage.find_element_by_xpath(
            "/html/body/div/section/section/main/div/div[2]/div/form/div[1]/div/div/div[2]/div[1]/div[1]/ul/li/span").click()
        # time.sleep(1)
        # 征占地面积
        webpage.find_element_by_xpath(
            "/html/body/div[1]/section/section/main/div/div[2]/div/form/div[3]/div/div/input").send_keys( area )
        # time.sleep(1)
        # 挖填土方
        webpage.find_element_by_xpath(
            "/html/body/div[1]/section/section/main/div/div[2]/div/form/div[4]/div/div[1]/input").send_keys( traditional_cure )
        # time.sleep(1)
        print("咨询填写完成")
        # 点击咨询
        webpage.find_element_by_xpath(
            "/html/body/div[1]/section/section/main/div/div[2]/div/form/div[7]/div/button[2]").click()
        # time.sleep(1)
        # 立即申报(总有出错)
        shenbao = WebDriverWait(webpage, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/section/section/main/div/div[2]/div/div/button")))
        shenbao.click()
        # webpage.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div/div/button").click()
        # time.sleep(3)
# # login = driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
# driver.find_element_by_class_name("el-button--primary").click()
# # time.sleep(2)