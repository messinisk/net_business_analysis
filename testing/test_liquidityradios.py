import pytest
import sys  
import os  

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.fundamental_analysis.liquidity_radios.liquidityradios import LiquidityRadios

@pytest.fixture
def liquidity_radios() -> LiquidityRadios:
    return LiquidityRadios()

class TestLiquidityRadios:
    """class test"""


    @pytest.mark.parametrize("circulating_assets, short_term_liabilities, expected_exception",  [
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
        (10, 0, TypeError),  # Διαίρεση με μηδέν
        (-10, 0, TypeError),  # Αρνητικός αριθμητής με διαίρεση μηδέν
        ("10", 2, TypeError),  # Μη αριθμητικός τύπος (string)
        (10, "2", TypeError),  # String παρονομαστής
        (None, 2, TypeError),  # None αριθμητής
        (10, None, TypeError),  # None παρονομαστής
        ([], {}, TypeError),  # Μη αριθμητικοί τύποι
    ])
    def test_current_radio(self,
        liquidity_radios,
        circulating_assets,
        short_term_liabilities,
        expected_exception):
        if expected_exception:
            with pytest.raises(expected_exception):
                liquidity_radios.current_radio(circulating_assets, short_term_liabilities)
    
    @pytest.mark.parametrize("available_cash, short_term_liabilities, expected_exception",  [
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
        (10, 0, TypeError),  # Διαίρεση με μηδέν
        (-10, 0, TypeError),  # Αρνητικός αριθμητής με διαίρεση μηδέν
        ("10", 2, TypeError),  # Μη αριθμητικός τύπος (string)
        (10, "2", TypeError),  # String παρονομαστής
        (None, 2, TypeError),  # None αριθμητής
        (10, None, TypeError),  # None παρονομαστής
        ([], {}, TypeError),  # Μη αριθμητικοί τύποι
    ])
    def test_cash_radio(self,
        liquidity_radios,
        available_cash, short_term_liabilities, expected_exception):
        if expected_exception:
            with pytest.raises(expected_exception):
                liquidity_radios.cash_radio(available_cash, short_term_liabilities)

    @pytest.mark.parametrize("circulating_assets,stocks,  forecast_daily_expenses, expected_exception" ,[
    # Έγκυρες περιπτώσεις
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
    def test_defensive_interval(self,
        liquidity_radios,
        circulating_assets,
        stocks,
        forecast_daily_expenses,
        expected_exception) -> float:
        if expected_exception:
            with pytest.raises(expected_exception):
                liquidity_radios.defensive_interval(circulating_assets,stocks,  forecast_daily_expenses)
     
    @pytest.mark.parametrize("short_term_liabilities, circulating_assets, expected_exception",  [
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
        (10, 0, TypeError),  # Διαίρεση με μηδέν
        (-10, 0, TypeError),  # Αρνητικός αριθμητής με διαίρεση μηδέν
        ("10", 2, TypeError),  # Μη αριθμητικός τύπος (string)
        (10, "2", TypeError),  # String παρονομαστής
        (None, 2, TypeError),  # None αριθμητής
        (10, None, TypeError),  # None παρονομαστής
        ([], {}, TypeError),  # Μη αριθμητικοί τύποι
    ])
    def test_net_working_capital(self,
        liquidity_radios,       
        short_term_liabilities,
        circulating_assets,
        expected_exception)-> float:
        if expected_exception:
            with pytest.raises(expected_exception):
                liquidity_radios.net_working_capital(short_term_liabilities, circulating_assets)

    @pytest.mark.parametrize("circulating_assets, stocks,  short_term_liabilities, expected_exception" ,[
    # Έγκυρες περιπτώσεις
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
    def test_acid_test_radio(self,
        liquidity_radios,
        circulating_assets,
        stocks,
        short_term_liabilities,
        expected_exception)-> float:
        if expected_exception:
            with pytest.raises(expected_exception):
                liquidity_radios.acid_test_radio(circulating_assets, stocks, short_term_liabilities)
   

    @pytest.mark.parametrize("requirements, available_cash,  short_term_liabilities, expected_exception" ,[
    # Έγκυρες περιπτώσεις
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
    def test_quick_radio(self,
        liquidity_radios,
        requirements,
        available_cash,
        short_term_liabilities,
        expected_exception)-> float:
        if expected_exception:
            with pytest.raises(expected_exception):
                liquidity_radios.quick_radio(requirements, available_cash, short_term_liabilities)
   