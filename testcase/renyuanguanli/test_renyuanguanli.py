from testcase.renyuanguanli.mainpage_renyuanguanli import Mainpage_renyuanguanli


class Test_renyuanguanli():
    def test_renyuanguanli(self):
        a=Mainpage_renyuanguanli()
        a.openandlogin()
        a.xiugairenyuan()

Test_renyuanguanli().test_renyuanguanli()