import logging
import os
import re
import smtplib
import unittest
from HTMLTestRunner import HTMLTestRunner
from _socket import gaierror,error
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from logging.handlers import TimedRotatingFileHandler
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Utils():
    #上滑
    def tap_up(self,driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        sleep(2)
        driver.swipe(0.5 * x,0.99 * y,0.5 * x,0.01 * y,duration=5000)
        sleep(2)

    #上滑到固定坐标
    def tap_up_coordinate(self,driver,x,y_start,y_end):
        sleep(2)
        x = driver.get_window_size()['width']
        driver.swipe(0.5 * x , y_start , 0.5 * x , y_end , duration=5000)
        sleep(2)

    #正断言
    def assertion(self,one,beice,jieguo):

        # try:
        #     assert(one.text == beice),print(jieguo+"："+one.text+"，通过")
        # except:
        #     print(jieguo + "：" + one.text + "，不通过")
        if (one.text == beice):
            self.get_logger().info(jieguo+"："+one.text+"，通过")
            print(jieguo+"："+one.text+"，通过")

        else:
            self.get_logger().info(jieguo + "：" + one.text + "，通过")
            print(jieguo+"："+one.text+"，不通过")

    #反断言
    def duanyanx(self,one,beice,jieguo):
        if (one.text == beice):
            self.get_logger().info(jieguo + "：" + one.text + "，不通过")
            print(jieguo+"："+one.text+"，不通过")
        else:
            self.get_logger().info(jieguo + "：" + one.text + "，通过")
            print(jieguo+"："+one.text+"，通过")

    #清空输入框内容
    def clear(self,driver, element):
        element.click()
        driver.keyevent(123)
        textLength = len(str(element.text))
        for i in range(0, textLength):
            driver.keyevent(67)

    #上传图片
    def upload_picture(self,driver):
        driver.find_element_by_id("com.zhilian.yoga:id/iv").click()
        driver.find_element_by_id("com.zhilian.yoga:id/cb_check").click()
        driver.find_element_by_id("com.zhilian.yoga:id/btn_ok").click()

    #包含文字，定位，点击
    def baohanwenzi(self,driver,content):
        #//android.widget.TextView[contains(@text,'content')]
        locator="//android.widget.TextView[contains(@text,'"+content+"')]"
        driver.find_element_by_xpath(locator).click()


    #权限
    #WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
    def authority(self,driver):
        for i in range(6):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    #unittest的discover，寻找所有test开头的py文件执行
    def run_alltestcase_discover(self):
        test_dir = "./"
        discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
        runner = unittest.TextTestRunner()
        runner.run(discover)



    #生成html报告
    def HTML_report(self,one):
        report_file_path = 'C:\\Users\\Administrator\\Desktop\\report.html'
        with open(report_file_path, 'wb') as file:  # 打开报告
            runner = HTMLTestRunner(file, verbosity=2, title='app登录科韵路瑜伽馆账号',
                                    description='登录成功后，测试完成')  # 实例化HTML报告对象，传参
            runner.run(one)  # 运行用例
            # runner.run(TestBaiDu('test_print'))  # TestBaiDu是类名，test_print是方法名










    #log日志
    def get_logger(self,logger_name='framework'):
        self.logger = logging.getLogger(logger_name)  # 日志中的日志名
        logging.root.setLevel(logging.NOTSET)
        self.logfilename = 'test.log'  # 日志文件名称
        self.backup_count = 5  # #备份数
        self.console_output_level = 'WARNING'  # 控制台输入级别
        self.file_output_level = 'DEBUG'  # 文件输出级别
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 日志输入格式

        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join("C:\\Users\\Administrator\\PycharmProjects\\app_aideyujia\\report", self.logfilename),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger



#发邮件
class Email():
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        """初始化Email

        :param title: 邮件标题，必填。
        :param message: 邮件正文，非必填。
        :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        :param server: smtp服务器，必填。
        :param sender: 发件人，必填。
        :param password: 发件人密码，必填。
        :param receiver: 收件人，多收件人用“；”隔开，必填。
        """
        self.title = title
        self.message = message
        self.files = path
        self.msg = MIMEMultipart('related')
        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

    def _attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        Utils().get_logger().info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)  # 连接sever
        except (gaierror and error) as e:
            Utils().get_logger().exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
                smtp_server.login(self.sender, self.password)  # 登录
            except smtplib.SMTPAuthenticationError as e:
                Utils().get_logger().exception('用户名密码验证失败！%s', e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())  # 发送邮件
            finally:
                smtp_server.quit()  # 断开连接
                Utils().get_logger().info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))

