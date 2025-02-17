import pytest
import sys  
import os  

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.fundamental_analysis.activity_radios.activityradios import ActivityRadio




@pytest.fixture
def activity_radio() -> ActivityRadio:
    """Fixture για τη δημιουργία μιας νέας παρουσίας του ActivityRadio."""
    return ActivityRadio()




class TestActivityRadio:
    """class test"""


    @pytest.mark.parametrize("cost_of_goods_sold, average_stock",  [

    ])
    def test_inventories_turnover_radio(self,
            activity_radio: ActivityRadio,
            cost_of_goods_sold,
            average_stock,
            
            ) -> None:
            assert activity_radio.inventories_turnover_radio(cost_of_goods_sold, average_stock) 
            


    
              
    @pytest.mark.parametrize("days, verage_stock, cost_of_goods_sold, expected_exception",[
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
    def test_average_dwell_time_of_inventory_in_the_warehouse(self,
        activity_radio: ActivityRadio,
        days,
        verage_stock,
        cost_of_goods_sold,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.average_dwell_time_of_inventory_in_the_warehouse(days, verage_stock, cost_of_goods_sold) 


    @pytest.mark.parametrize("sale_on_credit, average_requirement, expected_exception",  [
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
    def test_speed_of_collection_of_receivables(self,
        activity_radio: ActivityRadio,
        sale_on_credit, 
        average_requirement,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.speed_of_collection_of_receivables(sale_on_credit, average_requirement)
     


    @pytest.mark.parametrize("days, average_requirement, sale_on_credit, expected_exception",[
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
    def test_average_demand_period(self,
        activity_radio: ActivityRadio,
        days,
        average_requirement,
        sale_on_credit,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.average_dwell_time_of_inventory_in_the_warehouse(days, average_requirement, sale_on_credit) 

    @pytest.mark.parametrize("average_dwell_time_of_inventory_in_the_warehouse, speed_of_collection_of_receivables, expected_exception",  [
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
    def test_business_cycle(self,
        activity_radio: ActivityRadio,
        average_dwell_time_of_inventory_in_the_warehouse,
        speed_of_collection_of_receivables,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.business_cycle(average_dwell_time_of_inventory_in_the_warehouse, speed_of_collection_of_receivables)

    @pytest.mark.parametrize("sourcing, medium_term_short_term_liabilities, expected_exception",  [
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
    def test_velocity_of_current_liabilities(self,
        activity_radio: ActivityRadio,
        sourcing,
        medium_term_short_term_liabilities,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.velocity_of_current_liabilities(sourcing, medium_term_short_term_liabilities)

    @pytest.mark.parametrize("medium_term_short_term_liabilities, days, sourcing, expected_exception",[
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
    def test_average_repayment_period_of_short_term_liabilities(self,
        activity_radio: ActivityRadio,
        medium_term_short_term_liabilities,
        days,
        sourcing,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.velocity_of_current_liabilities(medium_term_short_term_liabilities, days, sourcing)

    @pytest.mark.parametrize("net_sales, net_working_capital, expected_exception",  [
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
    def test_net_working_capital_turnover_speed(self,
        activity_radio: ActivityRadio,
        net_sales,
        net_working_capital,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.velocity_of_current_liabilities(net_sales, net_working_capital)

    @pytest.mark.parametrize("net_sales, total_assets, expected_exception",  [
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
    def test_turnover_speed_total_assets(self,
        activity_radio: ActivityRadio,
        net_sales,
        total_assets,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.velocity_of_current_liabilities(net_sales, total_assets)
    

    @pytest.mark.parametrize("net_sales, net_assets, expected_exception",  [
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
    def test_fixed_turnover_rate(self,
        activity_radio: ActivityRadio,
        net_sales,
        net_assets,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.velocity_of_current_liabilities(net_sales, net_assets)
    

    @pytest.mark.parametrize("net_sales, invested_capital, expected_exception",  [
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
    def test_speed_of_circulating_invested_capital(self,
        activity_radio: ActivityRadio,
        net_sales,
        invested_capital,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.velocity_of_current_liabilities(net_sales, invested_capital)
    
    @pytest.mark.parametrize("net_sales, net_profit, expected_exception",  [
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
    def test_traffic_speed_net_profit(self,
        activity_radio: ActivityRadio,
        net_sales,
        net_profit,
        expected_exception) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                activity_radio.velocity_of_current_liabilities(net_sales, net_profit)
    
   