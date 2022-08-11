from time import sleep
from selenium.webdriver.common.by import By
from UI_Auto.page2.base_page import BasePage


class LoginPage(BasePage):

    def login1(self,accout,passwd):
        clear_location = (By.ID, "com.xueqiu.android:id/iv_delete_text")
        account_location = (By.ID, "com.xueqiu.android:id/login_account")
        pwd_location = (By.ID, "com.xueqiu.android:id/login_password")
        c_location = (By.ID, "com.xueqiu.android:id/button_next")
        sleep(5)
        self.find_element_init(account_location).send_keys(accout)
        self.find_element_init(pwd_location).send_keys(passwd)
        self.find_element_and_click(c_location)
        return self



    def get_login_index(self):
        back_location = (By.ID, "com.xueqiu.android:id/iv_action_back")
        inde_location = (By.ID, "com.xueqiu.android:id/title_text")
        self.find_element_and_click(back_location)
        index = self.find_element_init(inde_location)
        if index:
            return index.text


