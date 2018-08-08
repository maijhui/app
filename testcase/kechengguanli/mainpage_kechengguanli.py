from time import sleep
from common.login_page import Openandlogin


class Mainpage(Openandlogin):

    #新增课程
    def xinzengkecheng(self):
        driver=self.driver
        driver.find_element_by_name("课程管理").click()
        driver.find_element_by_id("com.zhilian.yoga:id/iv_baseAdd").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_course_name").send_keys("道瑜伽1")
        driver.find_element_by_id("com.zhilian.yoga:id/et_time").send_keys("30")
        driver.find_element_by_id("com.zhilian.yoga:id/iv_cover").click()
        driver.find_element_by_id("com.zhilian.yoga:id/cb_check").click()
        driver.find_element_by_id("com.zhilian.yoga:id/btn_ok").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_introduction").send_keys("这是道瑜伽简介")
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 8 * y, 200)  # 200毫秒
        driver.find_element_by_name("保存").click()
        one = driver.find_element_by_id("com.zhilian.yoga:id/tv_course_name")
        two = driver.find_element_by_id("com.zhilian.yoga:id/tv_course_time")
        three = driver.find_element_by_id("com.zhilian.yoga:id/tv_course_introduction")
        if (one.text == "道瑜伽1"):
            print("新增课程名称："+one.text+"，通过")
        else:
            print("新增课程名称："+one.text+"，不通过")
        if (two.text == "时长:30分钟"):
            print("新增课程时长："+two.text+"，通过")
        else:
            print("新增课程时长："+two.text+"，不通过")
        if (three.text == "这是道瑜伽简介"):
            print("新增课程简介："+three.text+"，通过")
        else:
            print("新增课程简介："+three.text+"，不通过")



    #修改课程
    def xiugaikecheng(self):
        driver = self.driver
        driver.find_element_by_id("com.zhilian.yoga:id/rl_main").click()
        driver.find_element_by_id("com.zhilian.yoga:id/btn_change").click()
        one = driver.find_element_by_id("com.zhilian.yoga:id/et_course_name")
        self.editClear(driver, one)
        one.send_keys("道瑜伽123")

        two = driver.find_element_by_id("com.zhilian.yoga:id/et_time")
        self.editClear(driver, two)
        two.send_keys("60")

        three = driver.find_element_by_id("com.zhilian.yoga:id/et_introduction")
        self.editClear(driver, three)
        three.send_keys("这是道瑜伽简介123")

        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 8 * y, 200)  # 200毫秒
        driver.find_element_by_name("修改").click()

        sleep(3)
        oneafter = driver.find_element_by_id("com.zhilian.yoga:id/tv_course_name")
        if (oneafter.text == "道瑜伽1"):
            print("修改课程详情名称：" + oneafter.text+"，不通过")
        else:
            print("修改课程详情名称：" + oneafter.text+"，通过")

        driver.find_element_by_id("com.zhilian.yoga:id/iv_baseBack").click()
        oneafteragain = driver.find_element_by_id("com.zhilian.yoga:id/tv_course_name")
        if (oneafteragain.text == "道瑜伽1"):
            print("修改课程列表名称：" + oneafteragain.text+"，不通过")
        else:
            print("修改课程列表名称：" + oneafteragain.text+"，通过")



    #删除课程
    def shanchukecheng(self):
        driver=self.driver
        driver.find_element_by_id("com.zhilian.yoga:id/rl_main").click()
        driver.find_element_by_id("com.zhilian.yoga:id/btn_del").click()
        one = driver.find_element_by_id("com.zhilian.yoga:id/tv_course_name")
        if (one.text == "道瑜伽1"):
            print("删除后课程名称："+one.text+"，不通过")
        else:
            print("删除后课程名称："+one.text+"，通过")



    #封装清空输入框
    def editClear(self,driver, el):
        el.click()
        driver.keyevent(123)
        textLength = len(str(el.text))
        for i in range(0, textLength):
            driver.keyevent(67)