#coding=utf-8
from testcase.daoshiguanli import mainpage_daoshiguanli
import unittest

class Test_Daoshiguanli(unittest.TestCase):
    def test_daoshiguanli(self):
        a= mainpage_daoshiguanli.Mainpage()
        a.openandlogin()
        a.xinzengdaoshi()
        a.xiugaidaoshi()
        a.shanchudaoshi()


if __name__=="__main__":
    Test_Daoshiguanli().test_daoshiguanli()