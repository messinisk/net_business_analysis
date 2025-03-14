import json
import sys
import os
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewEquityCapital:
    def __init__(
        self,
        method_name: str,
        judge: Optional[float] = None,
    ):
        self.judge = display_locale(
            judge
        )  # Διασφαλίζουμε ότι είναι float με 2 δεκαδικά
        self.method_name = method_name.replace("_", " ").title()  # Διαμόρφωση τίτλου
        self.activity_radio = self.to_dict()  # Δημιουργία λεξικού
        self.write_json_temp()  # Αποθήκευση σε JSON

    def to_dict(self):
        """Δημιουργεί το dictionary, παραλείποντας `None` values"""
        data = {"method_name": self.method_name, "judge": self.judge}
        return data

    def write_json_temp(self):
        """Αποθηκεύει το dictionary σε αρχείο JSON, χωρίς κενές τιμές"""
        with open("presentation_of_the_indices.json", mode="a") as file:
            json.dump(self.activity_radio, file, ensure_ascii=False)
            file.write("\n")

    def __str__(self) -> str:
        """Επιστρέφει μια καθαρή περιγραφή της κλάσης"""
        output = f"{self.method_name}, judge: {self.judge}"
        return output


class EquityCapital:
    """
    ### Τεκμηρίωση\n
    Η κλάση Μικτό περιθώριο,  ενσωματώνει όλους   εκείνους τους λογαριασμούς \
        που χρησιμοποιούν οι μέθοδοι του.\n
    ### Documentation\n\
    The Gross Margin class encapsulates all\
        those accounts that its methods use.\n
    This accounts are initialized as real something common in the way of \
        representation in accounting.\n
    method :
        +net_profit_margin
        +asset_turnover_velocity
        +financial_leverage
        +equity_multiplier
        +Restatement_equity_multiplier
    """

    def __init__(
        self,
        net_profits: float,
        net_sales: float,
        fixed_asset: float,
        equity_capital: float,
    ) -> None:
        self.net_profits = net_profits
        self.net_sales = net_sales
        self.fixed_asset = fixed_asset
        self.equity_capital = equity_capital
        self.netprofitmargin:float = 0.0
        self.assetturnovervelocity:float = 0.0
        self.financialleverage:float = 0.0

    def net_profit_margin(self) -> ViewEquityCapital:
        net_profits = is_valid_number(self.net_profits)
        net_sales = is_valid_number(self.net_sales)

        if isinstance(net_profits, str) or isinstance(net_sales, str):
            return ViewEquityCapital(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(net_profits / net_sales, 2)
        self.netprofitmargin = judge
        return ViewEquityCapital(sys._getframe(0).f_code.co_name, judge)

    def asset_turnover_velocity(self) -> ViewEquityCapital:
        net_sales = is_valid_number(self.net_sales)
        fixed_asset = is_valid_number(self.fixed_asset)

        if isinstance(net_sales, str) or isinstance(fixed_asset, str):
            return ViewEquityCapital(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(net_sales / fixed_asset, 2)
        self.assetturnovervelocity = judge
        return ViewEquityCapital(sys._getframe(0).f_code.co_name, judge)

    def financial_leverage(self) -> ViewEquityCapital:
        fixed_asset = is_valid_number(self.fixed_asset)
        equity_capital = is_valid_number(self.equity_capital)

        if isinstance(fixed_asset, str) or isinstance(equity_capital, str):
            return ViewEquityCapital(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(fixed_asset / equity_capital, 2)
        self.financialleverage = judge
        return ViewEquityCapital(sys._getframe(0).f_code.co_name, judge)

    def equity_multiplier(self) -> ViewEquityCapital:
        net_profit_margin = is_valid_number(self.netprofitmargin)
        asset_turnover_velocity = is_valid_number(self.assetturnovervelocity)
        financial_leverage = is_valid_number(self.financialleverage)
        if (
            isinstance(net_profit_margin, str)
            or isinstance(asset_turnover_velocity, str)
            or isinstance(financial_leverage, str)
        ):
            return ViewEquityCapital(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(
            (net_profit_margin * asset_turnover_velocity) * financial_leverage, 2
        )
        return ViewEquityCapital(sys._getframe(0).f_code.co_name, judge)

    def restatement_equity_multiplier(self) -> ViewEquityCapital:
        net_profits = is_valid_number(self.net_profits)
        equity_capital = is_valid_number(self.equity_capital)

        if isinstance(net_profits, str) or isinstance(equity_capital, str):
            return ViewEquityCapital(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(net_profits / equity_capital, 2)
        return ViewEquityCapital(sys._getframe(0).f_code.co_name, judge)
