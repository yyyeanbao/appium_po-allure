import datetime
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from UI_Auto.page2.main_page import MainPage
import os

# 获取项目的根目录路径
p = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
p = p.replace("UI_Auto","")

# 获取app的路径
appPath = lambda x: os.path.join(p, "test_packages", x)


# print(appPath("xueqiu.apk"))
class App:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "seveniruby"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["app"] = appPath("xueqiu.apk")
        caps["autoGrantPermissions"] = "true"
        caps["showChromedriverLog"] = True
        caps['noReset'] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        print(caps)
        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()


get = App
get.start()