import pytest
from utils import Driver


@pytest.mark.run(order=5)
class TestBegin:

    def test_begin(self):
        Driver.change_mis_key(False)
