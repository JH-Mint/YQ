"""
登录接口   http://mkgameht.yztest.top/api/login
    账号：admin
    密码：666666
参数：
    Headers:application/josn
    Boby: login admin
          pwd   666666
编写用例：
    1.账号密码，全部正确
    2.账号为空，密码正确
    3.账号正确，密码为空
    4.账号错误，密码错误
    5.账号正确，密码错误
    6.账号错误，密码正确
导入所需要的模块
    requests
    pytest
"""
import requests
import pytest
class Exerciselogin:
    def test_001_login(self):
        url = "http://mkgameht.yztest.top/api/login"
        data = "headers : application/josn"
        Boby = ["login : admin", "pwd : 666666"]
        y =requests.post(url = url, data=data, json=Boby)
        print(y.text)
if __name__ == "__main__":
    pytest.main()