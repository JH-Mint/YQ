"""
查询数据库中得验证码
pymysql 模块链接数据库
"""
import time
import pymysql
dt = {
"user" :'root',
"password" : 'C7uuGNqu0S65jg0doQ6PNqu',
"host" : '47.98.96.184',
"database":'moka',
"port":6033
}
# 链接数据库,用户名、端口、IP、密码、数据库名称
class sql():
    def selectmysql():
        conn = pymysql.connect(user = "root", password = "C7uuGNqu0S65jg0doQ6PNqu", host = "47.98.96.184", database = "moka", port = 6033)
        '''
        游标的使用
        '''
        cursor_1 = conn.cursor(cursor=pymysql.cursors.DictCursor)     #获取游标
        #moka数据库中mobile_verify表下mobile =18246117876 最新得一个biz_data（验证码）
        cursor_1.execute("SELECT biz_data FROM `moka`.`mobile_verify` WHERE `mobile` =18246117876 ORDER BY `created_time` DESC  LIMIT 1")#执行语句
        m = cursor_1.fetchone()["biz_data"]
        print(m)
        return m
    # print(m)#结果是元组,fetchone()获取查询结果
    selectmysql()
