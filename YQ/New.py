import requests
from YQ.creat_object import *

class S(Url):
    def Save(self):
        url = "http://47.110.61.112:8053/project/v2/save"
        baby = {"name": "321",
                "id": "2",
                "belongAddress": "乐清市",
                "assignCodeOrg": "乐清市经济和信息化局",
                "typeTwo": "基本建设",
                "typeOne": "核准",
                "assignCodeTime": "2022-04-07 00:00:00",
                "backupTime": "2022-04-06 00:00:00",
                "backupType": "31",
                "registMoney": "31",
                "buildDetailAddress": "31",
                "buildAddress": "321",
                "buildType": "扩建",
                "startTime": "2022-4",
                "endTime": "2022-4",
                "isZeroLand": 0,
                "cbdType": "13",
                "buildDesc": "21",
                "totalInvest": "31",
                "fixedAssets": "",
                "constructionCost": "31",
                "equipmentCost": "",
                "installCost": "",
                "buildOtherCost": "",
                "backupCost": "",
                "buildInterest": "",
                "flowCost": "",
                "moneySource": "",
                "privateMoney": "",
                "fiscalMoney": "",
                "blankLoans": "",
                "otherMoney": "",
                "isComplement": 0,
                "landUnique": "",
                "isZeroUsePublic": "",
                "useLandArea": "13",
                "containNewland": "",
                "addBuildLand": "",
                "totalBuildArea": "213",
                "addBuildArea": "",
                "landUpArea": "",
                "buildOrgName": "321",
                "buidOrgUnique": "3213",
                "buildOrgLeader": "21",
                "buildOrgPhone": "31",
                "buildOrgContants": "",
                "buildOrgContantsPhone": "",
                "packages": "1",
                "standardLand": 0,
                "commitmentSys": "是",
                "needPermit": "是"}
        heades = {"Authorization":super().Login()}
        creat = requests.post(url=url, json=baby, headers=heades)
        print(creat.text)
        return creat


if __name__ == "__main__":
        s = S()
        s.Save()