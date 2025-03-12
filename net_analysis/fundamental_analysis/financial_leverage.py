"""submodule inancial_leverage"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewFinancialLeverageRadio:
    def __init__(
        self,
        value: float,
        asset_turnover_velocity: float,
        equity_capital_efficiency: float,
        method_name: str,
    ):
        self.value = display_locale(value)
        self.method_name = method_name.replace("_", " ").title()
        self.asset_turnover_velocity = float(asset_turnover_velocity)
        self.equity_capital_efficiency = float(equity_capital_efficiency)
        self.mess: str = "Not calculated yet"  # Αρχικοποίηση
        self.economic_benefits()  # Καλούμε τη συνάρτηση ώστε να υπολογιστεί η mess

    def economic_benefits(self) -> None:
        if self.asset_turnover_velocity > self.equity_capital_efficiency:
            self.mess = "Borrowing is beneficial: Ο δανεισμός ειναι επωφελής"
        elif self.asset_turnover_velocity == self.equity_capital_efficiency:
            self.mess = "Borrowing has no effect: Ο δανεισμός δεν ασκεί καμία επίδραση"
        else:
            self.mess = "Borrowing is harmful: Ο δανεισμός είναι επιβλαβής"

    def __str__(self) -> str:
        return f"{self.method_name}: {self.value}: {self.mess}"


class FinancialLeverageRadio:
    """
    ### Τεκμηρίωση\n
    Η κλάση δείκτη χρηματοοικονομικής μόχλευσης,\n
    ενσωματώνει όλους   εκείνους τους λογαριασμούς που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί \
        Αρχικοποιούνται ως πραγματική\
         κάτι συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    ### Documentation\n
    The Financial Leverage Radio class\
          encapsulates all those accounts that its methods use.\n
        method :
        +financial_leverage
        +economic_benefits
    """

    def __init__(
        self,
        net_profits: float,
        equity_capital: float,
        interest: int,
        tax_rate: int,
    ) -> None:
        self.net_profits = net_profits
        self.equity_capital = equity_capital
        self.interest = interest
        self.tax_rate = tax_rate
        self.equity_capital = equity_capital

    def financial_leverage(self) -> ViewFinancialLeverageRadio:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος οικονομική μόχλευση, κληρονομεί τους\
            λογαριασμούς από την FinancialLeverageRadio κλάση.\n
        ### Documentation\n
        The financial leverage method inherits \
            Accounts from the FinancialLeverageRadio class.s\n
        return:
        ### asset_turnover_velocity = \
        # self.net_profits /self.equity_capital \n
        ###  equity_capital_efficiency = \
        # (self.net_profits + self.interest*(1 - self.tax_rate)) / self.equity_capital
        ### round((asset_turnover_velocity/equity_capital_efficiency) , 2)
        """
        tax_rate = is_valid_number(self.tax_rate)
        equity_capital = is_valid_number(self.equity_capital)
        interest = is_valid_number(self.interest)
        net_profits = is_valid_number(self.net_profits)

        if (
            isinstance(tax_rate, str)
            or isinstance(equity_capital, str)
            or isinstance(interest, str)
            or isinstance(net_profits, str)
        ):
            return ViewFinancialLeverageRadio(
                0.0, 0.0, 0.0, sys._getframe(0).f_code.co_name
            )

        asset_turnover_velocity = net_profits / equity_capital
        equity_capital_efficiency = (
            net_profits + interest * (1 - tax_rate)
        ) / equity_capital

        values = round(asset_turnover_velocity / equity_capital_efficiency, 2)
        return ViewFinancialLeverageRadio(
            values,
            asset_turnover_velocity,
            equity_capital_efficiency,
            sys._getframe(0).f_code.co_name,
        )


if __name__ == "__main__":
    financialleverageRadio = FinancialLeverageRadio(
        net_profits=150000, equity_capital=200000, interest=25000, tax_rate=35
    )
    viewfinancialleverageRadio1 = financialleverageRadio.financial_leverage()
    print(viewfinancialleverageRadio1)
