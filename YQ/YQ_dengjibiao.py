import time
import os
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
driver.find_element_by_class_name("el-input__inner").send_keys("13853360523")
time.sleep(1)
#登录
# login = driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
login = driver.find_element_by_class_name("el-button--primary").click()
time.sleep(2)
#咨询填报
driver.find_element_by_xpath("/html/body/div/section/section/main/ul/li[1]/p").click()

time.sleep(1)
#咨询填报内容输入
#项目名称
driver.find_element_by_class_name("el-input__inner").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div/section/section/main/div/div[2]/div/form/div[1]/div/div/div[2]/div[1]/div[1]/ul/li/span").click()
time.sleep(1)
#征占地面积
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/form/div[3]/div/div/input").send_keys("5000")
time.sleep(1)
# 挖填土方
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/form/div[4]/div/div[1]/input").send_keys("3000")
time.sleep(1)
# 咨询
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/form/div[7]/div/button[2]").click()
time.sleep(1)
#立即申报
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div/button").click()
time.sleep(1)
#勾选等5秒
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[2]/div/p[8]/label/span[1]/span").click()
time.sleep(6)
# 等5秒，下一步
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[7]/button[2]").click()
time.sleep(2)
#开挖
kaiwa = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[3]/form/div[1]/div/div/input")
kaiwa.clear()
kaiwa.send_keys("1500")
time.sleep(1)
#填筑
tianzhu = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[3]/form/div[2]/div/div/input")
tianzhu.clear()
tianzhu.send_keys("1500")
time.sleep(1)
#取土取石来源
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[3]/form/div[7]/div/div/div[1]/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[3]/form/div[7]/div/div/div[2]/div[1]/div[1]/ul/li[2]/span").click()
#弃土弃渣去向
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[3]/form/div[8]/div/div/div[1]/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[3]/form/div[8]/div/div/div[2]/div[1]/div[1]/ul/li[2]").click()
time.sleep(1)
#下一步
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[7]/button[2]/span").click()
time.sleep(1)
#选择开挖、填筑边坡挡土墙防护
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[4]/form/div[2]/label[1]/span[1]/span").click()
time.sleep(1)
#其他事项说明
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[4]/form/div[11]/div/div[1]/textarea").send_keys("测试添加")
time.sleep(1)
#下一步
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[7]/button[2]/span").click()
time.sleep(2)
#上传项目平面布置图
file = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[5]/div/form/div[1]/div/div/div[1]/button/span").click()

time.sleep(3)
#利用autoit工具进行windows弹窗元素定位并上传对应文件
os.system(r'D:\autoit-v3-setup\test.exe')
time.sleep(2)
# 勾选建设单位确认并承诺
driver.find_element_by_xpath("/html/body/div/section/section/main/div/div[2]/div/div[5]/div/form/label/span[1]/span").click()
time.sleep(1)
# 下一步
driver.find_element_by_xpath("/html/body/div/section/section/main/div/div[2]/div/div[7]/button[2]/span").click()
time.sleep(2)
# 选择日期
add_data = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[6]/ul[2]/li[8]/span[2]/div/input").send_keys("2022-03-30")
# add_data.clear()
# add_data.send_keys("2022-03-30")
time.sleep(2)
#下一步-提交
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div[7]/button[2]").click()
time.sleep(10)
#报批 --查看
driver.find_element_by_xpath("/html/body/div/section/section/main/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[3]/table/tbody/tr/td[7]/div/button/span").click()
time.sleep(2)
#下载批复文件
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div/div[2]/button/span").click()
time.sleep(2)
#一键下载
driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div/div[2]/div[2]/div/div[4]/div/div[2]/div/div/div[2]/button").click()





time.sleep(15)
driver.quit()
