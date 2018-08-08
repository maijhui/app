from common.login_page import Openandlogin
from utils.utils import Utils


class Mainpage_keshiguanli(Openandlogin):
    #新增课室
    def xinzengkeshi(self):
        driver=self.driver
        driver.find_element_by_name("课室管理").click()
        driver.find_element_by_id("com.zhilian.yoga:id/iv_baseAdd").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_name").send_keys("道家班")
        Utils().shangchuantupian(driver)
        driver.find_element_by_name("保存").click()

        #断言
        one = driver.find_element_by_id("com.zhilian.yoga:id/tv")
        beice="道家班"
        jieguo="新增课室名称"
        Utils().duanyan(one,beice,jieguo)
        driver.find_element_by_id("com.zhilian.yoga:id/iv_baseBack").click()

    #修改课室
    def xiugaikeshi(self):
        driver = self.driver
        driver.find_element_by_name("课室管理").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv").click()
        one=driver.find_element_by_name("道家班")
        Utils().qingkong(driver,one)
        driver.find_element_by_id("com.zhilian.yoga:id/et_name").send_keys("道家班123")
        driver.find_element_by_name("修改").click()

        #断言
        two=driver.find_element_by_id("com.zhilian.yoga:id/tv")
        beice="道家班123"
        jieguo="修改课室名称"
        Utils().duanyan(two, beice, jieguo)









