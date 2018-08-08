import os
from time import sleep


class Start():
    def __init__(self):
        self.packagename="com.zhilian.yoga"

    def test_start(self):
        os.popen("adb shell am force-stop " + self.packagename)
        sleep(1)
        os.popen("adb shell input keyevent 3")
        sleep(1)
        os.popen("adb shell am start -W -n com.zhilian.yoga/.Activity.SplashActivity")
        sleep(5)

    def test_close(self):
        os.popen("adb shell am force-stop " + self.packagename)
        sleep(1)
        os.popen("adb shell input keyevent 3")
        sleep(1)