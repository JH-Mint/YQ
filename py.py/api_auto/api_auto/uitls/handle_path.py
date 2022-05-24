#coding=utf-8

"""
此模块是用来组建项目各个包的路径
"""

import os


#定义项目的路径
base_path = os.path.dirname(os.path.dirname(__file__)) #获取当前目录所在的上级目录，当包移动路径时会自动更换，无需重新定义
print(base_path)
# print(os.path.dirname(__file__))  #获取当前文件所在的目录

#定义conf路径
conf_path = os.path.join(base_path,"conf")
print(conf_path)
#定义data路径
data_path = os.path.join(base_path,"data")
print(data_path)
#定义lib路径
lib_path = os.path.join(base_path,"lib")
print(lib_path)
#定义report路径
report_path = os.path.join(base_path,"report")
print(report_path)
#定义run路径
run_path = os.path.join(base_path,"run")
print(run_path)
#定义testcase路径
testcase_path = os.path.join(base_path,"testcase")
print(testcase_path)
#定义uitls路径
uitls_path = os.path.join(base_path,"uitls")
print(uitls_path)
"""
先创建一个存放所有包和文件路径的模块，导入os模块把所有路径定义在此模块，方便后面方法函数的调用。
"""

































































