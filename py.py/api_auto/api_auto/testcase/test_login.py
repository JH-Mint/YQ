#coding=utf-8

import unittest
from uitls.handle_excle import *    #导入读取excel表格的类
from uitls.handle_path import *     #导入所有路径
from uitls.handle_ini import *      #导入操作ini文件的类
from uitls.handle_requests import *

from ddt import ddt,data    #从ddt模块导入ddt和data装饰器

"""
ddt模块：用来做数据驱动的
作用：可以在excel表格中循环读取接口的用例数据，依次发送请求
装饰器的作用：在不改变原有函数的功能基础上给函数添加新的功能
ddt装饰器：用来装饰类
data装饰器：用来装饰用例（比如有10条用例，会从第一条依次按顺序跑到第10条）
"""


case_file = os.path.join(data_path,"apicase.xlsx")
path = os.path.join(conf_path,"conf.ini")
conf = Handle_conf(path)
@ddt
class Test_Login(unittest.TestCase):
    excel = Handle_Excel(case_file,"login")
    cases = excel.read_data()
    requests = Send_Requests()
    print(cases)    #打印的是一个列表，列表里面的4个字典

    def setUp(self):
        pass
    def tearDown(self):
        pass

    @data(*cases)       #cases是一个列表，里面有4个字典
    def test01_login(self,case):    #case是cases中的一个个字典，case变量名称可以自定义
        """
        此方法封装的是登录接口
        :return:
        """
        url = conf.get_value("env","url") + case["url"]
        #eval()函数用来执行一个字符串表达式，并返回表达式的值,只能对字符串进行操作
        data = eval(case["data"])
        excepted = eval(case["excepted"])
        headers = conf.get_value("env","headers")
        method = case["method"]
        case_id = case["case_id"]
        row_num = case_id + 1       #记录当前跑了几条用例

        #2、发送接口请求
        response = self.requests.send(method = method,url = url,data = data,headers = headers)
        result = response.json()

        #3、对接口的响应内容进行断言
        #尝试执行try里面的代码，如果出现异常（报错信息），则执行except中的代码并抛出异常
        # 如果没有出现异常，则执行else下面的代码
        try: #try是尝试去执行代码
            self.assertEquals(excepted["code"],result["code"])#专门用在unittest内进行断言比对
            self.assertEquals(excepted["msg"],result["msg"])  #断言期望结果中的msg和实际结果中的msg是否一致，如果执行失败则走到except

        except Exception as e:      #捕捉异常
            self.excel.write_excel(row_num,8,"未通过")
            print(e)
        else:
            self.excel.write_excel(row_num,8,"通过")


if __name__ == '__main__':
    unittest.main()









































