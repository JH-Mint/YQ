import pytest
import requests
from CangNanApp.conf.common import *
from CangNanApp.params.login_phone import *
class Login():
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def sms(self):
        url  = cangnan_host + "/app/login/sms/send"
        params = phone1
        sms = requests.get(url = url, params= params)
        print(sms.status_code)
    def Login_code(self):
        url = cangnan_host + "/app/login/code"
        data = phone2
        login = requests.post(url = url, data = data, headers=head2)
        print(login.status_code)
if __name__ == '__main__':
    p = Login()
    p.sms()
    p.Login_code()
