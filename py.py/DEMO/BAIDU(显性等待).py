# coding = utf-8
import unittest
from time import sleep

import unittestreport
from unittestreport import TestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
class Test(unittest.TestCase):
    #测试用例test01，输入软件测试
    def test01(self):
        #打开浏览器
        driver = webdriver.Chrome()
        #加载百度页面
        driver.get("https://www.baidu.com/?tn=27082910_8_hao_pg")
        #在百度搜索栏中输入软件测试

        driver.find_element_by_id("kw").send_keys("软件测试")
        #点击百度一下按钮
        # click = WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.ID, "su")))
        click = WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, "su")))
        click.click()
    #测试用例test02，输入硬件测试
    def test02(self):
        #打开浏览器
        driver = webdriver.Chrome()
        #加载百度页面
        driver.get("https://www.baidu.com/?tn=27082910_8_hao_pg")
        #在百度搜索栏中输入软件测试
        driver.find_element_by_id("kw").send_keys("硬件测试")
        #点击百度一下按钮
        driver.find_element_by_id("su").click()

if __name__ == "__main__":
    t = Test()
    t.test01()
    # t.test02()