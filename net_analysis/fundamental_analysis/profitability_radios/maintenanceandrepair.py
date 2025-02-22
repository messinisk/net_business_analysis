import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.return_func_error import validate_numerical_inputs


class MaintenanceRepair:
    """
    ### Τεκμηρίωση\n
    Η κλάση Επισκευή Συντήρησης,  ενσωματώνει όλους   εκείνους τους λογαριασμούς που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί  Αρχικοποιούνται ως πραγματική κάτι συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    Για να   αντιμετωπίσουμε πιθανό σφάλματα Division Error που αφορά διαίρεση με το 0  αρχικοποιούμε  σε τιμή ίση με  1.0\n
    και ταυτόχρονα αποκτάμε προαιρετική χρήση μεθόδων άλλα και  επιλογή ποια ορίσματα θέλουμε.\n\n
    ### Documentation\n
    The Maintenance Repair class encapsulates all those accounts that its methods use.\n
    This accounts are initialized as real something common in the way of representation in accounting.\n
    To deal with possible Division Error errors related to division by 0 we initialize to a value equal to 1.0\n
    and at the same time get optional use of other methods and choice of which arguments we want.
    method :
        + maintenance_and_repair_costs_for_fixed_assets
        + maintenance_and_repair_costs_to_sales
        + depreciation_of_fixed_assets
        + depreciation_to_net_sales
        + operating_expenses
        + operating_expenses_to_sales

    """

    def __init__(
        self,
        maintenance_and_repair_costs: float = 1.0,
        fixed_assets_before_depreciation: float = 1.0,
        net_sales: float = 1.0,
        depreciation_of_use: float = 1.0,
        fixed_assets_for_depreciation: float = 1.0,
        due_to_operating_expenses: float = 1.0,
        cost_of_goods_sold: float = 1.0,
    ):
        self.maintenance_and_repair_costs = maintenance_and_repair_costs
        self.fixed_assets_before_depreciation = fixed_assets_before_depreciation
        self.net_sales = net_sales
        self.depreciation_of_use = depreciation_of_use
        self.fixed_assets_for_depreciation = fixed_assets_for_depreciation
        self.due_to_operating_expenses = due_to_operating_expenses
        self.cost_of_goods_sold = cost_of_goods_sold

    @validate_numerical_inputs
    def maintenance_and_repair_costs_for_fixed_assets(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος δαπανες συντήρησης και επισκευής προς παγια, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The maintenance_and_repair_costs_for_fixed_assets method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.maintenance_and_repair_costs/self.fixed_assets_before_depreciation), 2)
        """
        if self.fixed_assets_before_depreciation == 0:
            self.fixed_assets_before_depreciation = 1
        return round(
            self.maintenance_and_repair_costs / self.fixed_assets_before_depreciation, 2
        )

    @validate_numerical_inputs
    def maintenance_and_repair_costs_to_sales(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος δαπανες συντήρησης και επισκευης προς πώλησεις, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The maintenance and repair costs to sales method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.maintenance_and_repair_costs/self.net_sales), 2)
        """
        return round((self.maintenance_and_repair_costs / self.net_sales), 2)

    @validate_numerical_inputs
    def depreciation_of_fixed_assets(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αποσβεσεις παγιων, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The mdepreciation of fixed assets method inherits Accounts from the MaintenanceRepair class.
        ### Returns:  round((self.depreciation_of_use/self.fixed_assets_before_depreciation), 2)
        """
        return round(
            (self.depreciation_of_use / self.fixed_assets_before_depreciation), 2
        )

    @validate_numerical_inputs
    def depreciation_to_net_sales(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αποσβεσεις προς καθαρές πωλήσεις, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The depreciation to net sales method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.depreciation_of_use/self.net_sales), 2)
        """
        return round((self.depreciation_of_use / self.net_sales), 2)

    @validate_numerical_inputs
    def operating_expenses(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος λειτουργικων εξοδων, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The operating expenses method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round(((self.cost_of_goods_sold + self.due_to_operating_expenses) /self.net_sales), 2)
        """
        return round(
            (
                (self.cost_of_goods_sold + self.due_to_operating_expenses)
                / self.net_sales
            ),
            2,
        )

    @validate_numerical_inputs
    def operating_expenses_to_sales(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος λειτουργικων εξοδων προς πωλησεις, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The operating expenses to sales method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.due_to_operating_expenses /self.net_sales), 2)
        """
        return round((self.due_to_operating_expenses / self.net_sales), 2)
