from locust import HttpUser, task, between, HttpLocust,TaskSet
# from honggetest.moka_game_api.moka_game_token import *
#
# class QuickstartUser(HttpUser):
#
#     wait_time = between(5, 9)
#     @task
#     def getpretrainedmodel(self):
#         url = 'https://cat.yztest.top/api/games/cat/home/index/head'
#         header = {
#             'Authorization' : 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMjAxMTIiLCJleHAiOjE2MDcyMzQ0Mzd9.rqohq5s0NQ8lzckmqVSz7LsvPHh54d1ugYp9vO7I6C4QanqwJivO3c17wSpRLIcmBpnuUlhz1vzz0VaFZGpHag'
#         }
#         req = self.client.request(method='GET', url= url, headers= header)
#         if req.status_code == 200:
#             print('success')
#         else:
#             print('fails')
class UserBehavior(TaskSet):
    def on_start(self):
        loginurl = '/api/login'
        h = {
         'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
        }
        body ={
            "login" : 'admin',
            "pwd" : "666666"
        }
        r = self.client.post(loginurl, data=body, headers=h)
        print(r.text)

        @task(2)
        def cat_chengzhang(self):
            print('1')
            r = self.client.get('/api/boms-game/nest/cat-list')
            assert '猫咪成长'in r.text


        @task(1)
        def cat_lixian(self):
            print('2')
            r = self.client.get('/api/boms-game/nest/config')
            assert '离线收益' in r.text

# if __name__ == "__main__":
#     import os
#     os.system("locust -f locustfile.py --hocdst=http://mkgameht.yztest.top")


class websiteUser(HttpUser):
    host = 'http://mkgameht.yztest.top'
    tesk_set = UserBehavior
    min_wait = 1000
    max_wait = 1000
