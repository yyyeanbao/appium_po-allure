from UI_Auto.page2.app import App

class TestDemo:

    def setup(self):
        self.login_page = App.start()
    def test_loginerror_po(self):
        self.login_page.to_login().login_fail("1741194780@qq.com","123456")

    def test_login_po(self):
        self.login_page.to_login().login1("1741194780@qq.com","0987654321q")

    def test_outlogin_po(self):
        self.login_page.to_outlogin().login_out()

    def teardown(self):
        App.quit()











