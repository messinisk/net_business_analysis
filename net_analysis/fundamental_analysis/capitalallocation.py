import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewCapitalStructure:
    def __init__(
        self,
        value: float,
        asset_turnover_velocity: float,
        equity_capital_efficiency: float,
        method_name: str,
    ):
        self.value = display_locale(value)
        self.method_name = method_name.replace("_", " ").title()

    def __str__(self) -> str:
        return f"{self.method_name}: {self.value}"


class CapitalStructure:
    """_summary_"""

    def __init__(
        self,
        total_assets: float,
        fixed: float,
        current_assets: float,
        liabilities: float,
        self_foreign: float,
        short_term_foreign_funds: float,
        long_term_foreign_capital: float,
        interest_rate: float,
        market_capitalization_of_equity: float,
        tax_rate: float,
    ):
        self.total_assets = total_assets
        self.fixed = fixed
        self.current_assets = current_assets
        self.liabilities = liabilities
        self.short_term_foreign_funds = short_term_foreign_funds
        self.long_term_foreign_capital = long_term_foreign_capital
        self.self_foreign = self_foreign
        self.interest_rate = interest_rate  # epitokio
        self.tax_rate = tax_rate  # συντελεστης φορου
        self.market_capitalization_of_equity = market_capitalization_of_equity
        self.dict = {"foreign_capital": "The total foreign capital is:"}

    def foreign_capital_ratio_calculation(self) -> ViewCapitalStructure:
        """
        Υπολογίζει το συνολικό ξένο κεφάλαιο με βάση τα short-term
        και long-term κεφάλαια, και επιστρέφει το αποτέλεσμα.
        """
        short_term_foreign_funds = is_valid_number(self.short_term_foreign_funds)
        long_term_foreign_capital = is_valid_number(self.long_term_foreign_capital)
        if isinstance(short_term_foreign_funds, (str)) or isinstance(
            long_term_foreign_capital, (str)
        ):
            return ViewCapitalStructure(0.0, sys._getframe(0).f_code.co_name)

        values = round((short_term_foreign_funds / long_term_foreign_capital), 2)
        return ViewCapitalStructure(values, sys._getframe(0).f_code.co_name)

    def total_capital(self) -> float:
        return sum([self.long_term_foreign_capital + self.short_term_foreign_funds])

    def leverage_tax_reduction(self):
        if self.short_term_foreign_funds > 1.0 and self.interest_rate > 0:
            interest = self.short_term_foreign_funds * (self.interest_rate / 100)
            incom_tax = interest * (self.tax_rate / 100)
            tax_reduction = (interest - incom_tax) / self.short_term_foreign_funds
            return f"\nshort_term_foreign_fund: {self.short_term_foreign_funds:,.2f}\
                \tinterest: {interest:,.2f}\tincom_tax: {incom_tax:,.2f}\
                \ttax_reduction: {tax_reduction:,.2%}"
        if self.long_term_foreign_capital > 1.0 and self.interest_rate > 0:
            interest = self.long_term_foreign_capital * (self.interest_rate / 100)
            incom_tax = interest * (self.tax_rate / 100)
            tax_reduction = (interest - incom_tax) / self.long_term_foreign_capital
            return f"\nshort_term_foreign_fund: {self.long_term_foreign_capital:,.2f}\
                \tinterest: {interest:,.2f}\tincom_tax: {incom_tax:,.2f}\
                \ttax_reduction: {tax_reduction:,.2%}"

    def distribution_of_assets(self):
        if self.fixed > self.current_assets:
            return "low liquidity of assets"
        if self.fixed == self.current_assets:
            return "balance"
        if self.fixed < self.current_assets:
            return "High liquidity of assets"

    def radio_of_owners_equity_to_total_assets(self):
        return f"Ιδοκτησιας {(self.self_foreign / self.total_capital()):,.2%}"

    def foreign_capital_pressure_index(self):
        return f"Πιεσης {self.foreign_capital_ratio_calculation() / self.total_capital():,.2%}"

    def radio_of_owners_equity_to_total_liavilities(self):
        return f"Δανιακης επιβαρινσης {(self.foreign_capital_ratio_calculation() / self.self_foreign):,.2%}"

    def listed_radio_of_owners_equity_to_total_liavilities(self):
        return (
            self.foreign_capital_ratio_calculation()
            / self.market_capitalization_of_equity
        )

    def asset_structure_radio(self):
        self.total_assets = self.fixed + self.current_assets

        def asset_structure_radio_a():
            if self.fixed > 1.0:
                return self.fixed / self.total_assets

        def asset_structure_radio_b():
            if self.current_assets > 1.0:
                return self.current_assets / self.total_assets

        def asset_structure_radio_c():
            return self.fixed / self.current_assets

        return f"{asset_structure_radio_a()}\n{asset_structure_radio_b()}\n{asset_structure_radio_c()}"

    def radio_of_owners_qquity_to_fixed_assets(self):
        return self.self_foreign / self.fixed
