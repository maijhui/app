from time import sleep

from common.login_page import Openandlogin
from utils.utils import Utils


class Mainpage_huiyuanguanli(Openandlogin):
    #修改会员资料
    def xiugaihuiyuan(self):
        driver=self.driver
        driver.find_element_by_name("会员管理").click()
        driver.find_element_by_name("a麦").click()
        driver.find_element_by_name("修改").click()
        one=driver.find_element_by_id("com.zhilian.yoga:id/et_name")
        Utils().qingkong(driver,one)
        one.send_keys("a麦123")
        Utils().shanghua(driver)
        driver.find_element_by_name("保存修改").click()

        two=driver.find_element_by_id("com.zhilian.yoga:id/tv_name")
        beice="a麦123"
        jieguo="修改后会员详情名称"
        Utils().duanyan(two,beice,jieguo)
        driver.keyevent(4)

        three=driver.find_elements_by_id("com.zhilian.yoga:id/item_userlist_name")
        beice = "a麦123"
        jieguo="修改后会员列表名称"

        for i in range(100):
            if(three[i].text==beice):
                print("修改后会员列表名称"+"："+three[i].text+"通过")
                break
            else:
                continue
        driver.keyevent(4)

    #拉黑会员
    def lahei(self):
        driver = self.driver
        driver.find_element_by_name("会员管理").click()
        content="a麦"
        Utils().baohanwenzi(driver,content)
        driver.find_element_by_name("拉黑").click()
        driver.find_element_by_name("确定").click()
        sleep(3)
        driver.find_element_by_name("恢复").click()
        driver.find_element_by_name("确定").click()
        print("拉黑、恢复，通过")
        driver.keyevent(4)
        sleep(3)
        driver.keyevent(4)

    #会员开卡
    def kaika(self):
        driver = self.driver
        driver.find_element_by_name("会员管理").click()
        content = "a麦"
        Utils().baohanwenzi(driver, content)
        driver.find_element_by_name("开卡").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_card_type").click()
        sleep(3)
        heng=260/1080
        zong1=1640/1914
        zong2=1000/1914
        Utils().shanghuazuobiao(driver,heng,zong1,zong2)
        driver.find_element_by_name("确定").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_paid").send_keys("23")
        Utils().shanghua(driver)
        driver.find_element_by_name("确认开卡").click()

        driver.find_element_by_name("会员卡").click()
        one =driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_name")
        beice="通用期限卡"
        jieguo="新增的会员卡名称"
        Utils().duanyan(one,beice,jieguo)
        driver.keyevent(4)
        sleep(3)
        driver.keyevent(4)


    #删除会员卡
    def shanchuhuiyuanka(self):
        driver = self.driver
        driver.find_element_by_name("会员管理").click()
        content = "a麦"
        Utils().baohanwenzi(driver, content)
        driver.find_element_by_name("会员卡").click()
        driver.find_element_by_name("通用期限卡").click()
        driver.find_element_by_name("删除").click()
        driver.find_element_by_name("确认").click()

        one = driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_name")
        beice = "通用期限卡"
        jieguo = "删除后会员卡名称"
        Utils().duanyanx(one, beice, jieguo)
        driver.keyevent(4)
        sleep(3)
        driver.keyevent(4)


    #延期会员卡
    def yanqihuiyuanka(self):
        driver=self.driver
        driver.find_element_by_name("会员管理").click()
        Utils().baohanwenzi(driver, "a麦")
        driver.find_element_by_name("会员卡").click()
        a = driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_term").text
        driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_name").click()
        driver.find_element_by_name("延期").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_choice_delay_time").click()
        sleep(3)
        Utils().shanghuazuobiao(driver,210/1080,1000/1914,600/1914)
        driver.find_element_by_name("确定").click()
        driver.find_element_by_name("确认").click()
        driver.keyevent(4)
        #com.zhilian.yoga:id/item_usercard_term

        b=driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_term").text
        if(a!=b):

            print("延期会员卡通过")
            print("延期前：" + a)
            print("延期后：" + b)
        else:
            print("延期会员卡不通过")
            print("延期前：" + a)
            print("延期后：" + b)

        driver.keyevent(4)
        sleep(3)
        driver.keyevent(4)


    #冻结会员卡
    def dongjiehuiyuanka(self):
        driver = self.driver
        driver.find_element_by_name("会员管理").click()
        Utils().baohanwenzi(driver, "a麦")
        driver.find_element_by_name("会员卡").click()
        driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_name").click()
        driver.find_element_by_name("冻结").click()
        driver.find_element_by_name("确认").click()
        sleep(3)
        driver.find_element_by_name("解冻").click()
        driver.find_element_by_name("确认").click()

        driver.keyevent(4)
        sleep(3)
        driver.keyevent(4)
        sleep(3)
        driver.keyevent(4)


    #请假会员卡
    def qingjiahuiyuanka(self):
        driver = self.driver
        driver.find_element_by_name("会员管理").click()
        Utils().baohanwenzi(driver, "a麦")
        driver.find_element_by_name("会员卡").click()
        driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_name").click()
        driver.find_element_by_name("请假").click()
        driver.find_element_by_name("请输入请假原因").send_keys("出国旅游")
        driver.find_element_by_id("com.zhilian.yoga:id/tv_start_time").click()
        driver.find_element_by_name("确定").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_end_time").click()
        sleep(3)
        Utils().shanghuazuobiao(driver,560,1080,850)
        sleep(2)
        driver.find_element_by_name("确定").click()
        driver.find_element_by_name("确认").click()
        sleep(5)

        driver.find_element_by_name("销假").click()
        driver.find_element_by_name("确认").click()
        driver.keyevent(4)
        sleep(3)
        driver.keyevent(4)
        sleep(3)
        driver.keyevent(4)



    #充值会员卡
    def chongzhihuiyuanka(self):
        driver = self.driver
        driver.find_element_by_name("会员管理").click()
        Utils().baohanwenzi(driver, "a麦")
        driver.find_element_by_name("会员卡").click()
        for i in range(100):
            one=driver.find_elements_by_id("com.zhilian.yoga:id/item_usercard_name")
            if("次" in one[i].text):
                print(one[i].text)
                one[i].click()
                break

            else:
                continue

        driver.find_element_by_name("充值").click()
        two=driver.find_element_by_id("com.zhilian.yoga:id/tv_current_numbers").text
        driver.find_element_by_id("com.zhilian.yoga:id/et_recharge_numbers").send_keys("1")
        driver.find_element_by_id("com.zhilian.yoga:id/et_note").send_keys("充值1")
        driver.find_element_by_name("确认").click()
        three=driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_time").text
        if(two+"次" == three):
            print("充值会员卡测试不通过")
            print("充值前："+two)
            print("充值后："+three)
        else:
            print("充值会员卡测试通过")
            print("充值前：" + two)
            print("充值后：" + three)

        driver.keyevent(4)
        sleep(2)
        driver.keyevent(4)
        sleep(2)
        driver.keyevent(4)
        sleep(2)

    #体测模板
    def ticemuban(self):
        driver = self.driver
        driver.find_element_by_name("会员管理").click()
        Utils().baohanwenzi(driver, "a麦")
        driver.find_element_by_name("体测模板").click()
        driver.find_element_by_name("修改").click()
        one=driver.find_element_by_id("com.zhilian.yoga:id/et_info")
        Utils().qingkong(driver,one)
        one.send_keys("188")
        driver.find_element_by_name("修改").click()
        two=driver.find_element_by_id("com.zhilian.yoga:id/tv_content").text
        if ("188" in two):
            print("体测模板测试通过")
            print("体测模板：" + two)
        else:
            print("体测模板测试不通过")
            print("体测模板：" + two)

        driver.keyevent(4)
        sleep(2)
        driver.keyevent(4)

    def sousuohuiyuan(self):
        driver = self.driver
        driver.find_element_by_name("会员管理").click()
        driver.find_element_by_name("搜索").click()
        sleep(2)
        driver.find_element_by_name("搜索").send_keys("a")

        driver.find_element_by_id("com.zhilian.yoga:id/tv_search").click()
        one=driver.find_elements_by_id("com.zhilian.yoga:id/item_userlist_name")
        for i in range(len(one)):
            if("a"or"A" in one[i].text):
                print(one[i].text+"：测试通过")
                continue
            else:
                print(one[i].text+"：测试失败")
                continue


