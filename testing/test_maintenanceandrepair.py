import pytest
import sys  
import os  

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from net_analysis.fundamental_analysis.profitability_radios.maintenanceandrepair import MaintenanceRepair

@pytest.fixture
def maintenance_repair() -> MaintenanceRepair:
    """Fixture για τη δημιουργία μιας νέας παρουσίας του ActivityRadio."""
    return MaintenanceRepair()

class TestMaintenanceRepair:
    """class test"""


    @pytest.mark.parametrize("maintenance_and_repair_costs, net_fixed_assets_before_depreciationsales, expected_exception",  [
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
    def test_maintenance_and_repair_costs_for_fixed_assets(self,
        maintenance_repair: MaintenanceRepair,
        maintenance_and_repair_costs: float,
        net_fixed_assets_before_depreciationsales: float,
        expected_exception: TypeError) -> None:
        if expected_exception:
            with pytest.raises(expected_exception):
                maintenance_repair.maintenance_and_repair_costs_for_fixed_assets(maintenance_and_repair_costs, net_fixed_assets_before_depreciationsales ) 

    @pytest.mark.parametrize("maintenance_and_repair_costs, net_sales, expected_exception",  [
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
    ])
    def test_maintenance_and_repair_costs_to_sales(self,
        maintenance_repair: MaintenanceRepair,
        maintenance_and_repair_costs: float,
        net_sales: float,
        expected_exception: TypeError):
        if expected_exception:
            with pytest.raises(expected_exception):
                maintenance_repair.maintenance_and_repair_costs_to_sales(maintenance_and_repair_costs, net_sales ) 
      
    @pytest.mark.parametrize("depreciation_of_use, fixed_assets_before_depreciation, expected_exception",  [
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
    ])
    def test_depreciation_of_fixed_assets(self,
        maintenance_repair: MaintenanceRepair,
        depreciation_of_use: float,
        fixed_assets_before_depreciation: float,
        expected_exception: TypeError):
        if expected_exception:
            with pytest.raises(expected_exception):
                maintenance_repair.depreciation_of_fixed_assets(depreciation_of_use, fixed_assets_before_depreciation ) 
    
    @pytest.mark.parametrize("depreciation_of_use, net_sales, expected_exception",  [
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
    ])
    def test_depreciation_to_net_sales(self,
        maintenance_repair: MaintenanceRepair,
        depreciation_of_use: float,
        net_sales: float,
        expected_exception: TypeError):
        if expected_exception:
            with pytest.raises(expected_exception):
                maintenance_repair.depreciation_to_net_sales(depreciation_of_use, net_sales) 
    
    @pytest.mark.parametrize("due_to_operating_expenses, net_sales, expected_exception",  [
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
    ])
    def test_operating_expenses_to_sales(self,
        maintenance_repair: MaintenanceRepair,
        due_to_operating_expenses: float,
        net_sales: float,
        expected_exception: TypeError):
        if expected_exception:
            with pytest.raises(expected_exception):
                maintenance_repair.depreciation_to_net_sales(due_to_operating_expenses, net_sales) 


    @pytest.mark.parametrize("cost_of_goods_sold, due_to_operating_expenses, net_sales, expected_exception",[
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
    def test_operating_expenses(self,
        maintenance_repair: MaintenanceRepair,
        cost_of_goods_sold: float,
        due_to_operating_expenses: float,
        net_sales,
        expected_exception: TypeError):
        if expected_exception:
            with pytest.raises(expected_exception):
                maintenance_repair.operating_expenses(cost_of_goods_sold, due_to_operating_expenses, net_sales) 