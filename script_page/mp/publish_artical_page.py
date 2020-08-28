from selenium.webdriver.common.by import By
from script_base.mp_base import BaseMp, MpAction
from utils import Driver, check_channel


class PubPage(BaseMp):
    def __init__(self):
        super().__init__()
        self.ari_title = (By.CSS_SELECTOR, '[placeholder="文章名称"]')
        self.ari_iframe = (By.CSS_SELECTOR, '#publishTinymce_ifr')
        self.ari_context = (By.CSS_SELECTOR, 'body')
        self.ari_cover = (By.XPATH, '//*[text()="自动"]')
        # self.channel = (By.CSS_SELECTOR, '[placeholder="请选择"]')
        # self.channel_option = (By.XPATH, '//*[text()="android"]')
        self.pub_btn = (By.XPATH, '//*[text()="发表"]')

    def find_ari_title(self):
        return self.find_elem(self.ari_title)

    def find_ari_iframe(self):
        return self.find_elem(self.ari_iframe)

    def find_ari_context(self):
        return self.find_elem(self.ari_context)

    def find_ari_cover(self):
        return self.find_elem(self.ari_cover)

    def find_pub_btn(self):
        return self.find_elem(self.pub_btn)


class PubHandle(MpAction):
    def __init__(self):
        self.driver = Driver.get_driver_mp()
        self.pub_page = PubPage()

    def input_ari_title(self, ari_title):
        self.input_text(self.pub_page.find_ari_title(), ari_title)

    def input_ari_context(self, ari_context):
        self.driver.switch_to.frame(self.pub_page.find_ari_iframe())
        self.input_text(self.pub_page.find_ari_context(), ari_context)
        self.driver.switch_to.default_content()

    def click_ari_cover(self):
        self.pub_page.find_ari_cover().click()

    def click_channel(self, option_name):
        check_channel(self.driver, "请选择", option_name)

    def click_pub_btn(self):
        self.pub_page.find_pub_btn().click()


class PubProxy:
    def __init__(self):
        self.pub_handle = PubHandle()

    def pub_art(self, ari_title, ari_context, option_name):
        self.pub_handle.input_ari_title(ari_title)
        self.pub_handle.input_ari_context(ari_context)
        self.pub_handle.click_ari_cover()
        self.pub_handle.click_channel(option_name)
        self.pub_handle.click_pub_btn()
