from selenium.webdriver.common.by import By
from UI_Auto.page2.base_page import BasePage


class OutLogin(BasePage):
    _exit_location = (By.ID,"com.xueqiu.android:id/md_buttonDefaultPositive")
    def login_out(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("退出登录").instance(0));'
        ).click()
        #点击弹窗退出
        self.find_element_and_click(self._exit_location)
        return self


