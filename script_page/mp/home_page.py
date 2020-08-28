import allure
from selenium.webdriver.common.by import By

from script_base.mp_base import BaseMp


class HomePage(BaseMp):

    def __init__(self):
        super().__init__()
        self.context_tab = (By.XPATH, "//*[text()='内容管理']")
        self.pub_ari_tab = (By.XPATH, "//*[contains(text(),'发布文章')]")

    def find_context_tab(self):
        return self.find_elem(self.context_tab)

    def find_pub_art_tab(self):
        return self.find_elem(self.pub_ari_tab)


@allure.step(title="操作层")
class HomeHandle:

    def __init__(self):
        self.home_page = HomePage()

    @allure.step(title="点击文章")
    def click_context_tab(self):
        self.home_page.find_context_tab().click()

    @allure.step(title="点击新建文章")
    def click_pub_art_tab(self):
        self.home_page.find_pub_art_tab().click()


class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    def home_proxy(self):
        self.home_handle.click_context_tab()
        self.home_handle.click_pub_art_tab()
