import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewEquityCapital:
    def __init__(self, value: float, method_name: str):
        self.value = display_locale(value)
        self.method_name = method_name.replace("_", " ").title()

    def __str__(self) -> str:
        return f"{self.method_name}: {self.value}"


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

    def net_profit_margin(self) -> ViewEquityCapital:
        net_profits = is_valid_number(self.net_profits)
        net_sales = is_valid_number(self.net_sales)

        if isinstance(net_profits, str) or isinstance(net_sales, str):
            return ViewEquityCapital(0.0, sys._getframe(0).f_code.co_name)

        values = round(net_profits / net_sales, 2)
        return ViewEquityCapital(values, sys._getframe(0).f_code.co_name)

    def asset_turnover_velocity(self) -> ViewEquityCapital:
        net_sales = is_valid_number(self.net_sales)
        fixed_asset = is_valid_number(self.fixed_asset)

        if isinstance(net_sales, str) or isinstance(fixed_asset, str):
            return ViewEquityCapital(0.0, sys._getframe(0).f_code.co_name)

        values = round(net_sales / fixed_asset, 2)
        return ViewEquityCapital(values, sys._getframe(0).f_code.co_name)

    def financial_leverage(self) -> ViewEquityCapital:
        fixed_asset = is_valid_number(self.fixed_asset)
        equity_capital = is_valid_number(self.equity_capital)

        if isinstance(fixed_asset, str) or isinstance(equity_capital, str):
            return ViewEquityCapital(0.0, sys._getframe(0).f_code.co_name)

        values = round(fixed_asset / equity_capital, 2)
        return ViewEquityCapital(values, sys._getframe(0).f_code.co_name)

    def equity_multiplier(self) -> ViewEquityCapital:
        net_profit_margin = is_valid_number(self.net_profit_margin())
        asset_turnover_velocity = is_valid_number(self.asset_turnover_velocity())
        financial_leverage = is_valid_number(self.financial_leverage())
        if (
            isinstance(net_profit_margin, str)
            or isinstance(asset_turnover_velocity, str)
            or isinstance(financial_leverage, str)
        ):
            return ViewEquityCapital(0.0, sys._getframe(0).f_code.co_name)

        values = round(
            (net_profit_margin * asset_turnover_velocity) * financial_leverage, 2
        )
        return ViewEquityCapital(values, sys._getframe(0).f_code.co_name)

    def restatement_equity_multiplier(self) -> ViewEquityCapital:
        net_profits = is_valid_number(self.net_profits)
        equity_capital = is_valid_number(self.equity_capital)

        if isinstance(net_profits, str) or isinstance(equity_capital, str):
            return ViewEquityCapital(0.0, sys._getframe(0).f_code.co_name)

        values = round(net_profits / equity_capital, 2)
        return ViewEquityCapital(values, sys._getframe(0).f_code.co_name)
