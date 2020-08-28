import allure
import pytest

from utils import Driver


@pytest.mark.run(order=4)
class TestEnd:

    @allure.step(title="结束")
    def test_mp_end(self):
        Driver.change_mp_key(True)
        Driver.quit_driver_mp()
