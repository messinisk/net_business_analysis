import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.fundamental_analysis.activityradios.activityradios import ActivityRadio



@pytest.fixture
def sample_metrics():
    return ActivityRadio(
        cost_of_goods_sold=1000, average_stock=200,
        days=365, sale_on_credit=5000, average_requirement=250,
        sourcing=3000, medium_term_short_term_liabilities=600,
        net_sales=12000, net_working_capital=400,
        total_assets=15000, net_assets=5000,
        invested_capital=7000, net_profit=2000
    )

def test_inventories_turnover_radio(sample_metrics):
    assert sample_metrics.inventories_turnover_radio() == 5.0

def test_average_dwell_time_of_inventory_in_the_warehouse(sample_metrics):
    assert sample_metrics.average_dwell_time_of_inventory_in_the_warehouse() == 73.0

def test_speed_of_collection_of_receivables(sample_metrics):
    assert sample_metrics.speed_of_collection_of_receivables() == 20.0

def test_average_demand_period(sample_metrics):
    assert sample_metrics.average_demand_period() == 18.25

def test_velocity_of_current_liabilities(sample_metrics):
    assert sample_metrics.velocity_of_current_liabilities() == 5.0

def test_average_repayment_period_of_short_term_liabilities(sample_metrics):
    assert sample_metrics.average_repayment_period_of_short_term_liabilities() == 73.0

def test_net_working_capital_turnover_speed(sample_metrics):
    assert sample_metrics.net_working_capital_turnover_speed() == 30.0

def test_turnover_speed_total_assets(sample_metrics):
    assert sample_metrics.turnover_speed_total_assets() == 0.8

def test_fixed_turnover_rate(sample_metrics):
    assert sample_metrics.fixed_turnover_rate() == 2.4

def test_speed_of_circulating_invested_capital(sample_metrics):
    assert sample_metrics.speed_of_circulating_invested_capital() == 1.71

def test_traffic_speed_net_profit(sample_metrics):
    assert sample_metrics.traffic_speed_net_profit() == 6.0

def test_business_cycle(sample_metrics):
    assert sample_metrics.business_cycle() == 93.0

