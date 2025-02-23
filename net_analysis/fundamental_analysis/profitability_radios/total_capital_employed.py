import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.setting.return_func_error import validate_numerical_inputs
from net_analysis.setting.number_output_formatting import display_locale


class ReturnTotalCapitalEmployed:
    """
    ### Τεκμηρίωση\n
    Η κλάση Επιστρέψτε το συνολικό κεφάλαιο,\n\n
    ενσωματώνει όλους   εκείνους τους λογαριασμούς\n\n
    που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί  Αρχικοποιούνται ως πραγματική κάτι\n\n
    συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    Για να αντιμετωπίσουμε πιθανό σφάλματα Division Error που\n\n
    αφορά διαίρεση με το 0  αρχικοποιούμε  σε τιμή ίση με  1.0\n
    και ταυτόχρονα αποκτάμε προαιρετική χρήση μεθόδων άλλα και\n\n
    επιλογή ποια ορίσματα θέλουμε.\n\n
    ### Documentation\n
    The Financial Leverage Radio class \n
    encapsulates all those accounts that its methods use.\n
    This accounts are initialized as real something \n
    common in the way of representation in accounting.\n
    To deal with possible Division Error errors related to division by 0\n
    we initialize to a value equal to 1.0\n
    and at the same time get optional use\n
    of other methods and choice of which arguments we want.
    +method :
        value_total_capital-> float
        net_profit_margin-> float
        asset_turnover_velocity-> float
        return_total_capital_employed-> float

    """

    def __init__(
        self,
        net_profits: float = 1.0,
        interest: float = 1.0,
        total_capital: float = 1.0,
        tax_rate: float = 1.0,
        net_sales: float = 1.0,
    ):
        self.net_profits = net_profits
        self.interest = interest
        self.total_capital = total_capital
        self.tax_rate = tax_rate
        self.net_sales = net_sales

    @validate_numerical_inputs
    @display_locale
    def value_total_capital(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αξία του συνολικού κεφαλαίου , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The total capital value method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### return: round(((self.net_profits + self.interest * (1-self.tax_rate))/self.total_capital), 8)
        """
        return round(
            (
                (self.net_profits + self.interest * (1 - self.tax_rate))
                / self.total_capital
            ),
            8,
        )

    @validate_numerical_inputs
    @display_locale
    def net_profit_margin(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος περιθώριο καθαρού κέρδους , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The net_profit_margin method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### Returns: round(((self.net_profits + self.interest*(1 - self.tax_rate))/self.net_sales), 2)
        """
        return round(
            ((self.net_profits + self.interest * (1 - self.tax_rate)) / self.net_sales),
            2,
        )

    @validate_numerical_inputs
    @display_locale
    def asset_turnover_velocity(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος ταχύτητα κύκλου εργασιών , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The asset turnover velocity method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### return round((self.net_sales/self.total_capital), 2)
        """
        return round((self.net_sales / self.total_capital), 2)

    @validate_numerical_inputs
    @display_locale
    def return_total_capital_employed(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος ταχυτητα κυκλοφοριας ενεργητικου , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n
        ### Documentation\n
        The asset turnover velocity method inherits Accounts from the ReturnTotalCapitalEmployed class.\n
        ### return round((self.net_profit_margin()/self.asset_turnover_velocity()), 2)
        """
        return round((self.net_profit_margin() / self.asset_turnover_velocity()), 2)
