import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from net_analysis.setting.return_func_error import validate_numerical_inputs
from net_analysis.setting.return_func_error import number_output_formatting


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
        net_profits: float = 1.0,
        net_sales: float = 1.0,
        fixed_asset: float = 1.0,
        equity_capital: float = 1.0,
    ) -> None:
        self.net_profits = net_profits
        self.net_sales = net_sales
        self.fixed_asset = fixed_asset
        self.equity_capital = equity_capital


    @validate_numerical_inputs
    @number_output_formatting
    def net_profit_margin(self) -> float:
        return round((self.net_profits / self.net_sales), 2)

    @validate_numerical_inputs
    @number_output_formatting
    def asset_turnover_velocity(self) -> float:
        return round((self.net_sales / self.fixed_asset), 2)

    @validate_numerical_inputs
    @number_output_formatting
    def financial_leverage(self) -> float:
        return round((self.fixed_asset / self.equity_capital), 2)

    @validate_numerical_inputs
    @number_output_formatting
    def equity_multiplier(self) -> float:
        return round(
            (
                self.net_profit_margin()
                * self.asset_turnover_velocity()
                * self.financial_leverage()
            ),
            2,
        )

    @validate_numerical_inputs
    @number_output_formatting
    def restatement_equity_multiplier(self) -> float:
        return round((self.net_profits / self.equity_capital), 2)
