
class MetaData:
    """## Return:  meta data
arithmetical gross profit => Αριθμοδείκτης μικτού κέρδους"""

    cost_of_goods_sold = """[Τεκμηρίωση cost_of_goods_sold]
[Βασικό στοιχείο που επηρεάζει τα μικτά αποτελέσματα της χρήσης είναι το κόστος των πωληθέντων αποθεμάτων.]
[Το κόστος πωλήσεων περιλαμβάνει τη διαφορά μεταξύ των κονδυλίων «κύκλος εργασιών» και «μικτά αποτελέσματα εκμεταλλεύσεως».   ]\n[Documentation cost_of_goods_sold]
[A key factor affecting the mixed results for the year is the cost of inventory sold. ]
[Cost of sales includes the difference between 'turnover' and 'gross operating results]'."""
    net_sales = """[Τεκμηρίωση net_sales]
[Η αξία των πωλήσεων μιας οικονομικής μονάδας μετά την αφαίρεση των φόρων (πχ. ΦΠΑ), των επιστροφών, των εκπτώσεων και της αξίας των κατεστραμμένων προϊόντων]
[Documentation net_sales]
[The value of sales of an economic unit after deduction of taxes (e.g. VAT), returns, discounts and the value of damaged products]
"""
    maintenance_and_repair_costs = """[Τεκμηρίωση maintenance_and_repair_costs]
Τα έξοδα συντήρησης και επισκευής (maintenance and repair costs) αναφέρονται σε εκείνα τα έξοδα που προκύπτουν για τη διατήρηση των πάγιων περιουσιακών στοιχείων ή των εγκαταστάσεων σε λειτουργική κατάσταση και την αποκατάσταση των τυχόν ζημιών ή φθορών που προκύπτουν από τη χρήση τους.]
[Αυτά τα έξοδα είναι συνήθως απαραίτητα για την καλή λειτουργία και μακροχρόνια διάρκεια ζωής των υποδομών, του εξοπλισμού και των μηχανημάτων.]
[Documentation maintenance_and_repair_costs]
[Maintenance and repair costs (maintenance and repair costs) refer to those costs incurred to maintain the fixed assets or facilities in an operational condition and to repair any damages or damages resulting from their use.]
[These costs are usually necessary for the good operation and long life of the infrastructure, equipment and machinery.]
"""
    fixed_assets_before_depreciation = """[Τεκμηρίωση fixed_assets_before_depreciation]
[Τα πάγια στοιχεία πριν από τις αποσβέσεις (fixed assets before depreciation) αναφέρονται στην αξία των πάγιων περιουσιακών στοιχείων μιας επιχείρησης πριν εφαρμοστούν οι αποσβέσεις. ]
[Τα πάγια στοιχεία περιλαμβάνουν τα υλικά ή άυλα περιουσιακά στοιχεία που χρησιμοποιούνται από την επιχείρηση για μεγαλύτερο χρονικό διάστημα, συνήθως πάνω από 1 έτος, και δεν προορίζονται για άμεση πώληση.]
[Documentation fixed_assets_before_depreciation]
[Fixed assets before depreciation refer to the value of a company's fixed assets before depreciation is applied.]
[Fixed assets include tangible or intangible assets that are used by the business for a longer period of time, usually more than 1 year, and are not intended for immediate sale.]
"""
    depreciation_of_use = """[Τεκμηρίωση depreciation_of_use]
[Η απόσβεση χρήσης (depreciation of use) αναφέρεται στον τρόπο με τον οποίο ένα πάγιο περιουσιακό στοιχείο χάνει την αξία του με την πάροδο του χρόνου, λόγω της χρήσης του στην παραγωγική διαδικασία ή στις καθημερινές λειτουργίες της επιχείρησης.]
[Η συγκεκριμένη φράση τονίζει τη συσχέτιση της απόσβεσης με την ένταση και διάρκεια χρήσης του περιουσιακού στοιχείου.]
[Documentation depreciation_of_use]
[Depreciation of use refers to the way in which a fixed asset loses its value over time, due to its use in the production process or in the day-to-day operations of the business.]
[This phrase emphasizes the correlation of depreciation with the intensity and duration of use of the asset.]
"""
    fixed_assets_for_depreciation = """[Τεκμηρίωση fixed_assets_for_depreciation]
[Ο όρος πάγια στοιχεία για απόσβεση (fixed assets for depreciation) αναφέρεται στα πάγια περιουσιακά στοιχεία που υπόκεινται σε απόσβεση, δηλαδή εκείνα που χρησιμοποιούνται από την επιχείρηση στις δραστηριότητές της και έχουν περιορισμένη ωφέλιμη διάρκεια ζωής.]
[Documentation fixed_assets_for_depreciation]
[The term fixed assets for depreciation (fixed assets for depreciation) refers to the assets that are subject to depreciation, that is, those that are referred by the company to its activities and have a limited useful life.]
"""
    due_to_operating_expenses = """"[Τεκμηρίωση due_to_operating_expenses]
[Ο όρος "due to operating expenses" μπορεί να αποδοθεί στα ελληνικά ως "λόγω λειτουργικών εξόδων" ή "εξαιτίας λειτουργικών εξόδων".]
[Χρησιμοποιείται για να περιγράψει δαπάνες ή υποχρεώσεις που προκύπτουν από την καθημερινή λειτουργία μιας επιχείρησης.]
[Μπορεί να αναφέρεται σε λόγους για τους οποίους μειώνονται τα έσοδα ή το κέρδος, π.χ. "Η μείωση των καθαρών κερδών οφείλεται στα υψηλά λειτουργικά έξοδα.]
[Documentation due_to_operating_expenses]
[It is used to describe expenses or liabilities arising from the day-to-day running of a business.]
[It can refer to reasons why revenue or profit is falling, e.g. "The decrease in net profits is due to high operating expenses.]
"""


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
    def __init__(self,
        maintenance_and_repair_costs:float=1.0,
        fixed_assets_before_depreciation:float=1.0,
        net_sales:float=1.0,
        depreciation_of_use: float=1.0,
        fixed_assets_for_depreciation: float=1.0,
        due_to_operating_expenses: float=1.0,
        cost_of_goods_sold: float=1.0):
        self.maintenance_and_repair_costs =  maintenance_and_repair_costs
        self.fixed_assets_before_depreciation =  fixed_assets_before_depreciation
        self.net_sales = net_sales
        self.depreciation_of_use = depreciation_of_use
        self.fixed_assets_for_depreciation = fixed_assets_for_depreciation
        self.due_to_operating_expenses = due_to_operating_expenses
        self.cost_of_goods_sold = cost_of_goods_sold

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
        return round(self.maintenance_and_repair_costs / self.fixed_assets_before_depreciation, 2)

    def maintenance_and_repair_costs_to_sales(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος δαπανες συντήρησης και επισκευης προς πώλησεις, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n 
        ### Documentation\n
        The maintenance and repair costs to sales method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.maintenance_and_repair_costs/self.net_sales), 2)
        """
        return round((self.maintenance_and_repair_costs/self.net_sales), 2)
    
    def depreciation_of_fixed_assets(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αποσβεσεις παγιων, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n 
        ### Documentation\n
        The mdepreciation of fixed assets method inherits Accounts from the MaintenanceRepair class.
        ### Returns:  round((self.depreciation_of_use/self.fixed_assets_before_depreciation), 2)
        """
        return round((self.depreciation_of_use/self.fixed_assets_before_depreciation), 2)
    
    def depreciation_to_net_sales(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αποσβεσεις προς καθαρές πωλήσεις, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n 
        ### Documentation\n
        The depreciation to net sales method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.depreciation_of_use/self.net_sales), 2)
        """
        return round((self.depreciation_of_use/self.net_sales), 2)
    
    def operating_expenses(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος λειτουργικων εξοδων, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n 
        ### Documentation\n
        The operating expenses method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round(((self.cost_of_goods_sold + self.due_to_operating_expenses) /self.net_sales), 2)
        """
        return round(((self.cost_of_goods_sold + self.due_to_operating_expenses) /self.net_sales), 2)
    
    def operating_expenses_to_sales(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος λειτουργικων εξοδων προς πωλησεις, κληρονομεί τους λογαριασμούς από την MaintenanceRepair κλάση\n 
        ### Documentation\n
        The operating expenses to sales method inherits Accounts from the MaintenanceRepair class.
        ### Returns: round((self.due_to_operating_expenses /self.net_sales), 2)
        """
        return round((self.due_to_operating_expenses /self.net_sales), 2)
    
    