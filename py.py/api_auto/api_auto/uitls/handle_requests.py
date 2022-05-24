#coding=utf-8

import requests

class Send_Requests(object):
    """
    封装一个发送接口请求的工具类
    """

    def __init__(self):
        self.session = requests.session()

    def send(self,method,url,data=None,json=None,params = None,headers= None):

        method = method.lower()
        if method == "get":
            response = self.session.get(url,params)

        elif method == "post":
            response = self.session.post(url,data,headers)

        elif method == "post_json":
            response = self.session.post(url,json,headers)

        elif method == "delete":
            response = self.session.delete(url)
        elif method == "put":
            response = self.session.post(url,data)

        return response





















































