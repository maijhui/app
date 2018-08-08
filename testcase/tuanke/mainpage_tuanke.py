from time import sleep

from common.login_page import Openandlogin
from utils.utils import Utils


class Mainpage_tuanke(Openandlogin):
    def paike(self):
        driver=self.driver
        driver.find_element_by_name("约课").click()
        driver.find_element_by_id("com.zhilian.yoga:id/iv_more").click()
        driver.find_element_by_name("新增团课课程").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_course_name").click()
        driver.find_element_by_name("确定").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_teacher_name").click()
        driver.find_element_by_id("com.zhilian.yoga:id/cb_tag").click()
        driver.find_element_by_name("确认").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_classroom").click()
        driver.find_element_by_name("确定").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_number").send_keys("2")
        driver.find_element_by_name("12").click()
        Utils().shanghua(driver)
        driver.find_element_by_id("com.zhilian.yoga:id/tv_date").click()
        sleep(2)
        Utils().shanghuazuobiao(driver,300,990,10)
        sleep(2)
        Utils().shanghuazuobiao(driver,300,990,500)
        driver.find_element_by_name("确定").click()
        driver.find_element_by_name("允许会员卡与付款").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_pay_sum").send_keys("1")
        driver.find_element_by_name("发布课程").click()
        driver.find_element_by_name("确认").click()
        driver.find_element_by_name("首页").click()
        #
        # def paike(self):
        #     driver = self.driver
        #     driver.find_element_by_name("约课").click()



        #
        #
        #
        #