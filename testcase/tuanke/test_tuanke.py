from testcase.tuanke.mainpage_tuanke import Mainpage_tuanke



class Test_tuanke():
    def test_tuanke(self):
        a=Mainpage_tuanke()
        a.openandlogin()
        a.paike()

Test_tuanke().test_tuanke()

