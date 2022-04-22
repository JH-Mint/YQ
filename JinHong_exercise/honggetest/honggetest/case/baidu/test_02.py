# coding:utf-8
import unittest
import time
import requests
from data import com_data
from common.login import Login
header,cookie = Login.login(18856267441)

# 送背包礼物

class JingDu(unittest.TestCase) :

    def test_zhubo(self):
        url1="http://47.98.96.184:8080/liveshowcenter/api/sendBackPackGift"
        data1={"actorId":"10401","giftId":"13","giftNumber":"1","giftSource":1,"roomId":"10401","userId":"10133"}
        y=requests.post(url=url1,json=data1,cookies=cookie)
        print(y.text)
        result = y.json()['code']  # 获取状态码
        # print(result)
        # 断言
        self.assertEqual(0, result)
        self.assertIn('msg', y.text)
        self.assertTrue('成功' in y.text)

if __name__ == "__main__":
    unittest.main()