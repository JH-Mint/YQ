# coding=utf-8
#1.先设置编码，utf-8可支持中英文，如上，一般放在第一行
#3.导入unittest模块
import unittest
#4.编写测试用例和断言
def all_case():
    # 待执行用例的目录
    case_dir = "C:\\Users\\Windows Hello\\PycharmProjects\\honggetest"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    testcase.addTests(discover)  # 直接加载 discover    可以兼容python2和3
    print(testcase)
    return testcase
if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    # run 所有用例
    runner.run(all_case())