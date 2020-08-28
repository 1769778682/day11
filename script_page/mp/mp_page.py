import allure
from selenium.webdriver.common.by import By

from script_base.mp_base import BaseMp, MpAction


class LoginPage(BaseMp):

    def __init__(self):
        super().__init__()
        self.username = (By.CSS_SELECTOR, '[placeholder*="手机号"]')
        self.code = (By.CSS_SELECTOR, '[placeholder*="验证码"]')
        self.login_btn = (By.CSS_SELECTOR, '.el-button--primary')

    def find_username(self):
        return self.find_elem(self.username)

    def find_code(self):
        return self.find_elem(self.code)

    def find_login_btn(self):
        return self.find_elem(self.login_btn)


@allure.step(title="登录操作层")
class LoginHandle(MpAction):

    def __init__(self):
        self.driver = LoginPage()

    @allure.step(title="输入用户名")
    def input_username(self, username):
        self.input_text(self.driver.find_username(), username)

    @allure.step(title="输入密码")
    def input_code(self, code):
        self.input_text(self.driver.find_code(), code)

    @allure.step(title="点击登录")
    def click_login_btn(self):
        self.driver.find_login_btn().click()


class LoginProxy(object):
    def __init__(self):
        self.login_mp = LoginHandle()

    def mp_login(self, username, code):
        self.login_mp.input_username(username)
        self.login_mp.input_code(code)
        self.login_mp.click_login_btn()
