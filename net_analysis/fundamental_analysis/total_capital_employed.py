import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewReturnTotalCapitalEmployed:
    def __init__(self, value: float, method_name: str):
        self.value = display_locale(value)
        self.method_name = method_name.replace("_", " ").title()

    def __str__(self) -> str:
        return f"{self.method_name}: {self.value}"


class ReturnTotalCapitalEmployed:
    """
    ### Τεκμηρίωση\n
    Η κλάση Επιστρέψτε το συνολικό κεφάλαιο,\n\n
    ενσωματώνει όλους   εκείνους τους λογαριασμούς\n\n
    που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί  Αρχικοποιούνται ως πραγματική κάτι\n\n
    συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    ### Documentation\n
    The Financial Leverage Radio class \n
    encapsulates all those accounts that its methods use.\n
    This accounts are initialized as real something \n
    common in the way of representation in accounting.\n
    +method :
        value_total_capital-> float
        net_profit_margin-> float
        asset_turnover_velocity-> float
        return_total_capital_employed-> float

    """

    def __init__(
        self,
        net_profits: float,
        interest: float,
        total_capital: float,
        tax_rate: float,
        net_sales: float,
    ):
        self.net_profits = net_profits
        self.interest = interest
        self.total_capital = total_capital
        self.tax_rate = tax_rate
        self.net_sales = net_sales

    def value_total_capital(self) -> ViewReturnTotalCapitalEmployed:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αξία του συνολικού κεφαλαίου , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The total capital value method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### return: round(((self.net_profits + self.interest * (1-self.tax_rate))/self.total_capital), 8)
        """
        net_profits = is_valid_number(self.net_profits)
        interest = is_valid_number(self.interest)
        tax_rate = is_valid_number(self.tax_rate)
        total_capital = is_valid_number(self.total_capital)

        if (
            isinstance(net_profits, str)
            or isinstance(interest, str)
            or isinstance(tax_rate, str)
            or isinstance(total_capital, str)
        ):
            return ViewReturnTotalCapitalEmployed(0.0, sys._getframe(0).f_code.co_name)

        values = round((net_profits + interest * (1 - tax_rate)) / total_capital, 2)
        return ViewReturnTotalCapitalEmployed(values, sys._getframe(0).f_code.co_name)

    def net_profit_margin(self) -> ViewReturnTotalCapitalEmployed:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος περιθώριο καθαρού κέρδους , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The net_profit_margin method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### Returns: round(((self.net_profits + self.interest*(1 - self.tax_rate))/self.net_sales), 2)
        """
        net_profits = is_valid_number(self.net_profits)
        interest = is_valid_number(self.interest)
        tax_rate = is_valid_number(self.tax_rate)
        net_sales = is_valid_number(self.net_sales)

        if (
            isinstance(net_profits, str)
            or isinstance(interest, str)
            or isinstance(tax_rate, str)
            or isinstance(net_sales, str)
        ):
            return ViewReturnTotalCapitalEmployed(0.0, sys._getframe(0).f_code.co_name)

        values = round((net_profits + interest * (1 - tax_rate)) / net_sales, 2)
        return ViewReturnTotalCapitalEmployed(values, sys._getframe(0).f_code.co_name)

    def asset_turnover_velocity(self) -> ViewReturnTotalCapitalEmployed:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος ταχύτητα κύκλου εργασιών , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The asset turnover velocity method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### return display_locale((self.net_sales/self.total_capital))
        """
        net_sales = is_valid_number(self.net_sales)
        total_capital = is_valid_number(self.total_capital)

        if isinstance(net_sales, str) or isinstance(total_capital, str):
            return ViewReturnTotalCapitalEmployed(0.0, sys._getframe(0).f_code.co_name)

        values = round(net_sales / total_capital, 2)
        return ViewReturnTotalCapitalEmployed(values, sys._getframe(0).f_code.co_name)

    def return_total_capital_employed(self) -> ViewReturnTotalCapitalEmployed:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος ταχυτητα κυκλοφοριας ενεργητικου , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The asset turnover velocity method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### return round((self.net_profit_margin()/self.asset_turnover_velocity()), 2)
        """
        net_profit_margin = is_valid_number(self.net_profit_margin())
        asset_turnover_velocity = is_valid_number(self.asset_turnover_velocity())

        if isinstance(net_profit_margin, str) or isinstance(
            asset_turnover_velocity, str
        ):
            return ViewReturnTotalCapitalEmployed(0.0, sys._getframe(0).f_code.co_name)

        values = round(net_profit_margin / asset_turnover_velocity, 2)
        return ViewReturnTotalCapitalEmployed(values, sys._getframe(0).f_code.co_name)
