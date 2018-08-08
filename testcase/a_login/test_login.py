import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(os.path.split(rootPath)[0])


from HTMLTestRunner import HTMLTestRunner
import time
from time import sleep
from appium import webdriver
from utils.excel import Excel
from utils.email import Email
from utils.log import logger
from utils.yaml_reader import YamlReader
from common.login_page import Login_Page
from utils.utils import Utils
import unittest

#https://github.com/maijhui/app.git

class Test_Login(unittest.TestCase):
    def __init__(self,methodName):
        super().__init__(methodName)
        excel_path = YamlReader(element="excel_path").yaml_reader()
        self.datas = Excel(excel_path=excel_path).excel_reader()
        self.log_path = YamlReader(element="log_path").yaml_reader()

    def test_login(self):
        # print("one")
        a = Login_Page()
        driver = a.driver

        for i in range(3):
            self.username = self.datas[i][0]
            self.password = self.datas[i][1]
            a.login(username=self.username,password=self.password)

            try:
                driver.implicitly_wait(3)
                element = driver.find_element_by_name("允许")
                assert (element.text == "允许"), "不通过"
                print("登录成功，"+"账号："+self.username+","+"密码："+self.password+","+self.datas[i][2])
                logger.info("登录成功，"+"账号："+self.username+","+"密码："+self.password+","+self.datas[i][2])
                Utils().authority(driver)
                a.logout()
                break
            except :
                print("登录失败，"+"账号："+self.username+","+"密码："+self.password+","+self.datas[i][2])
                logger.info("登录失败，"+"账号："+self.username+","+"密码："+self.password+","+self.datas[i][2])

#         # Email(files_path=self.log_path).send_email()
#         # print("登录完成，日志报告已经以邮件形式发送")
#
def suite():
     suiteTest=unittest.TestSuite()
     suiteTest.addTest(Test_Login("test_login"))
     return suiteTest


if __name__ == '__main__':

    runner=unittest.TextTestRunner()
    runner.run(suite())
#
#     # report = "C:\\Users\\Administrator\\PycharmProjects\\app_aideyujia\\report\\result.html"
#     # with open(report, 'wb') as report:
#     #     runner = HTMLTestRunner(report, verbosity=2, title='标题：测试app登录功能', description='描述：测试app登录功能')
#     #     # runner.run(Test_Login("test_login"))
#     #     runner.run(suite())
#
#
#     # runner=unittest.TextTestRunner(verbosity=2,descriptions=True)
#     # runner.run(Test_Login("test_login"))
#
#
# # unittest.main()
