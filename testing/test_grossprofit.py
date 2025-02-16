import pytest
import sys  
import os  

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.fundamental_analysis.profitability_radios.grossprofit import GrossMargin

@pytest.fixture
def grossmargin() -> GrossMargin:
    """Fixture για τη δημιουργία μιας νέας παρουσίας του ActivityRadio."""
    return GrossMargin()

class TestGrossMargin:
    """class test"""

    @pytest.mark.parametrize("gross_operating_profit, net_sales, expected_exception",  [
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
    def test_gross_profit_margin(self,
            grossmargin: GrossMargin,
            gross_operating_profit,
            net_sales,
            expected_exception,
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                grossmargin.gross_profit_margin(gross_operating_profit, net_sales) 

    @pytest.mark.parametrize("net_operating_profit, net_sales, expected_exception",  [
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
    def test_net_profit_margin(self,
            grossmargin: GrossMargin,
            net_operating_profit,
            net_sales,
            expected_exception,
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                grossmargin.net_profit_margin(net_operating_profit, net_sales) 
    
    @pytest.mark.parametrize("sales, net_profit_margin, expected_exception",  [
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
    def test_net_profits(self,
            grossmargin: GrossMargin,
            sales,
            net_profit_margin,
            expected_exception,
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                grossmargin.net_profits(sales, net_profit_margin) 

    @pytest.mark.parametrize("net_profit_of_use, total_of_these_funds, expected_exception",  [
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
    def test_return_on_equity(self,
            grossmargin: GrossMargin,
            net_profit_of_use,
            total_of_these_funds,
            expected_exception,
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                grossmargin.return_on_equity(net_profit_of_use, total_of_these_funds) 