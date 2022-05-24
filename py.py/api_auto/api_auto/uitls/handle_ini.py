#coding=utf-8


from configparser import ConfigParser
from api_auto.api_auto.uitls.handle_path import *

class Handle_conf(ConfigParser):
    """
    当前类用来处理conf，ini文件的工具类
    """
    def __init__(self,filename):
        super(Handle_conf, self).__init__()  #继承父类
        self.filename = filename
        self.read(self.filename)


    def get_value(self,section,option):
        """
        获取ini文件中某个section下的某个option的value值
        :return:
        """
        value = self.get(section,option)
        print(value)
        return value



if __name__ == '__main__':
    filename = os.path.join(conf_path,"conf.ini")
    f = Handle_conf(filename)
    f.get_value("env","url")

