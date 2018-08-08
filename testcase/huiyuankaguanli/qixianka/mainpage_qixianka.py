from time import sleep
from common.login_page import Openandlogin
from utils.utils import Utils


class Mainpage_qixianka(Openandlogin):
    def xinzengqixianka(self):
        driver=self.driver
        driver.find_element_by_name("会员卡管理").click()
        driver.find_element_by_id("com.zhilian.yoga:id/iv_baseAdd").click()
        driver.find_element_by_id("com.zhilian.yoga:id/tv_menu_item_text").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_card_name").send_keys("道瑜伽期限卡")
        driver.find_element_by_id("com.zhilian.yoga:id/et_card_limit_times").send_keys("12")
        driver.find_element_by_id("com.zhilian.yoga:id/et_card_price").send_keys("0.01")
        driver.find_element_by_id("com.zhilian.yoga:id/et_card_introduction").send_keys("这是道瑜伽期限卡介绍")
        driver.find_element_by_id("com.zhilian.yoga:id/rl_can_use_shop").click()
        elements=driver.find_elements_by_id("com.zhilian.yoga:id/cb_tag")
        elements[1].click()
        driver.find_element_by_name("确认").click()
        Utils().shanghua(driver)
        driver.find_element_by_name("保存").click()

        two=driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_name")
        beice="道瑜伽期限卡"
        jieguo="新增期限卡名称"
        Utils().duanyan(two,beice,jieguo)
        driver.keyevent(4)


    def xiugaiqixianka(self):
        driver = self.driver
        driver.find_element_by_name("会员卡管理").click()
        driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_name").click()
        driver.find_element_by_name("修改限制").click()
        driver.find_element_by_id("android.widget.RelativeLayout").click()
        driver.find_element_by_id("com.zhilian.yoga:id/et_limit").click()
        driver.find_element_by_name("保存").click()


        one=driver.find_element_by_id("com.zhilian.yoga:id/item_usercard_name")
        beice="道瑜伽期限卡"
        jieguo="修改期限卡后的名称是"
        Utils().duanyan(one,beice,jieguo)

