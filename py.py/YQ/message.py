#登录极简审批系统
# url = "http://test-tech-web.leadinsight.cn/yueqingpc/Login"
url = "http://lingjian-web.leadinsight.cn/yueqingpc/Login"
phone = "17820225235"
# 征占地面积
area = 200000
# 挖填土方
traditional_cure = 200000
# 登记表内容

# 报告表内容

# 报告书文件目录：C:\Users\63212\Desktop\乐清\uplanding\报告书文件  注：文件名称必须要以当前文件名称相同(报告书shp文件.zip\方案报告书.pdf\报告书申请文件.pdf)
# 报告书内容
class Report_data():
    # 项目类型_房地产项目
    xpath0 = "//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/ul/li[1]/span"
    # # 项目类型_市政道路项目
    # xpath0 = "//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/ul/li[2]/span"
    # # 项目类型_工业厂房项目
    # xpath0 = "//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/ul/li[3]/span"
    # # 项目类型_其他
    # xpath0 = "//*[@id='app']/section/section/main/div/div[2]/div/div/form/div[1]/div[1]/div/div/div/div[2]/div[1]/div[1]/ul/li[4]/span"

    #选择编制单位
    organization_unit = "//span[text()='浙江广川工程咨询有限公司']"
    #上传报告书  更换报告书需要更换Report_file中的文件
    Report_file = r"C:\Users\63212\Desktop\乐清\uplanding\Report_file.exe"
    # 上传Shp  更换shp文件需要更换Report_Shp中的文件
    Report_Shp = r"C:\Users\63212\Desktop\乐清\uplanding\Report_Shp.exe"
    # 计划开始时间
    plan_start = "2020-03"
    # 计划结束时间
    plan_end = "2021-01"
    # 填报日期
    fill_date= "2022-04-01"
    # 上传报批申请报告
    Report_apply = r"C:\Users\63212\Desktop\乐清\uplanding\Report_Apply.exe"