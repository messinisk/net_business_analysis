"""
# total working capital <br/>
# circulating assets <br/>
# net working capital
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.return_func_error import validate_numerical_inputs



class LiquidityRadios:
    """
    ### Τεκμηρίωση\n
    Η κλάση Μικτό περιθώριο,  ενσωματώνει όλους   εκείνους τους λογαριασμούς\
        που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί  Αρχικοποιούνται ως πραγματική κάτι \
        συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    Για να   αντιμετωπίσουμε πιθανό σφάλματα Division Error που\
        αφορά διαίρεση με το 0  αρχικοποιούμε  σε τιμή ίση με  1.0\n
    και ταυτόχρονα αποκτάμε προαιρετική χρήση μεθόδων άλλα και\
        επιλογή ποια ορίσματα θέλουμε.\n\n
    ### Documentation\n
    The Gross Margin class encapsulates all those\
        accounts that its methods use.\n
    This accounts are initialized as real something\
        common in the way of representation in accounting.\n
    To deal with possible Division Error errors\
        related to division by 0 we initialize to a value equal to 1.0\n
    and at the same time get optional use \
        of other methods and choice of which arguments we want.
    method :
        +current_radio-> float
        +cash_radio-> float
        +financial_leverage-> float
        +defensive_interval-> float
        +net_working_capital-> float
        +acid_test_radio-> float
        +quick_radio-> float

    """

    def __init__(
        self,
        circulating_assets: float,
        short_term_liabilities: float,
        available_cash: float,
        stocks: float,
        forecast_daily_expenses: float,
        requirements: float,
    ) -> None:
        self.circulating_assets = circulating_assets
        self.short_term_liabilities = short_term_liabilities
        self.available_cash = available_cash
        self.stocks = stocks
        self.forecast_daily_expenses = forecast_daily_expenses
        self.requirements = requirements

    @validate_numerical_inputs
    def current_radio(self) -> float:
        """Αριθμοδείκτης Γενικής
        ή έμμεσης ρευστότητας
        """
        return round(self.circulating_assets / self.short_term_liabilities, 2)

    @validate_numerical_inputs
    def cash_radio(self) -> float:
        """Αριθμοδείκτης ταμειακής ρευστότητας"""
        return round(self.available_cash / self.short_term_liabilities, 2)

    @validate_numerical_inputs
    def defensive_interval(self) -> float:
        """Το αμυντικό διάστημα"""
        return round(
            (
                (self.circulating_assets - self.stocks)
                / self.forecast_daily_expenses), 2
        )

    @validate_numerical_inputs
    def net_working_capital(self) -> float:
        """καθαρο κεφαλαιο κινησης"""
        return round(self.short_term_liabilities / self.circulating_assets, 2)

    @validate_numerical_inputs
    def acid_test_radio(self) -> float:
        """Άμεση ρευστότητα"""
        return round(
            (
                (self.circulating_assets - self.stocks)
                / self.short_term_liabilities), 2
        )

    @validate_numerical_inputs
    def quick_radio(self) -> float:
        """Άμεση ρευστότητα"""
        return round(
            (
                (self.requirements - self.available_cash)
                / self.short_term_liabilities), 2
        )


if __name__ == "__main__":
    metrics = LiquidityRadios(1000, 200, 365, 0, 250, 3000)
    assert metrics.current_radio() == float('inf')
    assert metrics.current_radio() == float('inf')
    assert metrics.defensive_interval() == float('inf')
    assert metrics.net_working_capital() == float('inf')
    assert metrics.acid_test_radio() == float('inf')
    assert metrics.quick_radio() == float('inf')
