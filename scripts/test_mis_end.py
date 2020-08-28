import pytest

from utils import Driver


@pytest.mark.run(order=30)
class TestEnd:

    def test_mis_end(self):
        Driver.change_mis_key(True)
        Driver.quit_driver_mis()
