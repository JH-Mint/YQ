'''
需要获得宠酱小程序的token，
参数要有宠酱的id
'''
import requests
class token():#封装
    def token_token(self):#函数
        # 请求接口，以及传参，注：params！！！不是data或者json
        gain = requests.get(url = "https://cat.yztest.top/api/token",  params = {"id":"120112"})
        # print(gain.text)#打印
        token_value = gain.json()["data"]#取返回值data下的从8个字符开始后的数据
        print(token_value)#打印token_value
        return token_value #返回token_value值
        # print(token_value)
token = token#给封装的token赋值为token
token.token_token(token)#调用
