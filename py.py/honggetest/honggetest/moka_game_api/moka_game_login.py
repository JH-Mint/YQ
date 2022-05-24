import requests
from honggetest.moka_game_api.moka_game_token import *
Authoriztion = token.token_token(token)
class login():
    def login_login(self):
        data = {"nick" : "老子"}
        header = {"Authoriztion" :token.token_token(token)}
        r = requests.post(url = "https://cat.yztest.top/api/games/cat/home/login",  data= data, headers= header )
        print(r.text)
        return r
login = login
login.login_login(login)