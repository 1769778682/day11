import logging

import pytest
from script_page.mp.mp_page import LoginProxy
from utils import Driver, is_element_exist, get_allure_png


@pytest.mark.run(order=2)
class TestMpLogin:

    def setup_class(self):
        self.driver = Driver.get_driver_mp()
        self.proxy_login = LoginProxy()

    @staticmethod
    def teardown_class():
        Driver.quit_driver_mp()

    @pytest.mark.parametrize(("username", "code"), [("15201405167", "246810")])
    def test_mp_login(self, username, code):
        logging.info("username={},code={}".format(username,code))
        self.proxy_login.mp_login(username, code)
        get_allure_png(self.driver, "filename")
        assert is_element_exist(self.driver, "江苏传智播客")
