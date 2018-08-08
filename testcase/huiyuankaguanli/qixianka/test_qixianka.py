from testcase.huiyuankaguanli.qixianka import mainpage_qixianka


class Test_qixianka():
    def test_qixianka(self):
        a=mainpage_qixianka.Mainpage_qixianka()
        a.openandlogin()
        a.xinzengqixianka()
        a.xiugaiqixianka()

Test_qixianka().test_qixianka()

