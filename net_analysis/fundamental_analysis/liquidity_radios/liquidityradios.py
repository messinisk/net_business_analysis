"""# total working capital <br/>
# circulating assets <br/>
# net working capital
"""

class MetaData:
    """## Return:  meta data """
    circulating_assets = """[Τεκμηρίωση circulating_assets]
[Κυκλοφορούντα Περιουσιακά στοιχεία αποτελούν τα περιουσιακά στοιχεία του Ενεργητικού που προορίζονται να αλλάζουν θέση και μορφή μία ή περισσότερες φορές μέσα σε μια διαχειριστική χρήση (ένα έτος).]
[Τα κυκλοφορούντα περιουσιακά στοιχεία διακρίνονται σε:]
[Αποθέματα υλικών αξιών, όπως εμπορεύματα, έτοιμα προϊόντα, ημιτελή προϊόντα, πρώτες και βοηθητικές ύλες, ανταλλακτικά πάγιων στοιχείων, είδη συσκευασίας κτλ. Βραχυπρόθεσμες απαιτήσεις.]
[Είναι οι απαιτήσεις που πρόκειται να εισπραχθούν το αργότερο μέχρι το τέλος της επόμενης χρήσης, όπως πελάτες, γραμμάτια εισπρακτέα, χρεώστες διάφοροι κτλ. Χρεόγραφα.]
[Είναι οι μετοχές Α.Ε. (εφόσον δεν πρόκειται για συμμετοχές), ομολογίες, ομόλογα, έντοκα γραμμάτια του Ελληνικού Δημοσίου, κτλ. Διαθέσιμα.]
[Είναι τα περιουσιακά στοιχεία που μετατρέπονται σε χρήματα αμέσως και ασφαλώς, δηλαδή μπορούν να χρησιμοποιηθούν για πληρωμές σε οποιαδήποτε στιγμή, όπως μετρητά (ταμείο), καταθέσεις όψεως, ληγμένα τοκομερίδια ομολογιών εισπρακτέα.]
[Το κόστος πωλήσεων περιλαμβάνει τη διαφορά μεταξύ των κονδυλίων «κύκλος εργασιών» και «μικτά αποτελέσματα εκμεταλλεύσεως».   ]
[Documentation circulating_assets]
Current Assets are the assets of the Asset that are intended to change position and one or more times within a management year (one year).]
[Current assets are divided into: Inventories of tangible assets, such as merchandise, finished products, unfinished products, raw and auxiliary materials, spare parts of fixed assets, types of packaging, etc.]
[Short term receivables. These are the receivables that are to be collected by the end of the next fiscal year at the latest, such as customers, notes receivable, miscellaneous debtors, etc.]
[Securities. Are the shares of A.E. (as long as it is not about participations), bonds, bonds, interest-bearing bonds of the Greek State, etc.]
[available_cash. They are the assets that can be converted into money immediately and safely, that is, they can be used for payments at any time, such as cash (cash), demand deposits, maturing notes receivable.]"""

    short_term_liabilities = """[Τεκμηρίωση short_term_liabilities]
[Βραχυπρόθεσμες υποχρεώσεις είναι εκείνες για τις ποίες η προθεσμία εξοφλήσεώς τους λήγει μέχρι το τέλος της επόμενης χρήσεως και Αποτελούν Έξοδο για την επιχείρηση.]
[Documentation short_term_liabilities]
[Short-term liabilities are those for which their repayment term expires by the end of the next fiscal year and constitute an Outgo for the business.]
"""

    available_cash = """[Τεκμηρίωση available_cash]
[Είναι τα περιουσιακά στοιχεία που μετατρέπονται σε χρήματα αμέσως και ασφαλώς, δηλαδή μπορούν να χρησιμοποιηθούν για πληρωμές σε οποιαδήποτε στιγμή, όπως μετρητά (ταμείο), καταθέσεις όψεως, ληγμένα τοκομερίδια ομολογιών εισπρακτέα.]
[Documentation available_cash]
[They are the assets that can be converted into money immediately and safely, that is, they can be used for payments at any time, such as cash (cash), demand deposits, maturing notes receivable.]
"""
    stock="""[Τεκμηρίωση stock]
[Το  μέγιστου αποθέματος μια συγκεκριμένης ημέρας στην αποθήκη.]
[Documentation average_stock]
[The maximum stock of a particular day in the warehouse).          ]
"""

    forecast_daily_expenses = """[Τεκμηρίωση forecast_daily_expenses]
[αναφέρεται στην εκτίμηση ή πρόβλεψη των ημερήσιων δαπανών με βάση τα ιστορικά δεδομένα, πρότυπα των δαπανών, και τις αναμενόμενες μελλοντικές ανάγκες.]
[Αυτό συνήθως περιλαμβάνει την ανάλυση παρελθόν έξοδα, την κατηγοριοποίηση των δαπανών, και τον υπολογισμό των μέσων όρων ή τάσεις να προβλέψει το μέλλον της καθημερινής κόστος]
[Documentation forecast_daily_expenses]
[refers to the estimation or prediction of daily spending based on historical data, spending patterns, and expected future needs.]
[It typically involves analyzing past expenses, categorizing expenditures, and calculating averages or trends to anticipate future daily costs.]
"""

    requirements = """[Τεκμηρίωση requirements]
[Στα οικονομικά και τη λογιστική, ο όρος "requirements" αναφέρεται σε:]
[Πόρους, κεφάλαια ή αγαθά που είναι απαραίτητα για την επίτευξη ενός στόχου, την υλοποίηση ενός έργου ή τη διατήρηση της λειτουργίας μιας επιχείρησης.]
[Στην περίπτωση επιχειρήσεων, περιλαμβάνει συχνά χρηματοοικονομικές απαιτήσεις]
[όπως εισπρακτέα ποσά από πελάτες (accounts receivable) ή άλλα στοιχεία που σχετίζονται με τον κύκλο εργασιών.]
[Documentation requirements]
[Requirements refer to the necessary resources, funds, or goods needed to achieve a goal, execute a project, or maintain a business's operations.]
[In financial terms, it often includes receivables or other obligations linked to the operating cycle]
"""

    def __str__(self):
        attributes = [
            self.circulating_assets,
            self.short_term_liabilities,
            self.available_cash,
            self.forecast_daily_expenses,
            self.requirements
        ]
        return "\n\n".join(map(str, attributes))


class LiquidityRadios:
    """
    ### Τεκμηρίωση\n
    Η κλάση Μικτό περιθώριο,  ενσωματώνει όλους   εκείνους τους λογαριασμούς που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί  Αρχικοποιούνται ως πραγματική κάτι συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    Για να   αντιμετωπίσουμε πιθανό σφάλματα Division Error που αφορά διαίρεση με το 0  αρχικοποιούμε  σε τιμή ίση με  1.0\n
    και ταυτόχρονα αποκτάμε προαιρετική χρήση μεθόδων άλλα και  επιλογή ποια ορίσματα θέλουμε.\n\n  
    ### Documentation\n
    The Gross Margin class encapsulates all those accounts that its methods use.\n 
    This accounts are initialized as real something common in the way of representation in accounting.\n 
    To deal with possible Division Error errors related to division by 0 we initialize to a value equal to 1.0\n 
    and at the same time get optional use of other methods and choice of which arguments we want.
    method :
        +current_radio-> float
        +cash_radio-> float
        +financial_leverage-> float
        +defensive_interval-> float
        +net_working_capital-> float
        +acid_test_radio-> float
        +quick_radio-> float

    """
    def __init__(self,
        circulating_assets: float,
        short_term_liabilities: float,
        available_cash: float,
        stocks: float,
        forecast_daily_expenses: float,
        requirements: float)->None:
        self.circulating_assets = circulating_assets
        self.short_term_liabilities = short_term_liabilities
        self.available_cash = available_cash
        self.stocks = stocks
        self.forecast_daily_expenses = forecast_daily_expenses
        self.requirements = requirements

    def current_radio(self) -> float:
        """Αριθμοδείκτης Γενικής
        ή έμμεσης ρευστότητας
        """
        return round(self.circulating_assets / self.short_term_liabilities, 2)

    def cash_radio(self) -> float:
        """Αριθμοδείκτης ταμειακής ρευστότητας"""
        return round(self.available_cash / self.short_term_liabilities, 2)

    def defensive_interval(self) -> float:
        """Το αμυντικό διάστημα"""
        return round((self.circulating_assets - self.stocks) / self.forecast_daily_expenses, 2)

    def net_working_capital(self)-> float:
        """καθαρο κεφαλαιο κινησης"""
        return round(self.short_term_liabilities / self.circulating_assets, 2)

    def acid_test_radio(self)-> float:
        """Άμεση ρευστότητα"""
        return round(((self.circulating_assets - self.stocks) / self.short_term_liabilities), 2)

    def quick_radio(self)-> float:
        """Άμεση ρευστότητα"""
        return round(((self.requirements - self.available_cash) / self.short_term_liabilities), 2)
