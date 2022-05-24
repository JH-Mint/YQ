#登录、咨询
from NewYQ.selenium_base import *
from NewYQ.YQ_page_element import *
from NewYQ.config import *
#乐清审批系统登录页面
class Login(BasePage):
    #输入账号位置定位
    input = "//*[@id='app']/div/div[2]/form/div/input"
    def Login_login(self):
        ele = self.find_mele(Login.input).send_keys(user1)
        return ele
if __name__ == "__main__":
    r = Login()
    r.Login_login()