"""
library liquidity_radios :
+modul :
    + activityradios
    +class : ActivityRadio:
        + args [cost_of_goods_sold: float = 1.0,
            average_stock: float = 1.0,
            days: int = 365,
            sale_on_credit: float = 1.0,
            average_requirement: float = 1.0,
            average_current_liabilities: float= 1.0,
            shopping: float= 1.0,
            net_working_capital: float= 1.0,
            net_sales: float= 1.0,
            total_assets: float=1.0,
            net_assets: float = 1.0,
            capital_employed: float = 1.0,
            net_profit: float = 1.0]
        +method :
        +inventories_turnover_radio -> float
        +Average_dwell_time_of_inventory_in_the_warehouse -> float
        +speed_of_collection_of_receivables -> float
        +average_demand_period -> float
        +business_cycle -> float
        +acid_test_radio -> float
        +velocity_of_current_liabilities -> float
        +average_repayment_period_of_short_term_liabilities -> float
        +net_working_capital_turnover_speed -> float
        +turnover_speed_total_assets -> float
        +fixed_turnover_rate -> float
        +speed_of_circulating_capital_employed -> float
        +traffic_speed_Net_Profit -> float
"""
__title__ = "Library: Liquidity Ratios"
__description__ = """### Documentation\n
This library provides a `Gross Margin` class that encapsulates accounting-related calculations.\n
The accounts are initialized as real numbers, following common accounting practices. To avoid\n
DivisionError (division by zero), the accounts are initialized to 1.0. This ensures robustness\n
and optional use of methods while offering flexibility in argument selection.\n\n
### Τεκμηρίωση\n
Η βιβλιοθήκη παρέχει την κλάση `Μικτό περιθώριο`, η οποία ενσωματώνει λογαριασμούς σχετικούς\n
με υπολογισμούς στη λογιστική. Οι λογαριασμοί αρχικοποιούνται ως πραγματικοί αριθμοί (real),\n
σύμφωνα με τις συνήθεις πρακτικές. Για την αποφυγή σφαλμάτων DivisionError (διαίρεση με το 0),\n
οι λογαριασμοί αρχικοποιούνται στην τιμή 1.0. Αυτό εξασφαλίζει σταθερότητα και ευελιξία\n
στη χρήση μεθόδων."""
__status__ = "Development"
__version__ = "0.0.1-alpha"
__author__ = "Kostas Messinis"
__author_email__ = "messinisk35@gmail.com"
__maintainer__ = "Kostas Messinis"
__maintainer_email__ = "maintainer@example.com"
__license__ = "MIT"
__url__ = "https://github.com/your-repo-url"
__package__ = "liquidity_ratios"
__dependencies__ : list[str] = []


