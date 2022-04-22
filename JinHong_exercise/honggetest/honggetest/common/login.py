import requests
import copy
from honggetest.data import com_data


class Login:
    header = com_data.heard
    data = com_data.data
    url1 = com_data.url1
    url2 = com_data.url2
    # print(data)

    def login(mobile):
        header = copy.deepcopy(com_data.heard)
        r1 = requests.get(com_data.url1)
        token = r1.headers.get('XSRF-TOKEN')
        header['X-XSRF-TOKEN'] = token
        print(token)

# """获取cookie"""
        data = copy.deepcopy(com_data.data)
        data['mobile'] = "18856267441"
        r2 = requests.post(url=com_data.url2, headers=header, json=data)
        cookie = requests.cookies.RequestsCookieJar()
        cookie.set('access_token', r2.headers.get('access_token'))
        cookie.set('refresh_token', r2.headers.get('refresh_token'))
        print(header) , print(cookie)

q=Login.login(18856267441)
print(q)
#Login.login(18856267441)

# q = Login()
# w = q.login(18856267441)




