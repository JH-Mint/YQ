import pymysql.cursors

class Da:
    def selectmysql(self):
        conn = pymysql.connect(user="root", password="C7uuGNqu0S65jg0doQ6PNqu", host="47.98.96.184", database="moka",
                                   port=6033)
        '''
        游标的使用
        '''

        cursor_1 = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 获取游标
        # 查询创建时间最早的一条数据
        cursor_1.execute("SELECT * FROM `uaa`.`jhi_user` ORDER BY `created_date` DESC LIMIT 0, 1")  # 执行语句
        m = cursor_1.fetchone()
        # conn.commit()
        p = m["id"]
        print(p)
        # return
        cursor_2 = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #增加余额
        cursor_2.execute("UPDATE `member_center`.`member` SET `charge_coin_balance` = 500 WHERE `id` = '{}'".format(p))  # 执行语句
        cursor_2.fetchone()
        conn.commit()
        print(200)

y = Da()
print(y.selectmysql())

