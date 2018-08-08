from common.login_page import Openandlogin
from utils.utils import Utils

class Mainpage_renyuanguanli(Openandlogin):

    locator_renyuanxingming="com.zhilian.yoga:id/tv_course_name"
    xiugaineirong="墨迹123"
    def xiugairenyuan(self):
        driver=self.driver
        driver.find_element_by_name("人员管理").click()
        driver.find_element_by_id(self.locator_renyuanxingming).click()
        driver.find_element_by_name("修改").click()
        one=driver.find_element_by_id("com.zhilian.yoga:id/et_name")
        Utils().qingkong(driver,one)
        one.send_keys(self.xiugaineirong)
        driver.find_element_by_name("修改").click()

        two=driver.find_element_by_id("com.zhilian.yoga:id/tv_name")
        beice=self.xiugaineirong
        jieguo="修改后工作人员姓名"
        Utils().duanyan(two,beice,jieguo)
        driver.keyevent(4)

        three=self.locator_renyuanxingming
        Utils().duanyan(three,beice,jieguo)
        driver.keyevent(4)

