import requests
heard = {"Accept-Encoding": "gzip",
         "X-XSRF-TOKEN": "53c1edb9-8bcd-4605-82c5-cd747ff9a182"}

data = {"appVersion": u"测试线下2.3.1(build231)",
        "channel": "gw",
        "defaultReg": "Y",
        "mobile": "",
        "phoneModels": "vivo vivoX20A",
        "systemName": "android",
        "systemVersion": "27",
        "type": "SYS",
        "validateCode": "999999"}


cookie = requests.cookies.RequestsCookieJar()
cookie.set('access_token', access_token)
cookie.set('refresh_token', refresh_token)
url1 = "http://47.98.96.184:8080/"
url2 = "http://47.98.96.184:8080/auth/fast-login"
url_3 = "http://47.98.96.184:8080/liveshowcenter/api/actor-daily-task-one-key-pass-cost"
pydata = {"actorId": "10133"}

r=requests.get(url=url_3,params=pydata,headers=heard,cookies=cookie)
print(r.text)
result = r.json()['code']  # 获取状态码
        # print(result)
        # # 断言
        # self.assertEqual(0, result)
        # self.assertIn('msg', r.text)
        # self.assertTrue('成功' in r.text)
