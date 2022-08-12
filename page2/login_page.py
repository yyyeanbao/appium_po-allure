from time import sleep
from selenium.webdriver.common.by import By
from UI_Auto.page2.base_page import BasePage


class LoginPage(BasePage):
    _clear_location = (By.ID, "com.xueqiu.android:id/iv_delete_text")
    _account_location = (By.ID, "com.xueqiu.android:id/login_account")
    _pwd_location = (By.ID, "com.xueqiu.android:id/login_password")
    _c_location = (By.ID, "com.xueqiu.android:id/button_next")
    _user_error = (By.XPATH, "//*[@text='用户名或密码错误']")
    _user_error_sure = (By.XPATH, "//*[@text='确定']")
    def login1(self,accout,passwd):
        sleep(5)
        self.find_element_init(self._account_location).send_keys(accout)
        self.find_element_init(self._pwd_location).send_keys(passwd)
        self.find_element_and_click(self._c_location)
        return self

    def login_fail(self,accout,passwd):
        sleep(5)
        self.find_element_init(self._account_location).send_keys(accout)
        self.find_element_init(self._pwd_location).send_keys(passwd)
        self.find_element_and_click(self._c_location)
        self.find_element_init(self._user_error)
        self.find_element_and_click(self._user_error_sure)


    def get_login_index(self):
        back_location = (By.ID, "com.xueqiu.android:id/iv_action_back")
        inde_location = (By.ID, "com.xueqiu.android:id/title_text")
        self.find_element_and_click(back_location)
        index = self.find_element_init(inde_location)
        if index:
            return index.text


