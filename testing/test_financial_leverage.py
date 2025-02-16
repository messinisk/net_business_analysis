import pytest
import sys  
import os  

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.fundamental_analysis.profitability_radios.financial_leverage import FinancialLeverageRadio


@pytest.fixture
def financial_leverage_radio() -> FinancialLeverageRadio:
    """Fixture για τη δημιουργία μιας νέας παρουσίας του ActivityRadio."""
    return FinancialLeverageRadio()

class TestFinancialLeverageRadio:
    """class test"""

    @pytest.mark.parametrize("asset_turnover_velocity, equity_capital_efficiency, expected_exception",  [
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
    def test_financial_leverage(self,
            financial_leverage_radio: FinancialLeverageRadio,
            asset_turnover_velocity,
            equity_capital_efficiency,
            expected_exception,
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                financial_leverage_radio.financial_leverage(asset_turnover_velocity, equity_capital_efficiency) 
    
    @pytest.mark.parametrize("asset_turnover_velocity, equity_capital_efficiency, expected_exception",  [
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
    def test_economic_benefits(self,
            financial_leverage_radio: FinancialLeverageRadio,
            asset_turnover_velocity,
            equity_capital_efficiency,
            expected_exception,
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                financial_leverage_radio.economic_benefits(asset_turnover_velocity, equity_capital_efficiency) 
