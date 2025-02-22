"""submodule inancial_leverage"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.return_func_error import validate_numerical_inputs


class FinancialLeverageRadio:
    """
    ### Τεκμηρίωση\n
    Η κλάση δείκτη χρηματοοικονομικής μόχλευσης,\n
    ενσωματώνει όλους   εκείνους τους λογαριασμούς που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί \
        Αρχικοποιούνται ως πραγματική\
         κάτι συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    Για να αντιμετωπίσουμε πιθανό σφάλματα \
        Division Error που αφορά διαίρεση με το 0  αρχικοποιούμε  σε τιμή ίση με  1.0\n
    και ταυτόχρονα αποκτάμε προαιρετική χρήση\
          μεθόδων άλλα και  επιλογή ποια ορίσματα θέλουμε.\n\n
    ### Documentation\n
    The Financial Leverage Radio class\
          encapsulates all those accounts that its methods use.\n
    This accounts are initialized as real\
          something common in the way of representation in accounting.\n
    To deal with possible Division Error \
        errors related to division by 0 \
            we initialize to a value equal to 1.0\n
    and at the same time get optional use of\
          other methods and choice of which arguments we want.
    method :
        +financial_leverage
        +economic_benefits
    """

    def __init__(
        self,
        net_profits: float = 1.0,
        equity_capital: float = 1.0,
        interest: int = 1,
        tax_rate: int = 1,
    ) -> None:
        self.net_profits = net_profits
        self.equity_capital = equity_capital
        self.interest = interest
        self.tax_rate = tax_rate
        self.equity_capital = equity_capital

    @validate_numerical_inputs
    def financial_leverage(self):
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
        asset_turnover_velocity = self.net_profits / (self.equity_capital or 1.0)
        equity_capital_efficiency = (
            self.net_profits + self.interest * (1 - self.tax_rate)
        ) / (self.equity_capital or 1.0)
        if equity_capital_efficiency == 0:
            return 0  # Εναλλακτικά, μπορείτε να επιστρέψετε ένα μήνυμα
        return round((asset_turnover_velocity / equity_capital_efficiency), 2)

    def economic_benefits(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος επωφελείστε οικονομικά, \
            κληρονομεί τους λογαριασμούς από την FinancialLeverageRadio κλάση\n
        Ουσιαστικά πραγματοποιείτε τρις \
            διαφορετική λογική έλεγχοι σύγκριση με μέθοδο οικονομική μόχλευση\n
        που επιδιώκουμε να υπολογίσουμε \
            το μέγεθος εδώ επιδιώκουμε καθορίζουμε\n
        αν σύνθεση επιλεγομένων λογαριασμών \
            έχουν κάποια θετική, ουδέτερη ή αρνητική επίδραση.\n
        ### Documentation\n
        The The you benefit financiall method inherits \
            Accounts from the FinancialLeverageRadio class.
        Essentially you carry out three different \
            logical checks compared with the method
        of financial leverage that we seek \
            to calculate the size here we seek to determine whether
        the composition of selected accounts have any positive, neutral or negative effect.
        """
        asset_turnover_velocity = self.net_profits / (self.equity_capital or 1.0)
        equity_capital_efficiency = (
            self.net_profits + self.interest * (1 - self.tax_rate)
        ) / (self.equity_capital or 1.0)

        # ΣΥΝΘΗΚΕΣ
        if asset_turnover_velocity > equity_capital_efficiency:
            return "Borrowing is beneficial: Ο δανεισμός ειναι επωφελής "
        elif asset_turnover_velocity == equity_capital_efficiency:
            return "Borrowing has no effect:\
                Ο δανεισμός δεν ασκεί καμία επίδραση "
        else:
            return "Borrowing is harmful: Ο δανεισμός είναι επιβλαβής "
