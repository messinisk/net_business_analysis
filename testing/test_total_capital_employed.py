import pytest
import sys  
import os  

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.fundamental_analysis.profitability_radios.total_capital_employed import ReturnTotalCapitalEmployed

@pytest.fixture
def maintenance_repair() -> ReturnTotalCapitalEmployed:
    """Fixture για τη δημιουργία μιας νέας παρουσίας του ActivityRadio."""
    return ReturnTotalCapitalEmployed()

class TestReturnTotalCapitalEmployed:
    """class test"""

#self.net_profits + self.interest * (1-self.tax_rate))/self.total_capital

    @pytest.mark.parametrize("net_profits, interest,tax_rate, total_capital, expected_exception",  [
       
    ])
    def test_value_total_capital(self,
        maintenance_repair: ReturnTotalCapitalEmployed,
        net_profits: float,
        interest,
        tax_rate: float,
        total_capital,
        expected_exception: TypeError) -> None:
        maintenance_repair.value_total_capital(net_profits, interest, tax_rate, total_capital)
    
    @pytest.mark.parametrize("net_profits, interest,tax_rate, net_sales, expected_exception",  [
         # ✅ Έγκυρες περιπτώσεις
        (10, 2, 10, 5,  None),  # Απλή διαίρεση
        (1e6, 1e3, 1e6, 1e3,None),  # Πολύ μεγάλες τιμές
        (1e-6, 1e-3,1e-6, 1e-3, None),  # Πολύ μικρές τιμές (floating point precision)
        
        # ❌ Λανθασμένες περιπτώσεις (Errors)
    
        (-10, 0,-10, 0, TypeError),  # Αρνητικός αριθμητής με διαίρεση μηδέν
        ("10", 2,"10", 2, TypeError),  # Μη αριθμητικός τύπος (string)
        (10, "2",10, 2, TypeError),  # String παρονομαστήςring)
        (10, "2",10, 2,TypeError),  # String παρονομαστής
    ])
    def test_net_profit_margin(self,
        maintenance_repair: ReturnTotalCapitalEmployed,
        net_profits: float,
        interest,
        tax_rate: float,
        net_sales,
        expected_exception: TypeError) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                maintenance_repair.net_profit_margin(net_profits, interest, tax_rate, net_sales)
    

    pytest.mark.parametrize("net_sales, total_capital, expected_exception",  [
        # ✅ Έγκυρες περιπτώσεις
        (10, 2, None),  # Απλή διαίρεση
        (100, 10, None),  # Απλή διαίρεση με μεγαλύτερους αριθμούς
        (-10, 2, None),  # Αρνητικός αριθμητής
        (10, -2, None),  # Αρνητικός παρονομαστής
        (-10, -2, None),  # Και οι δύο αρνητικοί (πρέπει να δώσει θετικό αποτέλεσμα)
        (0.1, 0.2, None),  # Floating-point αριθμοί
        (1e6, 1e3, None),  # Πολύ μεγάλες τιμές
        (1e-6, 1e-3, None),  # Πολύ μικρές τιμές (floating point precision)
        
        # ❌ Λανθασμένες περιπτώσεις (Errors)
        (10, -5, TypeError),  # Διαίρεση με μηδέν
        (-10, 0, TypeError),  # Διαίρεση με μηδέν
        (0, 10, TypeError),  # Διαίρεση με μηδέν
        (10, 0, TypeError),  # Διαίρεση με μηδέν
        (-10, 0, TypeError),  # Αρνητικός αριθμητής με διαίρεση μηδέν
        ("10", 2, TypeError),  # Μη αριθμητικός τύπος (string)
        (10, "2", TypeError),  # String παρονομαστής
        (None, 2, TypeError),  # None αριθμητής
        (10, None, TypeError),  # None παρονομαστής
        ([], {}, TypeError),  # Μη αριθμητικοί τύποι
    ])
    def test_asset_turnover_velocity(self,
        maintenance_repair: ReturnTotalCapitalEmployed,
        net_sales: float,
        total_capital: float,
        expected_exception: TypeError) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                maintenance_repair.asset_turnover_velocity(net_sales, total_capital)

    