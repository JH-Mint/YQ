import pymysql
def selectmysql():
    conn = pymysql.connect(user="root", password="C7uuGNqu0S65jg0doQ6PNqu", host="47.98.96.184", database="moka",
                           port=6033)
    '''
    游标的使用
    '''
    cursor_1 = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 获取游标
    cursor_1.execute("SELECT * FROM `uaa`.`jhi_user` ORDER BY `created_date` DESC LIMIT 0, 1")  # 执行语句
    m = cursor_1.fetchone()
    p = m["id"]
    print(p)
    return p
    cursor_2 = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 获取游标
    cursor_2.execute("INSERT INTO 'menmber_center'.'member' (id,v_flag,actor_grade,actor_level,auth_access,big_image_original,charge_coin_balance,consume_coins,experience,gender,header_image_original,im_id,im_token,live_status,member_flag,nick_name,receive_coin_balance,receive_lucky_gift_coins,registe_app,register_time,send_lucky_gift_coins,sign,total_charge_coins,total_receive_coins,total_watch_time,user_level,utype,version,w_level,watch_time_in_week,update_time) values (30200299,0,0,C,N,0,40000,40000,M,http://appstatic.cctv69.top/icon/avatar11.png,test1779457701455666,5d2b1a3d577f76fca02012a801fda2cb,0,0,15548520479,0,0,10002	2020-08-10,17:22:13,0,0,0,0,11,NORMAL_MEMBER,2,0,0,2020-11-25,17:35:51)")

selectmysql()