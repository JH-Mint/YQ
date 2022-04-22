import requests
from honggetest.moka_game_api.moka_game_token import *
def getpretrainedmodel(self):
    url = 'https://cat.yztest.top/api/games/cat/home/index/head'
    header = {
        'Authorization' : 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMjAxMTIiLCJleHAiOjE2MDcyMzQ0Mzd9.rqohq5s0NQ8lzckmqVSz7LsvPHh54d1ugYp9vO7I6C4QanqwJivO3c17wSpRLIcmBpnuUlhz1vzz0VaFZGpHag'}
    # locust = requests.get(url = url, headers=header)
    self.client.request(method='GET', url=url, headers=header)