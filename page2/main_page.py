import time

from selenium.webdriver.common.by import By
from UI_Auto.page2.base_page import BasePage
from UI_Auto.page2.login_page import LoginPage
from UI_Auto.page2.outlogin_page import OutLogin


class MainPage(BasePage):
    def to_login(self):
        _login_locator1 = (By.ID, "com.xueqiu.android:id/profile_image")
        _login_locator2 = (By.XPATH, "//*[@text='帐号密码登录']")
        self.find_element_and_click(_login_locator1)
        self.find_element_and_click(_login_locator2)
        return LoginPage(self.driver)

    def to_outlogin(self):
        _already_login_locator = (By.ID, "com.xueqiu.android:id/profile_image")
        _setting_locator = (By.ID, "com.xueqiu.android:id/iv_setting")
        self.find_element_and_click(_already_login_locator)
        time.sleep(5)
        self.find_element_and_click(_setting_locator)
        return OutLogin(self.driver)


