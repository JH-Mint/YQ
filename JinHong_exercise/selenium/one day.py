import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver.get("http://tech-web.leadinsight.cn/yueqingsys/login")  #启动Chrome打开乐清SaaS后台
# time.sleep(3)
# driver.find_element(By.class_name,"ivu-input ivu-input-default").send_keys("admin")
# driver.find_element(By.class_name,"ivu-input ivu-input-default").send_keys("Admin123")
# time.sleep(5)

# def get_size(driver):
driver.get("http://www.baidu.com")
time.sleep(3)
driver.find_elements(By.id,"kw").send_keys("selenium")
time.sleep(5)
driver.quit()