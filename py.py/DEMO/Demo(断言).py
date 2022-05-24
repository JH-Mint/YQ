
import os
import time

from selenium import webdriver
from time import sleep
# import org.openqa.selenium.support.ui.Select;
from selenium.webdriver.common.by import By


# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome(r'chromedriver')
# 用get打开乐清pc页面
driver.get('http://test-tech-web.leadinsight.cn/yueqingpc/Login')
#窗口最大化
driver.maximize_window()
#输入建设单位  id = # class = .
# driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("13565656565")
# driver.find_element_by_class_name("el-input__inner").send_keys("13853360520")
# driver.find_element_by_class_name("el-input__inner").isDisplayed()
driver.find_element_by_class_name("el-input__inner").isSelected()
time.sleep(1)
#登录
# login = driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
login = driver.find_element_by_class_name("el-button--primary").click()
time.sleep(2)
# 判断该页面是否有 xpath这个定位的元素，有则提示登录成功，没有则使用Exception将异常的信息进行打印
try:
    assert u"首页" in driver.title
    print("登录成功")
except Exception as e:
    print("Exception found", format(e))

time.sleep(3)
driver.quit()