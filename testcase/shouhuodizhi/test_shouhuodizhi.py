from common.login_page import Openandlogin
from testcase.shouhuodizhi.mainpage_shouhuodizhi import Mainpage_shouhuodizhi


class Test_shouhuodizhi():
    def test_shouhuodizhi(self):
        a=Mainpage_shouhuodizhi()
        a.openandlogin()
        # a.xinzengshouhuodizhi()
        # a.xiugaishouhuodizhi()
        a.shanchushouhuodizhi()

Test_shouhuodizhi().test_shouhuodizhi()

