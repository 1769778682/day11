from selenium.webdriver.common.by import By

from script_base.mis_base import BaseMis


class MisHomePage(BaseMis):

    def __init__(self):
        super().__init__()
        self.information = (By.XPATH, "//*[text()='信息管理']")
        self.auditing = (By.XPATH, "//*[text()='内容审核']")

    def find_information(self):
        return self.find_elem(self.information)

    def find_auditing(self):
        return self.find_elem(self.auditing)


class MisHandlePage:
    def __init__(self):
        self.mis_home = MisHomePage()

    def click_information(self):
        self.mis_home.find_information().click()

    def click_auditing(self):
        self.mis_home.find_auditing().click()


class MisProxyHome:

    def __init__(self):
        self.mis_handle = MisHandlePage()

    def mis_handle_home(self):
        self.mis_handle.click_information()
        self.mis_handle.click_auditing()
