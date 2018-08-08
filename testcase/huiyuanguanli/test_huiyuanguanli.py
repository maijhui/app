from testcase.huiyuanguanli.mainpage_huiyuanguanli import Mainpage_huiyuanguanli



class Test_huiyuanguanli():
    def test_huiyuanguanli(self):
        a=Mainpage_huiyuanguanli()
        a.openandlogin()
        # a.xiugaihuiyuan()
        # a.lahei()
        # a.kaika()
        # a.yanqihuiyuanka()
        # a.qingjiahuiyuanka()
        # a.chongzhihuiyuanka()
        # a.ticemuban()
        a.sousuohuiyuan()

Test_huiyuanguanli().test_huiyuanguanli()

