import time

from utils import Driver


# 定义对象库层的父类
class BaseMis(object):

    def __init__(self):
        self.driver = Driver.get_driver_mis()

    # 公用元素定位方法
    def find_elem(self, location):
        return self.driver.find_element(*location)


# 定义操作层父类
class MisAction(object):

    def input_text(self, element, text):
        element.clear()
        time.sleep(1)
        element.send_keys(text)
