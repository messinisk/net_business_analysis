import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.fundamental_analysis.activity_radios.activityradios import (
    ActivityRadio,
)


@pytest.fixture
def activity_radio() -> ActivityRadio:
    """Fixture για τη δημιουργία μιας νέας παρουσίας του ActivityRadio."""
    return ActivityRadio(cost_of_goods_sold=5000, average_stock=15000)


class TestActivityRadio:
    """class test"""

    # @pytest.mark.parametrize("cost_of_goods_sold, average_stock, resuil", [
    # (5000, 15000, 0.33),
    # (15000, 5000, 3.0),
    # (-15000, 5000, 3.0),
    # (15000, -5000, 3.0),
    # (-15000, -5000, 3.0)
    # ])
    @pytest.fixture
    def test_inventories_turnover_radio(
        activity_radio: ActivityRadio, cost_of_goods_sold, average_stock, resuil
    ) -> None:
        # resuil = 0.33
        assert (
            activity_radio.inventories_turnover_radio(cost_of_goods_sold, average_stock)
            == 0.33
        )
