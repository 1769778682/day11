import unittest

import pytest

from script_page.app.app_index_page import AppIndexProxy
from utils import Driver, is_element_by_attribute
from parameterized import parameterized


@pytest.mark.run(order=9)
class TestAPPIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver_app()
        cls.index_proxy = AppIndexProxy()

    def setUp(self) -> None:
        self.driver.start_activity("com.itcast.toutiaoApp", ".MainActivity")

    @classmethod
    def tearDownClass(cls):
        Driver.quit_driver_app()

    @parameterized.expand(["架构", "go"])
    def test_app_article(self, channel_name):
        self.index_proxy.app_index_proxy(channel_name)
        self.assertTrue(is_element_by_attribute(self.driver, "text", "已关注"))
