"""
获取手机验证码接口
"""
#调手机登录-发生验证码接口取smsId
import requests
import time
time.sleep(60)
def smsId():
    url2 = "https://cat.yztest.top/api/app/auth-mobile-sms"
            #参数
    data = {
                "mobile" : "18246117876"
            }
    #执行
    y = requests.post(url=url2, data=data)
    #取url2返回结果中data字段下的smsId并赋值
    a = y.json()["data"]["smsId"]
    # print(a)
    return a
# smsId()