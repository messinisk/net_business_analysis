import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from net_analysis.setting.number_output_formatting import display_locale
from net_analysis.setting.number_output_formatting import is_valid_number


class ViewMaintenanceRepair:
    def __init__(self, value: float, method_name: str):
        self.value = display_locale(value)
        self.method_name = method_name.replace("_", " ").title()

    def __str__(self) -> str:
        return f"{self.method_name}: {self.value}"


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
        maintenance_and_repair_costs: float,
        fixed_assets_before_depreciation: float,
        net_sales: float,
        depreciation_of_use: float,
        fixed_assets_for_depreciation: float,
        due_to_operating_expenses: float,
        cost_of_goods_sold: float,
    ):
        self.maintenance_and_repair_costs = maintenance_and_repair_costs
        self.fixed_assets_before_depreciation = fixed_assets_before_depreciation
        self.net_sales = net_sales
        self.depreciation_of_use = depreciation_of_use
        self.fixed_assets_for_depreciation = fixed_assets_for_depreciation
        self.due_to_operating_expenses = due_to_operating_expenses
        self.cost_of_goods_sold = cost_of_goods_sold

    def maintenance_and_repair_costs_for_fixed_assets(self) -> ViewMaintenanceRepair:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος δαπανες συντήρησης και επισκευής προς παγια, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The maintenance_and_repair_costs_for_fixed_assets method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.maintenance_and_repair_costs/self.fixed_assets_before_depreciation), 2)
        """
        maintenance_and_repair_costs = is_valid_number(
            self.maintenance_and_repair_costs
        )
        fixed_assets_before_depreciation = is_valid_number(
            self.fixed_assets_before_depreciation
        )

        if isinstance(maintenance_and_repair_costs, str) or isinstance(
            fixed_assets_before_depreciation, str
        ):
            return ViewMaintenanceRepair(0.0, sys._getframe(0).f_code.co_name)

        values = round(
            maintenance_and_repair_costs / fixed_assets_before_depreciation, 2
        )
        return ViewMaintenanceRepair(values, sys._getframe(0).f_code.co_name)

    def maintenance_and_repair_costs_to_sales(self) -> ViewMaintenanceRepair:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος δαπανες συντήρησης και επισκευης προς πώλησεις, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The maintenance and repair costs to sales method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.maintenance_and_repair_costs/self.net_sales), 2)
        """
        maintenance_and_repair_costs = is_valid_number(
            self.maintenance_and_repair_costs
        )
        net_sales = is_valid_number(self.net_sales)

        if isinstance(maintenance_and_repair_costs, str) or isinstance(net_sales, str):
            return ViewMaintenanceRepair(0.0, sys._getframe(0).f_code.co_name)

        values = round(maintenance_and_repair_costs / net_sales, 2)
        return ViewMaintenanceRepair(values, sys._getframe(0).f_code.co_name)

    def depreciation_of_fixed_assets(self) -> ViewMaintenanceRepair:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αποσβεσεις παγιων, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The mdepreciation of fixed assets method inherits Accounts from the MaintenanceRepair class.
        ### Returns:  round((self.depreciation_of_use/self.fixed_assets_before_depreciation), 2)
        """
        depreciation_of_use = is_valid_number(self.depreciation_of_use)
        fixed_assets_before_depreciation = is_valid_number(
            self.fixed_assets_before_depreciation
        )

        if isinstance(depreciation_of_use, str) or isinstance(
            fixed_assets_before_depreciation, str
        ):
            return ViewMaintenanceRepair(0.0, sys._getframe(0).f_code.co_name)

        values = round(depreciation_of_use / fixed_assets_before_depreciation, 2)
        return ViewMaintenanceRepair(values, sys._getframe(0).f_code.co_name)

    def depreciation_to_net_sales(self) -> ViewMaintenanceRepair:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αποσβεσεις προς καθαρές πωλήσεις, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The depreciation to net sales method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.depreciation_of_use/self.net_sales), 2)
        """
        depreciation_of_use = is_valid_number(self.depreciation_of_use)
        net_sales = is_valid_number(self.net_sales)

        if isinstance(depreciation_of_use, str) or isinstance(net_sales, str):
            return ViewMaintenanceRepair(0.0, sys._getframe(0).f_code.co_name)

        values = round(depreciation_of_use / net_sales, 2)
        return ViewMaintenanceRepair(values, sys._getframe(0).f_code.co_name)

    def operating_expenses(self) -> ViewMaintenanceRepair:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος λειτουργικων εξοδων, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The operating expenses method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round(((self.cost_of_goods_sold + self.due_to_operating_expenses) /self.net_sales), 2)
        """
        cost_of_goods_sold = is_valid_number(self.cost_of_goods_sold)
        due_to_operating_expenses = is_valid_number(self.due_to_operating_expenses)
        net_sales = is_valid_number(self.net_sales)

        if (
            isinstance(cost_of_goods_sold, str)
            or isinstance(due_to_operating_expenses, str)
            or isinstance(net_sales, str)
        ):
            return ViewMaintenanceRepair(0.0, sys._getframe(0).f_code.co_name)

        values = round(
            (self.cost_of_goods_sold + self.due_to_operating_expenses) / self.net_sales,
            2,
        )
        return ViewMaintenanceRepair(values, sys._getframe(0).f_code.co_name)

    def operating_expenses_to_sales(self) -> ViewMaintenanceRepair:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος λειτουργικων εξοδων προς πωλησεις, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n
        ### Documentation\n
        The operating expenses to sales method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.due_to_operating_expenses /self.net_sales), 2)
        """
        due_to_operating_expenses = is_valid_number(self.due_to_operating_expenses)
        net_sales = is_valid_number(self.net_sales)

        if isinstance(due_to_operating_expenses, str) or isinstance(net_sales, str):
            return ViewMaintenanceRepair(0.0, sys._getframe(0).f_code.co_name)

        values = round(due_to_operating_expenses / net_sales, 2)
        return ViewMaintenanceRepair(values, sys._getframe(0).f_code.co_name)
