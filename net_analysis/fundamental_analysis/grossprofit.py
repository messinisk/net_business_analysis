import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewGrossMargin:
    def __init__(self, value: float, method_name: str):
        self.value = display_locale(value)
        self.method_name = method_name.replace("_", " ").title()

    def __str__(self) -> str:
        return f"{self.method_name}: {self.value}"


class GrossMargin:
    """
    ### Τεκμηρίωση\n
    Η κλάση Μικτό περιθώριο,  ενσωματώνει όλους   εκείνους τους λογαριασμούς που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί  Αρχικοποιούνται ως πραγματική κάτι συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    ### Documentation\n
    The Gross Margin class encapsulates all those accounts that its methods use.\n
    This accounts are initialized as real something common in the way of representation in accounting.\n
        method :
            +gross_profit_margin
            +net_profit_margin
            +net_profits
            +return_on_equity
    """

    def __init__(
        self,
        gross_operating_profit: float,
        net_sales: float,
        net_operating_profit: float,
        sales: float,
        net_profit_of_use: float,
        total_of_these_funds: float,
    ) -> None:
        self.gross_operating_profit = gross_operating_profit
        self.net_sales = net_sales
        self.net_operating_profit = net_operating_profit
        self.sales = sales
        self.net_profit_of_use = net_profit_of_use
        self.total_of_these_funds = total_of_these_funds

    def gross_profit_margin(self) -> ViewGrossMargin:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος Μικτό περιθώριο \
            κέρδους, κληρονομεί τους λογαριασμούς από την GrossΜargin κλάση\n
        που είναι τα μικτά κέρδη \
            εκμετάλλευσης και καθαρές πωλήσεις.\n
        Στην επιστροφή της μεθόδου \
            φαίνεται ξεκάθαρα τόσο η πράξη της διαίρεσης όσο και στρογγυλοποίηση σε δυο δεκαδικά ψηφία. \n
        ### Documentation\n
        The Gross profit margin method inherits\n
        the accounts from the above \
            class which are gross operating profit and net sales.\n
        The return of the method \
            clearly shows both the act of division and rounding to two decimal places.
        ### round((self.gross_operating_profit /self.net_sales), 2)\n
        """
        gross_operating_profit = is_valid_number(self.gross_operating_profit)
        net_sales = is_valid_number(self.net_sales)

        if isinstance(gross_operating_profit, str) or isinstance(net_sales, str):
            return ViewGrossMargin(0.0, sys._getframe(0).f_code.co_name)

        values = round(gross_operating_profit / net_sales, 2)
        return ViewGrossMargin(values, sys._getframe(0).f_code.co_name)

    def net_profit_margin(self) -> ViewGrossMargin:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος περιθώριο καθαρού κέρδους,\n
        κληρονομεί τους λογαριασμούς\
            από την GrossΜargin κλάση\n
        που είναι τα  καθαρά κέρδη \
            εκμετάλλευσης και  καθαρές πωλήσεις.\n
        Στην επιστροφή της μεθόδου\
              φαίνεται ξεκάθαρα  τόσο η πράξη  της διαίρεσης\n
        όσο και στρογγυλοποίηση σε\
            δυο δεκαδικά ψηφία.\n
        ### Documentation\n
        The net profit margin method inherits\n
        the accounts from the above \
            class which are net operating profit and net sales.\n
        The return of the method \
            clearly shows both \
                the division operation and rounding to two decimal places.\n
        round((self.net_operating_profit / self.net_sales), 2)
        """
        net_operating_profit = is_valid_number(self.net_operating_profit)
        net_sales = is_valid_number(self.net_sales)

        if isinstance(net_operating_profit, str) or isinstance(net_sales, str):
            return ViewGrossMargin(0.0, sys._getframe(0).f_code.co_name)

        values = round(net_operating_profit / net_sales, 2)
        return ViewGrossMargin(values, sys._getframe(0).f_code.co_name)

    def net_profits(self) -> ViewGrossMargin:
        """
        Τεκμηρίωση\n
        Η μέθοδος καθαρά κέρδη,\n
        κληρονομεί τους λογαριασμούς από την GrossΜargin κλάση\n
        που είναι το   περιθώριο \
            καθαρού κέρδους και  πωλήσεις.\n
        Στην επιστροφή της μεθόδου \
            φαίνεται πράξη ενός μεγέθους πωλήσεις\n
        πολλαπλασιαζόμενο με την \
            προηγούμενη μέθοδος περιθώριο καθαρού κέρδους \n
        ενώ δεν παραλείπουμε να\
              υποχρεώσουμε το αποτελέσματα να \
                στρογγυλοποίηση σε δυο δεκαδικά ψηφία.\n
        Documentation\n
        The net profit method inherits \
            the accounts from the above class which\
                  are net profit margin and sales.\n
        In the return of the method, \
            an act of a sales size multiplied by the\
                  previous method net profit margin is shown,\n
        while we do not fail to oblige the \
            results to be rounded to two decimal places.\n
        ### round((self.sales * self.net_profit_margin()), 2)
        """
        sales = is_valid_number(self.sales)
        net_profit_margin = is_valid_number(self.net_profit_margin())

        if isinstance(sales, str) or isinstance(net_profit_margin, str):
            return ViewGrossMargin(0.0, sys._getframe(0).f_code.co_name)

        values = round(sales * net_profit_margin, 2)
        return ViewGrossMargin(values, sys._getframe(0).f_code.co_name)

    def return_on_equity(self) -> ViewGrossMargin:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος  απόδοση ιδίων κεφαλαίων,\n
        κληρονομεί τους λογαριασμούς από την GrossΜargin κλάση\n
        που είναι τα  καθαρό κέρδος χρήσης και \
              συνολικά ιδων κεφαλαίων.\n
        Στην επιστροφή της μεθόδου φαίνεται\
              ξεκάθαρα  τόσο η πράξη  της διαίρεσης\n
        όσο και στρογγυλοποίηση σε δυο δεκαδικά ψηφία.\n
        ### Documentation\n
        The return on equity method inherits\n
        the accounts from the above class which\
              are net_profit_of_use and total_of_these_funds.\n
        The return of the method clearly shows\
              both the division operation and rounding to two decimal places.\n
        ### round((self.net_profit_of_use / self.total_of_these_funds), 2)
        """
        net_profit_of_use = is_valid_number(self.net_profit_of_use)
        total_of_these_funds = is_valid_number(self.total_of_these_funds)

        if isinstance(net_profit_of_use, str) or isinstance(total_of_these_funds, str):
            return ViewGrossMargin(0.0, sys._getframe(0).f_code.co_name)

        values = round(net_profit_of_use / total_of_these_funds, 2)
        return ViewGrossMargin(values, sys._getframe(0).f_code.co_name)
