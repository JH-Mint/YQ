import requests
class token():#封装
    def token_token(self):#函数
        # 请求接口，以及传参，注：params！！！不是data或者json
        herads = {
                     "Accept - Encoding: gzip, compress, br, deflate",
            "User - Agent: Mozilla / 5.0(Linux;Android6.0.1;OPPOR9sBuild / MMB29M;wv)",
            "Content - Length: 893",
            "content-type: application/json",
            "charset: utf-8",
            "Referer: https://servicewechat.com/wx640dca8fdeb31ea5/0/page-frame.html"

        }
        gain = requests.post(url = "https://cat.yztest.top/api/login",  params = {"id":"119484"}, herads = herads)
        print(gain.text)#打印
        # token_value = gain.json()["data"][8:]#取返回值data下的从8个字符开始后的数据
        # print(token_value)#打印token_value
        # return token_value #返回token_value值
        # print(token_value)
token = token#给封装的token赋值为token
token.token_token(token)#调用