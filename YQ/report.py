#报告书进行填写
import os
import time
from YQ.login_consult import *
from YQ.message import *
# 判断进行报告书填报页面
class Report(Login_Consult):
    def Report_z(self):
        try:
            assert u"报告书" in Login_Consult.webpage.title
            print("报告书进行填报")
        except Exception as e:
            print("Exception found", format(e))
        # 点击项目类型
        Login_Consult.webpage.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div/form/div[1]/div[1]/div/div/div/div[1]/input").click()
        # time.sleep(1)
        # 选择项目类型
        Login_Consult.webpage.find_element_by_xpath( Report_data.xpath0 ).click()
        print("项目类型选择完成")
        # time.sleep(1)
        # 点击编制单位
        Login_Consult.webpage.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[1]/div[2]/div[1]/div/div/div[1]/input").click()
        # time.sleep(1)
        # 选择编制单位
        Login_Consult.webpage.find_element_by_xpath( Report_data.organization_unit ).click()
        print("编制单位选择完成")
        # time.sleep(1)
        # 报告书（送审稿）申请审批报告及相关材料
        #点击上传
        Login_Consult.webpage.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[2]/div/div/div/div/div[1]/button/span").click()
        time.sleep(2)
        #上传报告书  更换报告书需要更换Report_file中的文件
        os.system( Report_data.Report_file )
        print("报告书上传成功")
        time.sleep(3)
        #项目区域shp文件
        # 点击上传
        Login_Consult.webpage.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[3]/div/div/div/div/div[1]/button/span").click()
        time.sleep(2)
        # 上传Shp  更换报告书需要更换Report_Shp中的文件
        os.system( Report_data.Report_Shp )
        print("shp文件上传成功")
        time.sleep(3)
        #计划开始时间
        start = Login_Consult.webpage.find_element_by_xpath( "//*[@id='app']/section/section/main/div/div[2]/div/div/ul[2]/li[3]/span[2]/div/input" )
        start.clear()
        start.send_keys( Report_data.plan_start )
        # time.sleep(1)
        #计划结束时间
        end = Login_Consult.webpage.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div/div/ul[2]/li[4]/span[2]/div/input")
        end.clear()
        end.send_keys( Report_data.plan_end )
        # time.sleep(1)
        # 填报日期
        fill = Login_Consult.webpage.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div/div/ul[2]/li[8]/span[2]/div/input")
        fill.clear()
        fill.send_keys(Report_data.fill_date )
        # time.sleep(1)
        #点击提交
        Login_Consult.webpage.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div/div[3]/button[2]/span").click()
        # time.sleep(120)
        # 判断是否进入我的方案
        try:
            assert u"我的方案" in Login_Consult.webpage.title
            print("进入我的方案")
        except Exception as e:
            print("Exception found", format(e))
        print("报告书填报提交成功")
        # time.sleep(2)

        # 点击查看
        Login_Consult.webpage.find_element_by_xpath("//*[@id='pane-sh']/div/div[1]/div[3]/table/tbody/tr/td[8]/div/button/span").click()
        # time.sleep(3)
        try:
            assert u"方案报批" in Login_Consult.webpage.title
            print("开始方案报批")
        except Exception as e:
            print("Exception found(进入方案报批失败，请在我的方案进行查看)", format(e))
        # time.sleep(1)
        # 点击提交报批稿
        Login_Consult.webpage.find_element_by_xpath(
            "//*[@id='pane-sh']/div/div[3]/div/div[2]/div/div[2]/button[2]/span").click()
        # time.sleep(3)
        #方案报批填写
        print("方案报批填写")
        # 上传报批申请报告
        #点击上传
        Login_Consult.webpage.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[2]/div[1]/div/div/div/div/div[1]/button").click()
        time.sleep(2)
        #上传 申请报告pdf
        os.system( Report_data.Report_apply )
        print("报批申请报告文件上传成功")
        time.sleep(2)
        #点击上传：
        Login_Consult.webpage.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[2]/div[2]/div/div/div/div[1]/button/span").click()
        #上传报告书
        os.system( Report_data.Report_file )
        print("报告书报批文件上传成功")
        time.sleep(2)
        # 点击上传
        Login_Consult.webpage.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[3]/div/div/div/div/div[1]/button/span").click()
        # 上传Shp  更换报告书需要更换Report_Shp中的文件
        os.system( Report_data.Report_Shp )
        print("shp文件上传成功")
        time.sleep(2)
        #方案批复-提交
        Login_Consult.webpage.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div/div/div[3]/button[2]/span").click()
        # time.sleep(120)
        try:
            assert Login_Consult.webpage.find_element_by_class_name("status")
            print("批复中,请到SaaS后台进行审核")
        except Exception as e:
            print("Exception foung", format(e))
if __name__ == "__main__":
    r = Report()
    y = r.Report_z()