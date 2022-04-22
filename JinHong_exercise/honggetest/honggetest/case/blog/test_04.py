
# coding:utf-8
import unittest
import time
import requests
from data import com_data
from common.login import Login
header,cookie = Login.login(18856267441)

# 获取幸运礼物补偿用户
# url_5="http://47.98.96.184:8080/liveshowcenter/api/get-subsidy-users"
# y=requests.get(url=url_5,headers=header,cookies=cookie)
# print(y.text)
class JingDu(unittest.TestCase) :

    def test_zhubo(self):
        url_5="http://47.98.96.184:8080/liveshowcenter/api/get-subsidy-users"
        y=requests.get(url=url_5,headers=header,cookies=cookie)
        print(y.text)
        result = y.json()['code']  # 获取状态码
        # print(result)
        # 断言
        self.assertEqual(0, result)
        self.assertIn('msg', y.text)
        self.assertTrue('成功' in y.text)

if __name__ == "__main__":
    unittest.main()