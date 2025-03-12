"""Αριθμοδείκτες Ρεστότητας
description: Μετρούν το βαθμό αποτελεσματικότητας \
μιας επιχείρησης στη χρησιμοποίηση των κυκλοφοριακών περιουσιακών της στοιχείων,\
και στη διαχείριση των βραχυχρόνιων υποχρεώσεων.
"""

__main__ = "Αριθμοδείκτες Δραστηριότητας"
__version__ = "1.0.0"
__description__ = (
    "Μετρούν το βαθμό αποτελεσματικότητας μιας επιχείρησης στη χρησιμοποίηση των κυκλοφοριακών περιουσιακών της στοιχείων,\
και στη διαχείριση των βραχυχρόνιων υποχρεώσεων."
)

import json
import sys
import os
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewActivityRadio:
    def __init__(
        self, method_name: str, judge: Optional[float], vardict: Optional[dict] = None
    ):
        self.judge = display_locale(judge)  # Μετατροπή αριθμού σε σωστή μορφή
        self.method_name = method_name.replace("_", " ").title()  # Μορφοποίηση ονόματος
        self.vardict = vardict
        self.activity_radio = self.to_dict()  # Δημιουργία λεξικού
        self.write_json_temp()  # Αποθήκευση σε JSON

    def to_dict(self):
        """Δημιουργεί το dictionary, παραλείποντας `None` values"""
        data = {"method_name": self.method_name, "judge": self.judge}

        if hasattr(self, "vardict") and self.vardict is not None:
            data["vardict"] = self.vardict

        return data

    def write_json_temp(self):
        """Αποθηκεύει το dictionary σε αρχείο JSON, χωρίς κενές τιμές"""
        with open("presentation_of_the_indices.json", mode="a") as file:
            json.dump(self.activity_radio, file, ensure_ascii=False)
            file.write("\n")

    def __str__(self) -> str:
        """Επιστρέφει μια καθαρή περιγραφή της κλάσης"""
        output = f"{self.method_name}, judge: {self.judge}"
        if self.vardict:
            output += f", vardict: {self.vardict}"

        return output


class ActivityRadio:
    def __init__(
        self,
        cost_of_goods_sold: Optional[float],
        average_stock: Optional[float],
        sale_on_credit: Optional[float],
        average_requirement: Optional[float],
        medium_term_short_term_liabilities: Optional[float],
        sourcing: Optional[float],
        net_working_capital: Optional[float],
        net_sales: Optional[float],
        total_assets: Optional[float],
        net_assets: Optional[float],
        invested_capital: Optional[float],
        net_profit: Optional[float],
        equity_capital: Optional[float],
        days: Optional[int] = 365,
    ) -> None:
        self.cost_of_goods_sold = cost_of_goods_sold
        self.average_stock = average_stock
        self.days = days
        self.sale_on_credit = sale_on_credit
        self.average_requirement = average_requirement
        self.medium_term_short_term_liabilities = medium_term_short_term_liabilities
        self.sourcing = sourcing
        self.net_working_capital = net_working_capital
        self.net_sales = net_sales
        self.total_assets = total_assets
        self.net_assets = net_assets
        self.invested_capital = invested_capital
        self.net_profit = net_profit
        self.equity_capital = equity_capital

    def inventories_turnover_radio(self) -> ViewActivityRadio:
        """Aναλογία κύκλου εργασιών αποθεμάτων \
        ή Ταχύτητας κυκλοφορίας αποθεμάτων"""
        cost_of_goods_sold = is_valid_number(self.cost_of_goods_sold)
        average_stock = is_valid_number(self.average_stock)

        if isinstance(cost_of_goods_sold, str) or isinstance(average_stock, str):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(cost_of_goods_sold / average_stock, 2)
        return ViewActivityRadio(sys._getframe(0).f_code.co_name, judge)

    def average_demand_period(self) -> ViewActivityRadio:
        "Μέσος χρόνος Εισπραξης Απαιτήσεων"
        days = is_valid_number(self.days)
        average_requirement = is_valid_number(self.average_requirement)
        sale_on_credit = is_valid_number(self.sale_on_credit)
        if (
            isinstance(days, (str))
            or isinstance(average_requirement, (str))
            or isinstance(sale_on_credit, (str))
        ):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(((days * average_requirement) / sale_on_credit), 2)
        return ViewActivityRadio(
            sys._getframe(0).f_code.co_name,
            judge,
        )

    def trade_creditors_to_purchases_ratio(self) -> ViewActivityRadio:
        """Ταχύτητα  εξόφλησης Βραχυπρόθεσμων  υποχρεώσεων"""
        sourcing = is_valid_number(self.sourcing)
        medium_term_short_term_liabilities = is_valid_number(
            self.medium_term_short_term_liabilities
        )
        if isinstance(sourcing, (str)) or isinstance(
            medium_term_short_term_liabilities, (str)
        ):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(sourcing / (medium_term_short_term_liabilities / 12), 2)

        return ViewActivityRadio(sys._getframe(0).f_code.co_name, judge)

    def average_repayment_period_of_short_term_liabilities(self) -> ViewActivityRadio:
        """Μέσος χρόνος εξόφλησης Βραχυπρόθεσμων υποχρεώσεων"""
        days = is_valid_number(self.days)
        sourcing = is_valid_number(self.sourcing)
        medium_term_short_term_liabilities = is_valid_number(
            self.medium_term_short_term_liabilities
        )
        if (
            isinstance(days, (str))
            or isinstance(sourcing, (str))
            or isinstance(medium_term_short_term_liabilities, (str))
        ):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(((medium_term_short_term_liabilities / 12) * days) / sourcing, 2)

        return ViewActivityRadio(sys._getframe(0).f_code.co_name, judge)

    def net_working_capital_turnover_speed(self) -> ViewActivityRadio:
        """Ταχύτητα Κυκλοφορία Καθαρού Κεφαλαίου Κίνησης"""
        net_sales = is_valid_number(self.net_sales)
        net_working_capital = is_valid_number(self.net_working_capital)
        if isinstance(net_sales, (str)) or isinstance(net_working_capital, (str)):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((net_sales / net_working_capital), 2)
        return ViewActivityRadio(sys._getframe(0).f_code.co_name, judge)

    def turnover_speed_total_assets(self) -> ViewActivityRadio:
        """Ταχύτητα Κυκλοφορίας Συνολικού Ενεργητικού"""
        net_sales = is_valid_number(self.net_sales)
        total_assets = is_valid_number(self.total_assets)
        if isinstance(net_sales, (str)) or isinstance(total_assets, (str)):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((net_sales / total_assets), 2)
        return ViewActivityRadio(sys._getframe(0).f_code.co_name, judge)

    def assets_turnover_ratio(self) -> ViewActivityRadio:
        """Ταχύτητα Κυκλοφορίας Συνολικού Ενεργητικού"""
        net_sales = is_valid_number(self.net_sales)
        total_assets = is_valid_number(self.total_assets)
        if isinstance(net_sales, (str)) or isinstance(total_assets, (str)):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((net_sales / total_assets), 2)
        return ViewActivityRadio(sys._getframe(0).f_code.co_name, judge)

    def fixed_assets_turnover_ratio(self) -> ViewActivityRadio:
        """Ταχύτητα Κυκλοφορίας Παγίων"""
        net_sales = is_valid_number(self.net_sales)
        net_assets = is_valid_number(self.net_assets)
        if isinstance(net_sales, (str)) or isinstance(net_assets, (str)):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((net_sales / net_assets), 2)
        return ViewActivityRadio(sys._getframe(0).f_code.co_name, judge)

    def long_term_liabilities_turnover_ratio(self) -> ViewActivityRadio:
        """Ταχύτητα κυκλοφορίας απασχολούμενου  κεφαλαίου"""
        net_sales = is_valid_number(self.net_sales)
        invested_capital = is_valid_number(self.invested_capital)
        if isinstance(net_sales, (str)) or isinstance(invested_capital, (str)):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((net_sales / invested_capital), 2)
        return ViewActivityRadio(sys._getframe(0).f_code.co_name, judge)

    def owners_equity_turnover_ratio(self) -> ViewActivityRadio:
        """Ταχύτητα κυκλοφορίας ιδίων κεφαλαίων"""
        net_sales = is_valid_number(self.net_sales)
        equity_capital = is_valid_number(self.equity_capital)
        if isinstance(net_sales, (str)) or isinstance(equity_capital, (str)):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((net_sales / equity_capital), 2)
        return ViewActivityRadio(sys._getframe(0).f_code.co_name, judge)

    def business_cycle(self) -> ViewActivityRadio:
        """Λειτουργικός κύκλος"""

        def average_dwell_time_of_inventory_in_the_warehouse() -> float:
            """Mέσος χρόνος παραμονής του αποθέματος στην αποθήκη"""
            days = is_valid_number(self.days)
            average_stock = is_valid_number(self.average_stock)
            cost_of_goods_sold = is_valid_number(self.cost_of_goods_sold)
            if (
                isinstance(days, (str))
                or isinstance(average_stock, (str))
                or isinstance(cost_of_goods_sold, (str))
            ):
                return 0.0

            judge = round(((days * average_stock) / cost_of_goods_sold), 2)
            return judge

        def speed_of_collection_of_receivables() -> float:
            """Ταχύτητα είσπραξης των απαιτήσεων"""
            sale_on_credit = is_valid_number(self.sale_on_credit)
            average_requirement = is_valid_number(self.average_requirement)
            if isinstance(sale_on_credit, (str)) or isinstance(
                average_requirement, (str)
            ):
                return 0.0

            judge = round((sale_on_credit / average_requirement), 2)
            return judge

        warehouse_avg_time = average_dwell_time_of_inventory_in_the_warehouse()

        receivables_collection_time = speed_of_collection_of_receivables()

        if isinstance(warehouse_avg_time, (str)) or isinstance(
            receivables_collection_time, (str)
        ):
            return ViewActivityRadio(sys._getframe(0).f_code.co_name, 0.0)
        more = {
            "warehouse_avg_time": warehouse_avg_time,
            "receivables_collection_time": receivables_collection_time,
        }
        total_cycle = round((warehouse_avg_time + receivables_collection_time), 2)
        return ViewActivityRadio(sys._getframe(0).f_code.co_name, total_cycle, more)


if __name__ == "__main__":
    activityradio = ActivityRadio(
        cost_of_goods_sold=500,
        average_stock=800,
        sale_on_credit=9000,
        average_requirement=833,
        medium_term_short_term_liabilities=80000,
        sourcing=105000,
        net_working_capital=80058,
        net_sales=100000,
        total_assets=120000,
        net_assets=500000,
        invested_capital=8000,
        net_profit=500000,
        equity_capital=100000,
    )

    viewactivityradio1 = activityradio.owners_equity_turnover_ratio()

    print(viewactivityradio1, sep="\n")
