# coding:utf-8
import unittest
import time
import requests
from honggetest.data import com_data
from honggetest.common.login import Login
header,cookie = Login.login(18856267441)

class JingDu(unittest.TestCase):
    def test_zhubo(self):
        url_3 = "http://47.98.96.184:8080/liveshowcenter/api/actor-daily-task-one-key-pass-cost"
        pydata = {"actorId": "10133"}
        r=requests.get(url=url_3,params=pydata,headers=header,cookies=cookie)
        print(r.text)
        result = r.json()['code']  # 获取状态码
        # print(result)
        # 断言
        self.assertEqual(0, result)
        self.assertIn('msg', r.text)
        self.assertTrue('成功' in r.text)




r = JingDu()
q = r.test_zhubo()

if __name__ == "__main__":
    unittest.main()