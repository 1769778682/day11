import time

import pytest

import config
from script_page.mis.mis_auditing_page import MisProxyPage, MisHandlePage
from script_page.mis.mis_home_page import MisProxyHome
from utils import Driver, is_element_exist


@pytest.mark.run(order=7)
class TestMisAudit:

    def setup_class(self):
        self.driver = Driver.get_driver_mis()
        self.home_proxy = MisProxyHome()
        self.audit_proxy = MisProxyPage()

    def setup(self):
        self.driver.get("http://ttmis.research.itcast.cn/#/home")

    def teardown_class(self):
        Driver.quit_driver_mis()

    @pytest.mark.parametrize(('channel', 'option_name'), [('前端', '待审核')])
    def test_mis_audit(self, channel, option_name):
        self.home_proxy.mis_handle_home()
        time.sleep(7)
        self.audit_proxy.mis_audit_pass(config.PUB_ARITCAL_TITLE, channel, option_name)
        assert is_element_exist(self.driver, "驳回")

    # @pytest.mark.parametrize(('channel', 'option_name'), [('前端', '待审核')])
    # def test_mis_reject(self, channel, option_name):
    #     self.home_proxy.mis_handle_home()
    #     self.audit_proxy.mis_audit_reject(config.PUB_ARITCAL_TITLE, channel, option_name)
