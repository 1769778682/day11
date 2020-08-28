"""
手机端黑马头条首页
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from script_base.app_base import BaseApp
from utils import Driver


class AppIndexPage(BaseApp):

    def __init__(self):
        super().__init__()
        # 频道元素对象
        self.channel = (By.XPATH, "//*[contains(@text,'{}')]")
        # 频道选项区域元素对象
        self.channel_area = (By.CLASS_NAME, "android.widget.HorizontalScrollView")
        # 第一条文章元素对象
        self.first_article = (By.XPATH, "//*[@class='android.view.View' and @instance='1']")

    def find_channel(self, channel_name):
        return Driver.get_driver_app().find_element(self.channel[0], self.channel[1].format(channel_name))

    def find_channel_area(self):
        return self.find_elem(self.channel_area)

    def find_first_article(self):
        return self.find_elem(self.first_article)


class AppIndexHandle:
    def __init__(self):
        self.index_elem = AppIndexPage()
        self.driver = Driver.get_driver_app()

    def check_channel_option(self, channel_name):
        # 获取区域元素的所在位置
        area_elem = self.index_elem.find_channel_area()
        x = area_elem.location["x"]
        y = area_elem.location["y"]
        # 获取区域元素的大小
        w = area_elem.size["width"]
        h = area_elem.size["height"]
        # 计算起始按住的滑动点坐标
        start_x = x + w * 0.8
        start_y = y + h * 0.5
        # 计算目标位置的坐标
        end_x = x + w * 0.2
        end_y = start_y
        while True:
            # 先获取一次界面信息
            page_old = self.driver.page_source
            # 在当前区域中查找我们所想选择的频道元素对象
            try:
                # 如果能找到则点击
                self.index_elem.find_channel(channel_name).click()
                break
            except Exception as e:
                # 如果找不到则再次滑动
                self.driver.swipe(start_x, start_y, end_x, end_y)
                # 再获取一次界面信息和滑动前的相等
                page_new = self.driver.page_source
            if page_new == page_old:
                raise NoSuchElementException("没有找到{}的频道")

    def click_first_article(self):
        self.index_elem.find_first_article().click()


class AppIndexProxy:

    def __init__(self):
        self.index_handle = AppIndexHandle()

    def app_index_proxy(self, channel_name):
        self.index_handle.check_channel_option(channel_name)
        self.index_handle.click_first_article()
