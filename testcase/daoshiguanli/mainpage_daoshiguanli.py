from time import sleep
from common.login_page import Openandlogin
from utils.utils import Utils


class Mainpage(Openandlogin):


    #新增导师
    def xinzengdaoshi(self):
        driver=self.driver
        driver.find_element_by_name("导师管理").click()
        driver.find_element_by_id("com.zhilian.yoga:id/iv_baseAdd").click()
        driver.find_element_by_id("com.zhilian.yoga:id/iv_choose_head").click()
        driver.find_element_by_id("com.zhilian.yoga:id/cb_check").click()
        driver.find_element_by_id("com.zhilian.yoga:id/btn_ok").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_name").send_keys("道老师")
        driver.find_element_by_id("com.zhilian.yoga:id/et_phone").send_keys("13377766888") #输入完会减掉一位数？？？
        driver.find_element_by_id("com.zhilian.yoga:id/rb_female").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_email").send_keys("472847165@qq.com")
        driver.find_element_by_id("com.zhilian.yoga:id/tv_choose_lesson").click()
        driver.find_element_by_name("热瑜伽").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_comfirm").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_choose_mainstream").click()
        driver.find_element_by_name("智瑜伽").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_comfirm").click()
        Utils().shanghua(driver)
        driver.find_element_by_id("com.zhilian.yoga:id/et_tutor_introduction").send_keys("这是老师简介")
        driver.find_element_by_id("com.zhilian.yoga:id/et_tutor_experience").send_keys("这是老师证书和经历")
        driver.find_element_by_id("com.zhilian.yoga:id/iv").click()
        driver.find_element_by_id("com.zhilian.yoga:id/cb_check").click()
        driver.find_element_by_id("com.zhilian.yoga:id/btn_ok").click()
        driver.find_element_by_id("com.zhilian.yoga:id/btn_sumbit").click()

        #断言验证
        one = driver.find_element_by_id("com.zhilian.yoga:id/tv_course_name")
        beice="道老师"
        jieguo="新增老师名称："
        Utils().duanyan(one,beice,jieguo)

        driver.find_element_by_id("com.zhilian.yoga:id/iv_baseBack").click()

    #修改导师
    def xiugaidaoshi(self):
        driver = self.driver
        driver.find_element_by_name("导师管理").click()
        driver.find_element_by_name("道老师").click()
        driver.find_element_by_name("修改").click()
        one=driver.find_element_by_id("com.zhilian.yoga:id/et_name")
        Utils().qingkong(driver,one)
        one.send_keys("道老师123")
        Utils().shanghua(driver)
        driver.find_element_by_name("修改").click()

        one=driver.find_element_by_id("com.zhilian.yoga:id/tv_name")
        beice = "道老师123"
        jieguo = "修改后老师详情名称："
        Utils().duanyan(one,beice,jieguo)
        driver.find_element_by_id("com.zhilian.yoga:id/iv_baseBack").click()

        two=driver.find_element_by_id("com.zhilian.yoga:id/tv_course_name")
        beice = "道老师123"
        jieguo = "修改后老师列表名称："
        Utils().duanyan(two, beice, jieguo)
        driver.find_element_by_id("com.zhilian.yoga:id/iv_baseBack").click()

    #删除导师
    def shanchudaoshi(self):
        driver = self.driver
        driver.find_element_by_name("导师管理").click()
        driver.find_element_by_name("道老师123").click()
        driver.find_element_by_name("删除").click()

        one = driver.find_element_by_id("com.zhilian.yoga:id/tv_course_name")
        beice = "方老师123"
        jieguo = "删除后老师列表名称："
        Utils().duanyan(one, beice, jieguo)

