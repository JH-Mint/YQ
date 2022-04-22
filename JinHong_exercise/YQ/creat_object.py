import requests
class Url():
        def Login(self):
                url = "http://47.110.61.112:8053/access/account/login"
                baby = {"accountName":"admin","password":"5\u0010\u0019\u001d\u001aEFG","cbdType":1}
                login = requests.post(url = url, json = baby)
                Authorization = login.json()["result"]["authorization"]
                return Authorization
if __name__ == "__main__":
        a = Url()
        print(a.Login())