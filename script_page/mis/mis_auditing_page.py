import time

from selenium.webdriver.common.by import By
from script_base.mis_base import BaseMis, MisAction
from utils import Driver, check_channel


class MisAuditPage(BaseMis):
    def __init__(self):
        super().__init__()
        self.title = (By.XPATH, "//*[@placeholder='请输入: 文章名称']")
        self.channel = (By.XPATH, "//*[@placeholder='请输入: 频道']")
        self.select = (By.XPATH, "//*[text()='查询']")
        self.audit_pass = (By.XPATH, "//*[text()='通过']")
        self.audit_reject = (By.XPATH, "//*[text()='驳回']")
        self.pass_yes = (By.XPATH, "//span[contains(text(), '确定')]")

    def find_title(self):
        return self.find_elem(self.title)

    def find_channel(self):
        return self.find_elem(self.channel)

    def find_click_select(self):
        return self.find_elem(self.select)

    def find_pass(self):
        return self.find_elem(self.audit_pass)

    def find_reject(self):
        return self.find_elem(self.audit_reject)

    def find_yes(self):
        return self.find_elem(self.pass_yes)


class MisHandlePage(MisAction):
    def __init__(self):
        self.driver = Driver.get_driver_mis()
        self.mis_audit = MisAuditPage()

    def input_title(self, title):
        self.input_text(self.mis_audit.find_title(), title)

    def input_channel(self, channel):
        self.input_text(self.mis_audit.find_channel(), channel)

    def click_state(self, option_name):
        check_channel(self.driver, "请选择", option_name)

    def click_select(self):
        self.mis_audit.find_click_select().click()

    def click_reject(self):
        time.sleep(1)
        self.mis_audit.find_reject().click()

    def click_pass(self):
        time.sleep(1)
        self.mis_audit.find_pass().click()

    def click_yes(self):
        time.sleep(1)
        self.mis_audit.find_yes().click()


class MisProxyPage:
    def __init__(self):
        self.mis_handle = MisHandlePage()

    def mis_audit_pass(self, title, channel, option_name):
        self.mis_handle.input_title(title)
        self.mis_handle.input_channel(channel)
        self.mis_handle.click_state(option_name)
        self.mis_handle.click_select()
        self.mis_handle.click_pass()
        self.mis_handle.click_yes()

    def mis_audit_reject(self, title, channel, option_name):
        self.mis_handle.input_title(title)
        self.mis_handle.input_channel(channel)
        self.mis_handle.click_state(option_name)
        self.mis_handle.click_select()
        self.mis_handle.click_reject()
        self.mis_handle.click_yes()
