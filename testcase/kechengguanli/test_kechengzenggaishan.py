#coding=utf-8
from testcase.kechengguanli import mainpage_kechengguanli
import unittest

class Kechengzenggaishan(unittest.TestCase):
    def test_kechengzenggaishan(self):
        a= mainpage_kechengguanli.Mainpage()
        a.openandlogin()
        a.xinzengkecheng()
        a.xiugaikecheng()
        a.shanchukecheng()

if __name__=="__main__":
    Kechengzenggaishan().test_kechengzenggaishan()


