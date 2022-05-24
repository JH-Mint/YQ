#-*- coding:utf-8 -*-
#手机用户18246117876登录
#先导入requests
import time
import requests
from honggetest.moka_app_api.phone_smsId import *
from honggetest.moka_app_api.select_Navicat import *

    # 手机登陆接口
def login():
    url1 = "https://cat.yztest.top/api/app/auth-mobile"
    #验证码smsID
    p = smsId()
    # print(p)
    #手机验证码
    m = selectmysql()
    #添加对应参数
    data = {
        "mobile" : "18246117876",
        "code" : str(m),
        "smsId" : str(p)  #用赋值后的a作为参数
    }
    #执行
    d = requests.post(url=url1, json=data ) #以json格式传参
    print(d.text)
login()

# from honggetest.moka_app_api.parameters import *
# class login:
#     def user_login(self):
#         # 发送验证码到手机获取smsid
#         p = ps.phone_smsId_data(ps)
#         #查询验证码
#         m = ps.select_Navicat_data(ps)
#         k = ps.login_data(p , m)
#         print(k.text)
#         return k
# user = login
# user.user_login(login)