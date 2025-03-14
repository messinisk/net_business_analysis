"""Αριθμοδείκτες Αποδοτιότητας
description: Η ικανότητα της επιχείρησης\
να πραγματοποιεί κέρδη!Αυτους που ενδιαφερει ειναι \
Οι μετοχοί, η διοικηση, τους πιστωτές, τις τράπεζες,\
τους επενδυτές, τους εργαζόμενους, το κράτος. 
"""

__main__ = "Αριθμοδείκτες Αποδοτιότητας"
__version__ = "1.0.0"
__description__ = "Η ικανότητα της επιχείρησης\
να πραγματοποιεί κέρδη! Αυτους που ενδιαφερει ειναι κατωθι: \
Οι μετοχοί, η διοικηση, τους πιστωτές, τις τράπεζες,\
τους επενδυτές, τους εργαζόμενους, το κράτος. "

import json
import sys
import os
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewGrossMargin:
    def __init__(
        self,
        method_name: str,
        judge: Optional[float] = None,
        days: Optional[int] = None,
        quality_indicator: Optional[str] = None,
        currency: Optional[float] = None,
    ):
        self.judge = display_locale(
            judge
        )  # Διασφαλίζουμε ότι είναι float με 2 δεκαδικά
        self.method_name = method_name.replace("_", " ").title()  # Διαμόρφωση τίτλου
        self.quality_indicator = (
            quality_indicator  # Μία από τις ["good", "balance", "not good"]
        )
        self.currency = currency  # Αν υπάρχει, στρογγυλοποιούμε
        self.days = days
        self.activity_radio = self.to_dict()  # Δημιουργία λεξικού
        self.write_json_temp()  # Αποθήκευση σε JSON

    def to_dict(self):
        """Δημιουργεί το dictionary, παραλείποντας `None` values"""
        data = {"method_name": self.method_name}

        if hasattr(self, "days") and self.days is not None:
            data["days"] = self.days
        else:
            data["judge"] = self.judge
            if hasattr(self, "quality_indicator"):
                data["quality_indicator"] = self.quality_indicator
            if hasattr(self, "currency"):
                data["currency"] = self.currency

        return data

    def write_json_temp(self):
        """Αποθηκεύει το dictionary σε αρχείο JSON, χωρίς κενές τιμές"""
        with open("presentation_of_the_indices.json", mode="a") as file:
            json.dump(self.activity_radio, file, ensure_ascii=False)
            file.write("\n")

    def __str__(self) -> str:
        """Επιστρέφει μια καθαρή περιγραφή της κλάσης"""
        output = f"{self.method_name}, judge: {self.judge}"
        if self.quality_indicator:
            output += f", quality_indicator: {self.quality_indicator}"
        if self.currency:
            output += f", currency: {self.currency}"
        if self.days:
            output = f"{self.method_name}, Days: {self.days}"
        return output


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
        gross_operating_profit: Optional[float],
        net_sales: Optional[float],
        net_operating_profit: Optional[float],
        sales: Optional[float],
        net_profit_of_use: Optional[float],
        total_of_these_funds: Optional[float],
        net_profitmargin: Optional[float] = 0,
    ) -> None:
        self.gross_operating_profit = gross_operating_profit
        self.net_sales = net_sales
        self.net_operating_profit = net_operating_profit
        self.sales = sales
        self.net_profit_of_use = net_profit_of_use
        self.total_of_these_funds = total_of_these_funds
        self.net_profitmargin = net_profitmargin

    def gross_profit_margin(self) -> ViewGrossMargin:
        """μικτά περιθώρια κέρδους\
         round(gross_operating_profit / net_sales, 2)  """
        gross_operating_profit = is_valid_number(self.gross_operating_profit)
        net_sales = is_valid_number(self.net_sales)

        if isinstance(gross_operating_profit, str) or isinstance(net_sales, str):
            return ViewGrossMargin(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(gross_operating_profit / net_sales, 2)
        return ViewGrossMargin(sys._getframe(0).f_code.co_name, judge)

    def net_profit_margin(self) -> ViewGrossMargin:
        """
        Η μέθοδος περιθώριο καθαρού κέρδους
        """
        net_operating_profit = is_valid_number(self.net_operating_profit)
        net_sales = is_valid_number(self.net_sales)

        if isinstance(net_operating_profit, str) or isinstance(net_sales, str):
            return ViewGrossMargin(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(net_operating_profit / net_sales, 2)
        self.net_profitmargin = judge
        print(self.net_profitmargin, judge)
        return ViewGrossMargin(sys._getframe(0).f_code.co_name, judge)

    def net_profits(self) -> ViewGrossMargin:
        """
        Η μέθοδος "καθαρά κέρδη"
        """
        sales = is_valid_number(self.sales)
        net_profitmargin = is_valid_number(
            self.net_profitmargin)

        if isinstance(sales, str) or isinstance(net_profitmargin, str):
            return ViewGrossMargin(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(sales * net_profitmargin, 2)
        return ViewGrossMargin(sys._getframe(0).f_code.co_name, judge)

    def return_on_equity(self) -> ViewGrossMargin:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος  απόδοση ιδίων κεφαλαίων,\n
        κληρονομεί τους λογαριασμούς από την GrossΜargin κλάση\n
        που είναι τα  καθαρό κέρδος χρήσης και \
        συνολικά ιδων κεφαλαίων.\n
        """
        net_profit_of_use = is_valid_number(self.net_profit_of_use)
        total_of_these_funds = is_valid_number(self.total_of_these_funds)

        if isinstance(net_profit_of_use, str) or isinstance(total_of_these_funds, str):
            return ViewGrossMargin(sys._getframe(0).f_code.co_name, 0.0)

        judge = round(net_profit_of_use / total_of_these_funds, 2)
        return ViewGrossMargin(sys._getframe(0).f_code.co_name, judge)


if __name__ == "__main__":
    grossmargin = GrossMargin(
        gross_operating_profit=258880,
        net_sales=2588809,
        net_operating_profit=25000,
        sales=2588800009,
        net_profit_of_use=258809,
        total_of_these_funds=2588809,
    )
    viewgrossmargin = grossmargin.net_profits()
    print(viewgrossmargin)
