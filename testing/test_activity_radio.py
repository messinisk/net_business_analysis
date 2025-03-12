import pytest
from net_analysis.fundamental_analysis.activityradios import (
    ActivityRadio,
    ViewActivityRadio,
)


@pytest.mark.parametrize(
    "cost_of_goods_sold, average_stock, expected_value",
    [
        (1000, 500, 2),  # Κανονική περίπτωση
        (0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (-1000, 500, 2),  # Αρνητικό κόστος πωληθέντων
        (1000, -500, 2),  # Αρνητικό μέσο απόθεμα
        ("1000", 500, 2),  # Κόστος πωληθέντων ως συμβολοσειρά
        (1000, "500", 2),  # Μέσο απόθεμα ως συμβολοσειρά
        ("abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_inventories_turnover_radio(cost_of_goods_sold, average_stock, expected_value):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=cost_of_goods_sold,
        average_stock=average_stock,
        sale_on_credit=0,
        average_requirement=0,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=0,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=0,
    )
    result = activity_radio.inventories_turnover_radio()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "days, cost_of_goods_sold, average_stock, expected_value",
    [
        (365, 1000, 500, 71),  # Κανονική περίπτωση
        (365, 0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (365, 1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (365, -1000, 500, 730),  # Αρνητικό κόστος πωληθέντων
        (365, 1000, -500, 730),  # Αρνητικό μέσο απόθεμα
        (365, "1000", 500, 730),  # Κόστος πωληθέντων ως συμβολοσειρά
        (365, 1000, "500", 730),  # Μέσο απόθεμα ως συμβολοσειρά
        (365, "abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (365, 1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_average_dwell_time_of_inventory_in_the_warehouse(
    days, average_stock, cost_of_goods_sold, expected_value
):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=cost_of_goods_sold,
        average_stock=average_stock,
        sale_on_credit=0,
        average_requirement=0,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=0,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=days,
    )
    result = activity_radio.average_dwell_time_of_inventory_in_the_warehouse()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "sale_on_credit, average_requirement, expected_value",
    [
        (1000, 500, 2),  # Κανονική περίπτωση
        (0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (-1000, 500, 2),  # Αρνητικό κόστος πωληθέντων
        (1000, -500, 2),  # Αρνητικό μέσο απόθεμα
        ("1000", 500, 2),  # Κόστος πωληθέντων ως συμβολοσειρά
        (1000, "500", 2),  # Μέσο απόθεμα ως συμβολοσειρά
        ("abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_speed_of_collection_of_receivables(
    sale_on_credit, average_requirement, expected_value
):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=0,
        average_stock=0,
        sale_on_credit=sale_on_credit,
        average_requirement=average_requirement,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=0,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=0,
    )
    result = activity_radio.speed_of_collection_of_receivables()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "days, average_requirement, sale_on_credit, expected_value",
    [
        (365, 1000, 500, 71),  # Κανονική περίπτωση
        (365, 0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (365, 1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (365, -1000, 500, 730),  # Αρνητικό κόστος πωληθέντων
        (365, 1000, -500, 730),  # Αρνητικό μέσο απόθεμα
        (365, "1000", 500, 730),  # Κόστος πωληθέντων ως συμβολοσειρά
        (365, 1000, "500", 730),  # Μέσο απόθεμα ως συμβολοσειρά
        (365, "abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (365, 1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_average_demand_period(
    days, average_requirement, sale_on_credit, expected_value
):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=0,
        average_stock=0,
        sale_on_credit=sale_on_credit,
        average_requirement=average_requirement,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=0,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=days,
    )
    result = activity_radio.average_demand_period()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "sourcing, medium_term_short_term_liabilities, expected_value",
    [
        (1000, 500, 2),  # Κανονική περίπτωση
        (0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (-1000, 500, 2),  # Αρνητικό κόστος πωληθέντων
        (1000, -500, 2),  # Αρνητικό μέσο απόθεμα
        ("1000", 500, 2),  # Κόστος πωληθέντων ως συμβολοσειρά
        (1000, "500", 2),  # Μέσο απόθεμα ως συμβολοσειρά
        ("abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_velocity_of_current_liabilities(
    sourcing, medium_term_short_term_liabilities, expected_value
):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=0,
        average_stock=0,
        sale_on_credit=0,
        average_requirement=0,
        medium_term_short_term_liabilities=medium_term_short_term_liabilities,
        sourcing=sourcing,
        net_working_capital=0,
        net_sales=0,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=0,
    )
    result = activity_radio.velocity_of_current_liabilities()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "days, sourcing, medium_term_short_term_liabilities, expected_value",
    [
        (365, 1000, 500, 182),  # Κανονική περίπτωση
        (365, 0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (365, 1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (365, -1000, 500, 182),  # Αρνητικό κόστος πωληθέντων
        (365, 1000, -500, 182),  # Αρνητικό μέσο απόθεμα
        (365, "1000", 500, 182),  # Κόστος πωληθέντων ως συμβολοσειρά
        (365, 1000, "500", 182),  # Μέσο απόθεμα ως συμβολοσειρά
        (365, "abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (365, 1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_average_repayment_period_of_short_term_liabilities(
    days, sourcing, medium_term_short_term_liabilities, expected_value
):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=0,
        average_stock=0,
        sale_on_credit=0,
        average_requirement=0,
        medium_term_short_term_liabilities=medium_term_short_term_liabilities,
        sourcing=sourcing,
        net_working_capital=0,
        net_sales=0,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=days,
    )
    result = activity_radio.average_repayment_period_of_short_term_liabilities()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "net_sales, net_working_capital, expected_value",
    [
        (1000, 500, 2),  # Κανονική περίπτωση
        (0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (-1000, 500, 2),  # Αρνητικό κόστος πωληθέντων
        (1000, -500, 2),  # Αρνητικό μέσο απόθεμα
        ("1000", 500, 2),  # Κόστος πωληθέντων ως συμβολοσειρά
        (1000, "500", 2),  # Μέσο απόθεμα ως συμβολοσειρά
        ("abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_net_working_capital_turnover_speed(
    net_sales, net_working_capital, expected_value
):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=0,
        average_stock=0,
        sale_on_credit=0,
        average_requirement=0,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=net_working_capital,
        net_sales=net_sales,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=0,
    )
    result = activity_radio.net_working_capital_turnover_speed()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "net_sales, total_assets, expected_value",
    [
        (1000, 500, 2),  # Κανονική περίπτωση
        (0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (-1000, 500, 2),  # Αρνητικό κόστος πωληθέντων
        (1000, -500, 2),  # Αρνητικό μέσο απόθεμα
        ("1000", 500, 2),  # Κόστος πωληθέντων ως συμβολοσειρά
        (1000, "500", 2),  # Μέσο απόθεμα ως συμβολοσειρά
        ("abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def turnover_speed_total_assets(net_sales, total_assets, expected_value):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=0,
        average_stock=0,
        sale_on_credit=0,
        average_requirement=0,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=net_sales,
        total_assets=total_assets,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=0,
    )
    result = activity_radio.turnover_speed_total_assets()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "net_sales, net_assets, expected_value",
    [
        (1000, 500, 2),  # Κανονική περίπτωση
        (0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (-1000, 500, 2),  # Αρνητικό κόστος πωληθέντων
        (1000, -500, 2),  # Αρνητικό μέσο απόθεμα
        ("1000", 500, 2),  # Κόστος πωληθέντων ως συμβολοσειρά
        (1000, "500", 2),  # Μέσο απόθεμα ως συμβολοσειρά
        ("abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_fixed_turnover_rate(net_sales, net_assets, expected_value):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=0,
        average_stock=0,
        sale_on_credit=0,
        average_requirement=0,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=net_sales,
        total_assets=0,
        net_assets=net_assets,
        invested_capital=0,
        net_profit=0,
        days=0,
    )
    result = activity_radio.fixed_turnover_rate()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "net_sales, invested_capital, expected_value",
    [
        (1000, 500, 2),  # Κανονική περίπτωση
        (0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (-1000, 500, 2),  # Αρνητικό κόστος πωληθέντων
        (1000, -500, 2),  # Αρνητικό μέσο απόθεμα
        ("1000", 500, 2),  # Κόστος πωληθέντων ως συμβολοσειρά
        (1000, "500", 2),  # Μέσο απόθεμα ως συμβολοσειρά
        ("abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_speed_of_circulating_invested_capital(
    net_sales, invested_capital, expected_value
):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=0,
        average_stock=0,
        sale_on_credit=0,
        average_requirement=0,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=net_sales,
        total_assets=0,
        net_assets=0,
        invested_capital=invested_capital,
        net_profit=0,
        days=0,
    )
    result = activity_radio.speed_of_circulating_invested_capital()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


@pytest.mark.parametrize(
    "net_sales, net_profit, expected_value",
    [
        (1000, 500, 2),  # Κανονική περίπτωση
        (0, 500, 0),  # Μηδενικό κόστος πωληθέντων
        (1000, 0, 0),  # Μηδενικό μέσο απόθεμα
        (-1000, 500, 2),  # Αρνητικό κόστος πωληθέντων
        (1000, -500, 2),  # Αρνητικό μέσο απόθεμα
        ("1000", 500, 2),  # Κόστος πωληθέντων ως συμβολοσειρά
        (1000, "500", 2),  # Μέσο απόθεμα ως συμβολοσειρά
        ("abc", 500, 0),  # Μη έγκυρη συμβολοσειρά για κόστος πωληθέντων
        (1000, "abc", 0),  # Μη έγκυρη συμβολοσειρά για μέσο απόθεμα
    ],
)
def test_traffic_speed_net_profit(net_sales, net_profit, expected_value):
    activity_radio = ActivityRadio(
        cost_of_goods_sold=0,
        average_stock=0,
        sale_on_credit=0,
        average_requirement=0,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=net_sales,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=net_profit,
        days=0,
    )
    result = activity_radio.traffic_speed_net_profit()
    assert isinstance(result, ViewActivityRadio)
    assert result != expected_value


def test_business_cycle():
    obj = ActivityRadio(
        cost_of_goods_sold=500,
        average_stock=1500,
        sale_on_credit=5000,
        average_requirement=1200,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=0,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=365,
    )
    obj.average_dwell_time_of_inventory_in_the_warehouse = lambda: 1095
    obj.speed_of_collection_of_receivables = lambda: 4

    result = obj.business_cycle()
    assert result.value == "1.099,00"


def test_business_cycle_invalid():
    obj = ActivityRadio(
        cost_of_goods_sold=500,
        average_stock=1500,
        sale_on_credit=5000,
        average_requirement=1200,
        medium_term_short_term_liabilities=0,
        sourcing=0,
        net_working_capital=0,
        net_sales=0,
        total_assets=0,
        net_assets=0,
        invested_capital=0,
        net_profit=0,
        days=365,
    )
    obj.average_dwell_time_of_inventory_in_the_warehouse = lambda: "error"
    obj.speed_of_collection_of_receivables = lambda: 4

    result = obj.business_cycle()
    assert result.value == "0,00"
