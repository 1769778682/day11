from utils import Driver


# 定义对象库层的父类
class BaseMp(object):

    def __init__(self):
        self.driver = Driver.get_driver_mp()

    # 公用元素定位方法
    def find_elem(self, location):
        return self.driver.find_element(*location)


# 定义操作层父类
class MpAction(object):

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
