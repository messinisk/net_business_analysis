"""Αριθμοδείκτες Ρεστότητας
description: Μετρούν την ικανότητα της επιχείρησης\
να ανταποκριθεί στις ληξιπρόθεσμες υποχρεώσεις της.
    """

__main__ = "Αριθμοδείκτες Ρεστότητας"
__version__ = "1.0.0"
__description__ = "Μετρούν την ικανότητα της επιχείρησης\
να ανταποκριθεί στις ληξιπρόθεσμες υποχρεώσεις της."

import json
import sys
import os
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewLiquidityRadios:
    def __init__(
        self,
        method_name: str,
        judge: Optional[float] = None,
        days: Optional[int] = None,
        quality_indicator: Optional[str] = None,
        currency: Optional[float] = None,
    ):
        self.judge = display_locale(
            judge
        )  # Διασφαλίζουμε ότι είναι float με 2 δεκαδικά
        self.method_name = method_name.replace("_", " ").title()  # Διαμόρφωση τίτλου
        self.quality_indicator = (
            quality_indicator  # Μία από τις ["good", "balance", "not good"]
        )
        self.currency = currency  # Αν υπάρχει, στρογγυλοποιούμε
        self.days = days
        self.activity_radio = self.to_dict()  # Δημιουργία λεξικού
        self.write_json_temp()  # Αποθήκευση σε JSON

    def to_dict(self):
        """Δημιουργεί το dictionary, παραλείποντας `None` values"""
        data = {"method_name": self.method_name}

        if hasattr(self, "days") and self.days is not None:
            data["days"] = self.days
        else:
            data["judge"] = self.judge
            if hasattr(self, "quality_indicator"):
                data["quality_indicator"] = self.quality_indicator
            if hasattr(self, "currency"):
                data["currency"] = self.currency

        return data

    def write_json_temp(self):
        """Αποθηκεύει το dictionary σε αρχείο JSON, χωρίς κενές τιμές"""
        with open("presentation_of_the_indices.json", mode="a") as file:
            json.dump(self.activity_radio, file, ensure_ascii=False)
            file.write("\n")

    def __str__(self) -> str:
        """Επιστρέφει μια καθαρή περιγραφή της κλάσης"""
        output = f"{self.method_name}, judge: {self.judge}"
        if self.quality_indicator:
            output += f", quality_indicator: {self.quality_indicator}"
        if self.currency:
            output += f", currency: {self.currency}"
        if self.days:
            output = f"{self.method_name}, Days: {self.days}"
        return output


class LiquidityRadios:
    """
    method :
        + net_working_capital_ratio-> ViewLiquidityRadios
        + acid_test_radio-> ViewLiquidityRadios
        + quick_radio-> ViewLiquidityRadios
        + cash_ratio-> ViewLiquidityRadios
        + defensive_interval-> ViewLiquidityRadios

    """

    def __init__(
        self,
        circulating_assets: Optional[float],
        short_term_liabilities: Optional[float],
        available_cash: Optional[float],
        stocks: Optional[float],
        requirements: Optional[float],
        cost_of_goods_sold: Optional[float],
        administrative_expenses: Optional[float],
        research_and_development_expenses: Optional[float],
        disposal_costs: Optional[float],
        financial_expenses: Optional[float],
        built_in_depreciation: Optional[float],
        days: int = 365,
    ) -> None:
        self.circulating_assets = circulating_assets
        self.short_term_liabilities = short_term_liabilities
        self.available_cash = available_cash
        self.stocks = stocks
        self.requirements = requirements
        self.cost_of_goods_sold = cost_of_goods_sold
        self.administrative_expenses = administrative_expenses
        self.research_and_development_expenses = research_and_development_expenses
        self.disposal_costs = disposal_costs
        self.financial_expenses = financial_expenses
        self.built_in_depreciation = built_in_depreciation
        self.days = days

    def net_working_capital_ratio(self) -> ViewLiquidityRadios:
        """[Καθαρό Κεφάλαιο Κίνησης, ή\n
        Αριθμοδείκτης Γενικής ή έμμεσης ρευστότητας!!
        circulating_assets == working capital radio\n
        currency:\n
        net_working_capital_ratio = circulating_assets - short_term_liabilities\n
        judge:\n
        circulating_assets / short_term_liabilities\n
        quality indicator:\n
        circulating_assets > short_term_liabilities [good]\n
        circulating_assets == short_term_liabilities [balance]\n
        circulating_assets < short_term_liabilities [not good]]"""
        effect: list[str] = ["good", "balance", "not good"]
        short_term_liabilities = is_valid_number(self.short_term_liabilities)
        circulating_assets = is_valid_number(self.circulating_assets)

        if isinstance(short_term_liabilities, str) or isinstance(
            circulating_assets, str
        ):
            return ViewLiquidityRadios(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(circulating_assets / short_term_liabilities, 2)

        days = None
        quality_indicator = (
            effect[0]
            if circulating_assets > short_term_liabilities
            else effect[1]
            if circulating_assets == short_term_liabilities
            else effect[2]
        )

        currency = round(circulating_assets - short_term_liabilities, 2)

        return ViewLiquidityRadios(
            sys._getframe(0).f_code.co_name, judge, days, quality_indicator, currency
        )

    def acid_test_radio(self) -> ViewLiquidityRadios:
        """[Άμεση ρευστότητα, Instant liquidity]"""
        circulating_assets = is_valid_number(self.circulating_assets)
        stocks = is_valid_number(self.stocks)
        short_term_liabilities = is_valid_number(self.short_term_liabilities)

        if (
            isinstance(circulating_assets, str)
            or isinstance(stocks, str)
            or isinstance(short_term_liabilities, str)
        ):
            return ViewLiquidityRadios(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((circulating_assets - stocks) / short_term_liabilities, 2)
        return ViewLiquidityRadios(sys._getframe(0).f_code.co_name, judge)

    def quick_radio(self) -> ViewLiquidityRadios:
        """[Άμεση ρευστότητα, Instant liquidity]"""
        requirements = is_valid_number(self.requirements)
        available_cash = is_valid_number(self.available_cash)
        short_term_liabilities = is_valid_number(self.short_term_liabilities)

        if (
            isinstance(requirements, str)
            or isinstance(available_cash, str)
            or isinstance(short_term_liabilities, str)
        ):
            return ViewLiquidityRadios(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((requirements + available_cash) / short_term_liabilities, 2)
        return ViewLiquidityRadios(sys._getframe(0).f_code.co_name, judge)

    def cash_ratio(self) -> ViewLiquidityRadios:
        """[Αριθμοδείκτης ταμειακής ρευστότητας,
        Cash liquidity ratio]"""
        requirements = is_valid_number(self.requirements)
        short_term_liabilities = is_valid_number(self.short_term_liabilities)

        if isinstance(requirements, str) or isinstance(short_term_liabilities, str):
            return ViewLiquidityRadios(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(requirements / short_term_liabilities, 2)
        return ViewLiquidityRadios(sys._getframe(0).f_code.co_name, judge)

    def defensive_interval(self) -> ViewLiquidityRadios:
        """[Το αμυντικό διάστημα, The defensive space]"""
        available_cash = is_valid_number(self.circulating_assets)
        requirements = is_valid_number(self.stocks)
        forecast_daily_expenses = self.forecast_daily_expenses()

        if (
            isinstance(available_cash, str)
            or isinstance(requirements, str)
            or isinstance(forecast_daily_expenses, str)
        ):
            return ViewLiquidityRadios(sys._getframe(0).f_code.co_name, 0.0)

        days = int((available_cash - requirements) // forecast_daily_expenses)
        judge = None
        return ViewLiquidityRadios(sys._getframe(0).f_code.co_name, judge, days)

    def forecast_daily_expenses(self) -> float:
        cost_of_goods_sold = is_valid_number(self.cost_of_goods_sold)
        administrative_expenses = is_valid_number(self.administrative_expenses)
        research_and_development_expenses = is_valid_number(
            self.research_and_development_expenses
        )
        disposal_costs = is_valid_number(self.disposal_costs)
        financial_expenses = is_valid_number(self.financial_expenses)
        built_in_depreciation = is_valid_number(self.built_in_depreciation)
        days = is_valid_number(self.days)

        if (
            isinstance(cost_of_goods_sold, str)
            or isinstance(administrative_expenses, str)
            or isinstance(research_and_development_expenses, str)
            or isinstance(disposal_costs, str)
            or isinstance(financial_expenses, str)
            or isinstance(built_in_depreciation, str)
            or isinstance(days, str)
        ):
            return 0.0
        values = round(
            (
                cost_of_goods_sold
                + administrative_expenses
                + research_and_development_expenses
                + disposal_costs
                + financial_expenses
                + built_in_depreciation
            )
            / days,
            2,
        )
        return values


if __name__ == "__main__":
    liquidityradios = LiquidityRadios(
        circulating_assets=119924,
        short_term_liabilities=119924,
        available_cash=95225,
        stocks=18000,
        requirements=6699,
        cost_of_goods_sold=15000,
        administrative_expenses=15000,
        research_and_development_expenses=10000,
        disposal_costs=10000,
        financial_expenses=10000,
        built_in_depreciation=10000,
    )
    viewactivityradio1 = liquidityradios.defensive_interval()
    # viewactivityradio2 = liquidityradios.quick_radio()
    print(viewactivityradio1)
