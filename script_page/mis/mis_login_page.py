from selenium.webdriver.common.by import By

from script_base.mis_base import BaseMis, MisAction
from utils import Driver


class MisLoginPage(BaseMis):

    def __init__(self):
        super().__init__()
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.ID, "inp1")

    def find_username(self):
        return self.find_elem(self.username)

    def find_password(self):
        return self.find_elem(self.password)

    def find_login_btn(self):
        return self.find_elem(self.login_btn)


class MisHandlePage(MisAction):

    def __init__(self):
        self.mis_login = MisLoginPage()

    def input_username(self, username):
        self.input_text(self.mis_login.find_username(), username)

    def input_password(self, password):
        self.input_text(self.mis_login.find_password(), password)

    def click_login_btn(self):
        js_str = "document.getElementById('inp1').removeAttribute('disabled')"
        Driver.get_driver_mis().execute_script(js_str)
        self.mis_login.find_login_btn().click()


class MisProxyPage:
    def __init__(self):
        self.handle = MisHandlePage()

    def mis_proxy(self, username, password):
        self.handle.input_username(username)
        self.handle.input_password(password)
        self.handle.click_login_btn()
