import requests
import unittest
url1 = "http://47.98.96.184:8080/"
q=requests.get(url1)
# print(q.text)
# print(type(q.headers))
# 获取token
value =q.headers.get('XSRF-TOKEN')
header = {}
header['X-XSRF-TOKEN'] = value
# print(header)
# 登录
url2 = "http://47.98.96.184:8080/auth/fast-login"
data = {"appVersion": u"测试线下2.3.1(build231)",
        "channel": "gw",
        "defaultReg": "Y",
        "mobile": "11111111111",
        "phoneModels": "vivo vivoX20A",
        "systemName": "android",
        "systemVersion": "27",
        "type": "SYS",
        "validateCode": "999999"}
w=requests.post(url=url2, headers=header, json=data)
# print(w.text)
# 获取cookie
cookie = requests.cookies.RequestsCookieJar()
cookie.set('access_token', w.headers.get('access_token'))
cookie.set('refresh_token', w.headers.get('refresh_token'))
# print(type(cookie))

# 送背包礼物
# data1={"actorId":"10401","giftId":"13","giftNumber":"1","giftSource":1,"roomId":"10401","userId":"10133"}
# url1="http://47.98.96.184:8080/liveshowcenter/api/sendBackPackGift"
# y=requests.post(url=url1,json=data1,cookies=cookie)
# print(y.text)

# 主播每日任务查询
# url_3="http://47.98.96.184:8080/liveshowcenter/api/actor-daily-task-one-key-pass-cost"
# pydata={"actorId":"10133"}
# r=requests.get(url=url_3,params=pydata,headers=header,cookies=cookie)
# print(r.text)

# 主播每日任务进度
# pydata_2={"actorId":"10133"}
# url_7="http://47.98.96.184:8080/liveshowcenter/api/actor-daily-task-progress"
# u=requests.get(url=url_7,headers=header,cookies=cookie,params=pydata_2)
# print(u.text)

# 一键闯关
# pydata_1={"actorId":"10133","level":"30"}
# url_4="http://47.98.96.184:8080/liveshowcenter/api/actor-daily-task-one-key-pass"
# t=requests.post(url=url_4,headers=header,cookies=cookie,json=pydata_1)
# print(t.text)
# 获取幸运礼物补偿用户
# url_5="http://47.98.96.184:8080/liveshowcenter/api/get-subsidy-users"
# y=requests.get(url=url_5,headers=header,cookies=cookie)
# print(y.text)
# 活动中心列表
# url_6="http://47.98.96.184:8080/liveshowcenter/api/activity-center-config/get-config-list"
# u=requests.get(url=url_6,headers=header,cookies=cookie)
# print(u.text)

class JingDu(unittest.TestCase):
    def test_zhubo(self):
        url_7 = "http://47.98.96.184:8080/liveshowcenter/api/actor-daily-task-progress"
        pydata_2 = {"actorId": "10133"}
        u = requests.get(url=url_7, headers=header, cookies=cookie, params=pydata_2)
        print(u.text)  # 获取返回的结果
        result = u.json()['code']  # 获取状态码
        print(result)
        # 断言
        self.assertEqual(0, result)
        self.assertIn('msg', u.text)
        self.assertTrue('成功' in u.text)

if __name__ == "__main__":
     unittest.main()