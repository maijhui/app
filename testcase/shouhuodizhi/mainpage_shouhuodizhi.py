from time import sleep

from common.login_page import Openandlogin
from utils.utils import Utils


class Mainpage_shouhuodizhi(Openandlogin):
    def xinzengshouhuodizhi(self):
        driver=self.driver
        driver.find_element_by_name("我的").click()
        driver.find_element_by_name("收货地址").click()
        driver.find_element_by_name("添加地址").click()
        driver.find_element_by_name("请输入收货人姓名").send_keys("陈陈陈")
        driver.find_element_by_name("请输入联系电话").send_keys("13377766381")
        driver.find_element_by_name("请输入邮编").send_keys("523520")
        driver.find_element_by_id("com.zhilian.yoga:id/tv_region").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_region").click()
        sleep(3)
        heng=200/1080
        zong1=1655/1916
        zong2=855/1916#一个80
        Utils().shanghuazuobiao(driver,heng,zong1,zong2)
        sleep(3)
        driver.find_element_by_name("确定").click()
        driver.find_element_by_name("请输入详细地址").send_keys("alibaba")
        driver.find_element_by_name("保存").click()

        one=driver.find_elements_by_id("com.zhilian.yoga:id/tv_address_name")[1]
        beice="陈陈陈"
        jieguo="收货人姓名"
        Utils().duanyan(one,beice,jieguo)
        driver.keyevent(4)

    def xiugaishouhuodizhi(self):
        driver = self.driver
        driver.find_element_by_name("我的").click()
        driver.find_element_by_name("收货地址").click()
        driver.find_elements_by_name("编辑")[1].click()
        one=driver.find_element_by_id("com.zhilian.yoga:id/et_name")
        Utils().qingkong(driver,one)
        one.send_keys("陈陈陈123")
        driver.find_element_by_name("保存").click()

        two= driver.find_elements_by_id("com.zhilian.yoga:id/tv_address_name")[1]
        beice="陈陈陈123"
        jieguo="修改后收货人姓名"
        Utils().duanyan(two,beice,jieguo)
        driver.keyevent(4)

    def shanchushouhuodizhi(self):
        driver = self.driver
        driver.find_element_by_name("我的").click()
        driver.find_element_by_name("收货地址").click()
        driver.find_elements_by_name("删除")[1].click()

        try:
            driver.find_elements_by_id("com.zhilian.yoga:id/tv_address_name")[1]

        except:
            print("新增的收货地址已经删除")



