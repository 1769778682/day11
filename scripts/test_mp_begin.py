import allure
import pytest

from utils import Driver


@pytest.mark.run(order=1)
class TestBegin:

    @allure.step(title="开始")
    def test_begin(self):
        Driver.change_mp_key(False)
