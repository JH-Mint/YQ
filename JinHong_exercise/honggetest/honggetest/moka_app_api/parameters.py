# _*_coding = uft-8_*_
import requests
import time
import pymysql
class ps:
    def login_data(p , m):#传入参数p，m
        # p = phone_smsId_data()
        # m = select_Navicat_data()
        url1 = "https://cat.yztest.top/api/app/auth-mobile"#调接口
        data = {
            "mobile": "18246117876",
            "code": str(m),
            "smsId": str(p)  # 用赋值后的p作为参数
        }
        d = requests.post(url=url1, json=data)  # 以json格式传参
        return d

    def phone_smsId_data(self):
        time.sleep(60)
        url2 = "https://cat.yztest.top/api/app/auth-mobile-sms"
        # 参数
        data = {
            "mobile": "18246117876"
        }
        # 执行
        y = requests.post(url=url2, data=data)
        # 取url2返回结果中data字段下的smsId并赋值
        a = y.json()["data"]["smsId"]
        # print(a)
        return a

    def select_Navicat_data(seif):
        conn = pymysql.connect(user="root", password="C7uuGNqu0S65jg0doQ6PNqu", host="47.98.96.184", database="moka",
                               port=6033)
        '''
        游标的使用
        '''
        cursor_1 = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 获取游标
        # moka数据库中mobile_verify表下mobile =18246117876 最新得一个biz_data（验证码）
        cursor_1.execute(
            "SELECT biz_data FROM `moka`.`mobile_verify` WHERE `mobile` =18246117876 ORDER BY `created_time` DESC  LIMIT 1")  # 执行语句
        m = cursor_1.fetchone()["biz_data"]
        print(m)
        return m
# s = ps
# s.select_Navicat_data(ps)
# s.phone_smsId_data(ps)
# s.login_data(ps)