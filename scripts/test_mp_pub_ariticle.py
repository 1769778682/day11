import logging
import time

import pytest

import config
from script_page.mp.home_page import HomeProxy
from script_page.mp.publish_artical_page import PubProxy
from utils import Driver, is_element_exist, pub_mp_data


@pytest.mark.run(order=3)
class TestMpLogin:

    def setup_class(self):
        self.driver = Driver.get_driver_mp()
        self.proxy_home = HomeProxy()
        self.proxy_pub = PubProxy()

    def setup(self):
        self.driver.get("http://ttmp.research.itcast.cn/")

    @staticmethod
    def teardown_class():
        Driver.quit_driver_mp()

    @pytest.mark.parametrize(("ari_title", "ari_context", "option_name"), pub_mp_data("./data/mp/pub_ari_data.json"))
    def test_mp_pub(self, ari_title, ari_context, option_name):
        config.PUB_ARITCAL_TITLE = ari_title.format(time.strftime("%Y%m%d_%H%M%S"))
        logging.info("文章标题为{}".format(config.PUB_ARITCAL_TITLE))
        self.proxy_home.home_proxy()
        self.proxy_pub.pub_art(config.PUB_ARITCAL_TITLE, ari_context, option_name)
        assert is_element_exist(self.driver, "新增文章成功")
