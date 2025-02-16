import pytest
import sys  
import os  

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.fundamental_analysis.profitability_radios.equity_capital import EquityCapital


@pytest.fixture
def equitycapital() -> EquityCapital:
    """Fixture για τη δημιουργία μιας νέας παρουσίας του ActivityRadio."""
    return EquityCapital()

class TestEquityCapital:
    """class test"""

    @pytest.mark.parametrize("net_profits, net_sales, expected_exception",  [
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
            equitycapital: EquityCapital,
            net_profits,
            net_sales,
            expected_exception,
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                equitycapital.net_profit_margin(net_profits, net_sales) 
    
    @pytest.mark.parametrize("net_sales, fixed_asset, expected_exception",  [
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
            equitycapital: EquityCapital,
            net_sales,
            fixed_asset,
            expected_exception,
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                equitycapital.asset_turnover_velocity(net_sales, fixed_asset) 

    
    @pytest.mark.parametrize("fixed_asset, equity_capital, expected_exception",  [
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
        equitycapital:EquityCapital,
        fixed_asset ,
        equity_capital,
        expected_exception
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                equitycapital.financial_leverage(fixed_asset, equity_capital) 

    @pytest.mark.parametrize("net_profit_margin, asset_turnover_velocity, financial_leverage, expected_exception", [  # Έγκυρες περιπτώσεις
        (10, 5, 2, None),
        (10.0, 5.0, 2.0, None),
        (-10, 5, 2, None),
        (1e6, 1e3, 1e2, None),  # Μεγάλες τιμές
        (1e-6, 1e-3, 1e-2, None),  # Πολύ μικρές τιμές
        (100, 10, -5, None),  # Αρνητικός διαιρέτης
        (-100, -10, -5, None),  # Όλες οι τιμές αρνητικές
        (0.1, 0.2, 0.3, None),  # Floating-point precision

        # Λανθασμένες περιπτώσεις (Errors)
        (100, 0, 10, TypeError),  # Πολλαπλασιασμός με μηδέν (έγκυρο)
        (100, 10, 0, TypeError),  # Διαίρεση με μηδέν
        (0, 100, 10, TypeError),  # Πολλαπλασιασμός με μηδέν (έγκυρο)
        (1e308, 1e308, 1e308, TypeError),  # Πολύ μεγάλες τιμές (overflow)
        (-1e308, -1e308, -1e308, TypeError),  # Πολύ μεγάλες αρνητικές τιμές (overflow)
        ("10", 5, 2, TypeError),  # String ως είσοδος
        (None, 5, 2, TypeError),  # None ως είσοδος
        ([], {}, [], TypeError),  # Μη αριθμητικοί τύποι
        ("days9", "verage_stock9", "cost_of_goods_sold9", TypeError),  # Μη αριθμητικά strings
    ])
    def test_equity_multiplier(self,
            equitycapital:EquityCapital,
            net_profit_margin: float | None ,
            asset_turnover_velocity,
            financial_leverage,
            expected_exception: None | type[TypeError],
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                equitycapital.equity_multiplier(net_profit_margin, asset_turnover_velocity, financial_leverage) 

    @pytest.mark.parametrize("net_profits, equity_capital, expected_exception",  [
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
        equitycapital:EquityCapital,
        net_profits ,
        equity_capital,
        expected_exception
            ) -> None:
        
        if expected_exception:
            with pytest.raises(expected_exception):
                equitycapital.financial_leverage(net_profits, equity_capital) 
