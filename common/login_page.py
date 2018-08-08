from time import sleep
from appium import webdriver
from utils.utils import Utils


class Login_Page():
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.zhilian.yoga'
        desired_caps['appActivity'] = 'com.zhilian.yoga.Activity.SplashActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        sleep(3)

    def login(self,username,password):
        driver = self.driver
        element_one=driver.find_element_by_id("com.zhilian.yoga:id/login_et_username")
        Utils().clear(driver,element_one)
        element_one.send_keys(username)
        element_two = driver.find_element_by_id("com.zhilian.yoga:id/login_et_password")
        Utils().clear(driver, element_two)
        element_two.send_keys(password)
        driver.find_element_by_name("登录").click()



    def logout(self):
        driver=self.driver
        driver.find_element_by_name("我的").click()
        Utils().tap_up(driver)
        driver.find_element_by_name("退出登录").click()
        driver.find_element_by_name("确定").click()

