from time import sleep

from common.login_page import Login_Page
from common.start import Start


class Page_login(Login_Logout):
    def correct_login(self,username,password):
        self.login(username,password)
        sleep(3)
        self.logout()

    def wrong_login(self,username,password):
        self.login(username,password)

