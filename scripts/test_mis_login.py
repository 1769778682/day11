import pytest
from script_page.mis.mis_login_page import MisProxyPage
from utils import Driver, is_element_exist


@pytest.mark.run(order=6)
class TestMisLogin:

    def setup_class(self):
        self.driver = Driver.get_driver_mis()
        self.login = MisProxyPage()

    # def setup_methon(self):
    #     self.driver.get("http://ttmis.research.itcast.cn/")

    @staticmethod
    def teardown_class():
        Driver.quit_driver_mis()

    @pytest.mark.parametrize(("username", "password"), [("testid", "testpwd123")])
    def test_mis_login(self, username, password):
        self.login.mis_proxy(username, password)

        assert is_element_exist(self.driver, "退出")