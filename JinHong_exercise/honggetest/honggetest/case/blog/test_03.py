# coding:utf-8
import unittest
import time
import requests
from data import com_data
from common.login import Login
header,cookie = Login.login(18856267441)

# 一键闯关
class JingDu(unittest.TestCase) :

    def test_zhubo(self):
        url_4="http://47.98.96.184:8080/liveshowcenter/api/actor-daily-task-one-key-pass"
        pydata_1={"actorId":"10133","level":"30"}
        t=requests.post(url=url_4,headers=header,cookies=cookie,json=pydata_1)
        print(t.text)
        result = t.json()['code']  # 获取状态码
        # print(result)
        # 断言
        self.assertEqual(0, result)
        self.assertIn('msg', t.text)
        self.assertTrue('成功' in t.text)

if __name__ == "__main__":
    unittest.main()