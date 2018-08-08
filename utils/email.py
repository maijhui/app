import re
import smtplib
from _socket import gaierror, error
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class Email():
    def __init__(self,server="smtp.qq.com",
                 sender="1691614276@qq.com",
                 password="jrlhfdrrzqedeehc",
                 receiver="472847165@qq.com",
                 files_path="C:\\Users\\Administrator\\Desktop\\test_log.txt",
                 title="登录报告",
                 message="这是正文"):

        self.msg = MIMEMultipart("related")
        self.server= server #服务器
        self.sender =  sender #发送人
        self.password= password #发送人密码
        self.receiver = receiver #接收人
        self.files_path = files_path  #附件地址
        self.title = title  # 标题
        self.message= message #正文内容


    def send_email(self):

        self.msg["Subject"]=self.title
        self.msg["From"]=self.sender
        self.msg["To"]=self.receiver
        self.msg.attach(MIMEText(self.message))

        if self.files_path:
            if isinstance(self.files_path, list):  #多个附件
                for f in self.files_path:
                    self._attach_file(f)
            elif isinstance(self.files_path, str): #一个附件
                self._attach_file(self.files_path)

    def _attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        # logger.info('attach file {}'.format(att_file))

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)  # 连接sever
        except (gaierror and error) as e:
            pass
            # logger.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
                smtp_server.login(self.sender, self.password)  # 登录
            except smtplib.SMTPAuthenticationError as e:
                pass
                # logger.exception('用户名密码验证失败！%s', e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())  # 发送邮件
            finally:
                smtp_server.quit()  # 断开连接
                # logger.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                #             '同时检查收件人地址是否正确'.format(self.title, self.receiver))

if __name__=="__main__":
    Email().send_email()