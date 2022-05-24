#登记表进行填写(待补充)
from YQ.login_consult import *
# 继承父类Login_Consult
#子类不能继承父类的私有方法和属性
class registry_form(Login_Consult):
    try:
        assert u"登记表填报" in Login_Consult.webpage.title
        print("正在进行登记表填报")
    except Exception as e:
        print("Exception found", format(e))
    #咨询填报页面，定位元素
    def Zixun(self):
        Login_Consult.webpage.find_element_by_xpath("/html/body/div/section/section/main/ul/li[1]/p").click()
        time.sleep(10)
Consult = registry_form()
Consult.Zixun()

