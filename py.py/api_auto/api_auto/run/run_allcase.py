#coding=utf-8

import unittest
import time
from api_auto.api_auto.lib.HTMLTestRunnerNew import HTMLTestRunner
from api_auto.api_auto.uitls.handle_path import *

now = time.strftime("%Y-%m-%d-%H-%M-%S")
filename = report_path + "\\"+ now + "api_report.html"

def auto_run():
    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,pattern="test*.py")
    f = open(filename,"wb")
    runner = HTMLTestRunner(
        stream=f,
        title="登录接口自动化测试报告",
        description="接口用例执行情况如下",
        tester="麦钊鹏"
    )
    runner.run(discover)
    f.close()
if __name__ == '__main__':
    auto_run()


















































