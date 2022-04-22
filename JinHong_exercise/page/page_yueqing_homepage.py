from base.base_yueqing_report import *

class HomePage(BasePage):
    consult = "//*[@id='app']/section/section/main/ul/li[1]/p"
    myplan = "//*[@id='app']/section/section/main/ul/li[2]/p"
    def homePage_consult(self):
        ele = self.find_element(HomePage.consult)
        return ele
    def homePage_myplan(self):
        ele = self.find_element(HomePage.myplan)
        return ele
    def search01(self):
        self.homePage_consult().click()
    def search02(self):
        self.homePage_myplan().click()