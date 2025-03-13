import json
import sys
import os
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewReturnTotalCapitalEmployed:
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
        net_profits: Optional[float],
        interest: Optional[float],
        total_capital: Optional[float],
        tax_rate: Optional[float],
        net_sales: Optional[float],
        net_margin: Optional[float],
        asset_velocity: Optional[float],
    ):
        self.net_profits = net_profits
        self.interest = interest
        self.total_capital = total_capital
        self.tax_rate = tax_rate
        self.net_sales = net_sales
        self.net_margin = net_margin
        self.asset_velocity = asset_velocity

    def value_total_capital(self) -> ViewReturnTotalCapitalEmployed:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αξία του συνολικού κεφαλαίου , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The total capital value method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### return: round(((self.net_profits + self.interest * (1-self.tax_rate))/self.total_capital), 8)
        """
        # καθαρα κερδη
        net_profits = is_valid_number(self.net_profits)
        # τοκοι
        interest = is_valid_number(self.interest)
        # συντελεστης  φορου
        tax_rate = is_valid_number(self.tax_rate)
        # Συνολικα κεφαλαια
        total_capital = is_valid_number(self.total_capital)

        if (
            isinstance(net_profits, str)
            or isinstance(interest, str)
            or isinstance(tax_rate, str)
            or isinstance(total_capital, str)
        ):
            return ViewReturnTotalCapitalEmployed(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((net_profits + interest * (1 - tax_rate)) / total_capital, 2)
        return ViewReturnTotalCapitalEmployed(sys._getframe(0).f_code.co_name, judge)

    def net_profit_margin(self) -> ViewReturnTotalCapitalEmployed:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος περιθώριο καθαρού κέρδους , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The net_profit_margin method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### Returns: round(((self.net_profits + self.interest*(1 - self.tax_rate))/self.net_sales), 2)
        """
        # καθαρα κερδη
        net_profits = is_valid_number(self.net_profits)
        # τοκοι
        interest = is_valid_number(self.interest)
        # συντελεστης  φορου
        tax_rate = is_valid_number(self.tax_rate)
        # Καθαρες πωλησης
        net_sales = is_valid_number(self.net_sales)

        if (
            isinstance(net_profits, str)
            or isinstance(interest, str)
            or isinstance(tax_rate, str)
            or isinstance(net_sales, str)
        ):
            return ViewReturnTotalCapitalEmployed(sys._getframe(0).f_code.co_name, 0.0)

        judge = round((net_profits + interest * (1 - tax_rate)) / net_sales, 2)
        self.net_margin = judge

        return ViewReturnTotalCapitalEmployed(sys._getframe(0).f_code.co_name, judge)

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
            return ViewReturnTotalCapitalEmployed(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(net_sales / total_capital, 2)
        self.asset_velocity = judge

        return ViewReturnTotalCapitalEmployed(sys._getframe(0).f_code.co_name, judge)

    def return_total_capital_employed(self) -> ViewReturnTotalCapitalEmployed:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος ταχυτητα κυκλοφοριας ενεργητικου , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The asset turnover velocity method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### return round((self.net_profit_margin()/self.asset_turnover_velocity()), 2)
        """
        # net_profit_margin() == self.net_margin
        net_profit_margin = is_valid_number(self.net_margin)
        # asset_turnover_velocity() == self.asset_velocity
        asset_turnover_velocity = is_valid_number(self.asset_velocity)

        if isinstance(net_profit_margin, str) or isinstance(
            asset_turnover_velocity, str
        ):
            return ViewReturnTotalCapitalEmployed(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(net_profit_margin / asset_turnover_velocity, 2)
        return ViewReturnTotalCapitalEmployed(sys._getframe(0).f_code.co_name, judge)


if __name__ == "__main__":
    grossmargin = ReturnTotalCapitalEmployed(
        net_profits=55222,
        interest=555555,
        total_capital=22555,
        tax_rate=656533,
        net_sales=15856598,
        net_margin=2127878,
        asset_velocity=212498,
    )
    viewgrossmargin = grossmargin.return_total_capital_employed()
    print(viewgrossmargin)
