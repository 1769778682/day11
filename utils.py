import json
import logging
import time

import allure
import selenium.webdriver
import appium.webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Driver(object):
    __driver_mp = None
    __driver_mis = None
    __driver_app = None
    __mp_key = True
    __mis_key = True

    @classmethod
    def get_driver_mp(cls):
        if cls.__driver_mp is None:
            cls.__driver_mp = selenium.webdriver.Chrome()
            cls.__driver_mp.maximize_window()  # 窗口最大化
            cls.__driver_mp.implicitly_wait(30)  # 隐式等待
            cls.__driver_mp.get("http://ttmp.research.itcast.cn/")
        return cls.__driver_mp

    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    @classmethod
    def quit_driver_mp(cls):
        if cls.__driver_mp is not None and cls.__mp_key:
            time.sleep(3)
            cls.__driver_mp.quit()
            cls.__driver_mp = None

    @classmethod
    def get_driver_mis(cls):
        if cls.__driver_mis is None:
            cls.__driver_mis = selenium.webdriver.Chrome()
            cls.__driver_mis.maximize_window()  # 窗口最大化
            cls.__driver_mis.implicitly_wait(30)  # 隐式等待
            cls.__driver_mis.get("http://ttmis.research.itcast.cn/")
        return cls.__driver_mis

    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    @classmethod
    def quit_driver_mis(cls):
        if cls.__driver_mis is not None and cls.__mis_key:
            time.sleep(3)
            cls.__driver_mis.quit()
            cls.__driver_mis = None

    @classmethod
    def get_driver_app(cls):
        if cls.__driver_app is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.itcast.toutiaoApp'
            desired_caps['appActivity'] = '.MainActivity'
            desired_caps['noReset'] = True
            cls.__driver_app = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            cls.__driver_app.implicitly_wait(30)
        return cls.__driver_app

    @classmethod
    def quit_driver_app(cls):
        if cls.__driver_app is not None:
            time.sleep(3)
            cls.__driver_app.quit()
            cls.__driver_app = None


# 根据文本判断元素是否存在的公用方法
def is_element_exist(driver, text):
    # 定位元素的xpath表达式
    str_xpath = "//*[contains(text(), '{}')]".format(text)
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        logging.error(NoSuchElementException("找不到{}".format(text)))
        return False


def is_element_by_attribute(driver, att_name, att_value):
    # 定位元素的xpath表达式
    str_xpath = "//*[contains(@{}, '{}')]".format(att_name, att_value)
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        logging.error(NoSuchElementException("找不到{}".format(att_name)))
        return False


# 公用下拉框选择方法
def check_channel(driver, channel_name, option_name):
    str_xpath = "//*[contains(@placeholder,'{}')]".format(channel_name)
    driver.find_element_by_xpath(str_xpath).click()
    # 获取所有选项的频道名称
    list_elem = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    is_suc = False
    # 对获取的频道名称进行遍历
    for i in list_elem:
        # 如果文本信息相等则点击，跳出
        if i.text == option_name:
            i.click()
            is_suc = True
            break
        # 如果不相等，则鼠标悬停当前元素,键盘点击向下
        else:
            action = ActionChains(driver)
            action.move_to_element(i).send_keys(Keys.DOWN).perform()
            is_suc = False
    # 判断标识符is_suc是否为False，如果是则抛出异常
    if is_suc is False:
        NoSuchElementException("没有找到{}元素".format(option_name))


# 获取json文件信息
def pub_mp_data(file_data):
    list_data = []
    with open(file_data, encoding="utf_8") as f:
        mp_data = json.load(f)
        for i in mp_data.values():
            list_data.append(list(i.values()))
            print(list_data)
    return list_data


def get_allure_png(driver, filename):
    allure.attach(driver.get_screenshot_as_png(), filename, allure.attachment_type.PNG)
