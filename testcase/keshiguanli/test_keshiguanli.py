from HTMLTestRunner import HTMLTestRunner

from testcase.keshiguanli.mainpage_keshiguanli import Mainpage_keshiguanli
import unittest
from utils.utils import Utils, Email


class Test_keshiguanli():
    def test_keshiguanli(self):
        a=Mainpage_keshiguanli()
        a.openandlogin()
        a.xinzengkeshi()
        # a.xiugaikeshi()

if __name__=="__main__":
    Test_keshiguanli().test_keshiguanli()
    # reportfilepath =  'C:\\Users\\Administrator\\PycharmProjects\\xianlianyueke\\xianliankuangjia\\report\\report.html'
    # e = Email(title='现联瑜伽后台列表打印',  # 实例化email邮件对象，传参
    #           message='各位同事，附件为今天的测试报告，请查收。',
    #           receiver='472847165@qq.com',
    #           server='smtp.qq.com',
    #           sender='1691614276@qq.com',
    #           password='vgktngsdhjmheiag',
    #           path=reportfilepath
    #           )
    # e.send()
