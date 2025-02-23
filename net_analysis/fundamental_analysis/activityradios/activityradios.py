"""
El:Αυτή η μονά περιλαμβάνει μεθόδους εκτιμούν
την δραστηριότητα  της επιχείρησης.
En:This single includes methods appreciate
the business activity
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.setting.return_func_error import validate_numerical_inputs
from net_analysis.setting.number_output_formatting import display_locale


class ActivityRadio:
    def __init__(
        self,
        cost_of_goods_sold: float = 1.0,
        average_stock=1.0,
        days: int = 365,
        sale_on_credit: float = 1.0,
        average_requirement: float = 1.0,
        medium_term_short_term_liabilities: float = 1.0,
        sourcing: float = 1.0,
        net_working_capital: float = 1.0,
        net_sales: float = 1.0,
        total_assets: float = 1.0,
        net_assets: float = 1.0,
        invested_capital: float = 1.0,
        net_profit: float = 1.0,
    ) -> None:
        self.cost_of_goods_sold = cost_of_goods_sold
        self.average_stock = average_stock
        self.days = days
        self.sale_on_credit = sale_on_credit
        self.average_requirement = average_requirement
        self.medium_term_short_term_liabilities = (
            medium_term_short_term_liabilities)
        self.sourcing = sourcing
        self.net_working_capital = net_working_capital
        self.net_sales = net_sales
        self.total_assets = total_assets
        self.net_assets = net_assets
        self.invested_capital = invested_capital
        self.net_profit = net_profit

    @validate_numerical_inputs
    @display_locale
    def inventories_turnover_radio(self) -> float:
        return round(self.cost_of_goods_sold / self.average_stock, 2)

    @validate_numerical_inputs
    @display_locale
    def average_dwell_time_of_inventory_in_the_warehouse(self) -> float:
        return round(
            (self.days * self.average_stock)
            /
            self.cost_of_goods_sold, 2)

    @validate_numerical_inputs
    @display_locale
    def speed_of_collection_of_receivables(self) -> float:
        return round(self.sale_on_credit / self.average_requirement, 2)

    
    @validate_numerical_inputs
    @display_locale
    def average_demand_period(self) -> float:
        return round(
            (self.days * self.average_requirement)
            /
            self.sale_on_credit, 2)

    @validate_numerical_inputs
    @display_locale
    def velocity_of_current_liabilities(self) -> float:
        return round(
            self.sourcing / self.medium_term_short_term_liabilities,
            2)

    @validate_numerical_inputs
    @display_locale
    def average_repayment_period_of_short_term_liabilities(self) -> float:
        return round(
            (self.medium_term_short_term_liabilities * self.days)
            / self.sourcing, 2)

    @validate_numerical_inputs
    @display_locale
    def net_working_capital_turnover_speed(self) -> float:
        return round(self.net_sales / self.net_working_capital, 2)

    @validate_numerical_inputs
    @display_locale
    def turnover_speed_total_assets(self) -> float:
        return round(self.net_sales / self.total_assets, 2)

    @validate_numerical_inputs
    @display_locale
    def fixed_turnover_rate(self) -> float:
        return round(self.net_sales / self.net_assets, 2)

    @validate_numerical_inputs
    @display_locale
    def speed_of_circulating_invested_capital(self) -> float:
        return round(self.net_sales / self.invested_capital, 2)

    @validate_numerical_inputs
    @display_locale
    def traffic_speed_net_profit(self) -> float:
        return round(self.net_sales / self.net_profit, 2)

    @display_locale
    def business_cycle(self) -> float:
        try:
            the_warehouse_average = (
                self.average_dwell_time_of_inventory_in_the_warehouse()
            )
            collection_of_receivables = (
                self.speed_of_collection_of_receivables())

            if the_warehouse_average > 0 and collection_of_receivables > 0:
                return round(
                    the_warehouse_average + collection_of_receivables,
                    2)
        except ZeroDivisionError:
            print("προκληθηκε ZeroDivisionError επανεξεταστε τα δεδομενα ")
            return 0.0

        return 0.0  # ✅ Προσθήκη default return για κάθε περίπτωση
