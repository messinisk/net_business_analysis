class MetaData:
    """## Return:  meta data """
    net_profit = """[Τεκμηρίωση net_profit]
[Στις επιχειρήσεις, το καθαρό εισόδημα ή τα καθαρά κέρδη είναι τα έσοδα μείον το κόστος πωληθέντων αγαθών, τα έξοδα και τους φόρους για μια λογιστική χρήση.]
[Documentation net_profit]
[In business, net income or net profit is revenue minus cost of goods sold, expenses, and taxes for an accounting year.]
"""
    net_sales = """[Τεκμηρίωση net_sales]
[Η αξία των πωλήσεων μιας οικονομικής μονάδας μετά την αφαίρεση των φόρων (πχ. ΦΠΑ), των επιστροφών, των εκπτώσεων και της αξίας των κατεστραμμένων προϊόντων]
[Documentation net_sales]
[The value of sales of an economic unit after deduction of taxes (e.g. VAT), returns, discounts and the value of damaged products]
"""
    interest = """[Τεκμηρίωση interest]
[Τόκος είναι η αποζημίωση σε χρήματα που είναι υποχρεωμένος να δώσει ο οφειλέτης στο δανειστή για ορισμένη ποσότητα χρηματικού δανείου που πήρε για συγκεκριμένη χρονική περίοδο.]
[Οι οικονομολόγοι συχνά αναφέρονται στον τόκο ως αμοιβή για τη χρησιμοποίηση χρηματικού κεφαλαίου, ή ως τιμή με την οποία χρεώνεται η χρήση κεφαλαίου. Ο λόγος του τόκου προς το κεφάλαιο λέγεται επιτόκιο. ]
[Documentation interest]
[Interest is the compensation in money that the debtor is obliged to give to the lender for a certain amount of money borrowed for a certain period of time.]
[Economists often refer to interest as a fee for the use of money capital, or as the price at which the use of capital is needed. The ratio of the interest to the principal is called the interest rate.]
"""
    tax_rate = """[Τεκμηρίωση tax_rate]
[Ο φορολογικός συντελεστής (tax_rate) είναι ένα ποσοστό που αντιπροσωπεύει το ποσό του φόρου που επιβάλλεται στα κέρδη μιας επιχείρησης ή ενός ατόμου. Εκφράζεται συνήθως ως δεκαδικός αριθμός ή ποσοστό.]
[Documentation tax_rate]
[The tax rate (tax_rate) is a percentage that represents the amount of tax levied on the profits of a business or an individual. It is usually expressed as a decimal number or percentage.]
"""
    total_capital="""[Τεκμηρίωση total_capital]
[ο συνολικό κεφάλαιο αναφέρεται στο άθροισμα όλων των οικονομικών πόρων που διαθέτει μία επιχείρηση ή ένα άτομο, συμπεριλαμβανομένων ιδίων κεφαλαίων και δανειακού κεφαλαίου. Περιλαμβάνει όλα τα στοιχεία ενεργητικού που χρησιμοποιούνται για την επίτευξη κέρδους,]
[όπως μετρητά, επενδύσεις, ακίνητα και εξοπλισμό. Είναι ένας σημαντικός δείκτης για την οικονομική κατάσταση και τη χρηματοδοτική ικανότητα.]
[Documentation total_capital]
[Total capital refers to the sum of all financial resources available to a business or an individual, including equity and debt capital. It includes all assets used to make a profit.]
[such as cash, investments, property and equipment. It is an important indicator of financial status and financial capacity.]
"""

class ReturnTotalCapitalEmployed:
    """
    ### Τεκμηρίωση\n
    Η κλάση Επιστρέψτε το συνολικό κεφάλαιο,\n\n  
    ενσωματώνει όλους   εκείνους τους λογαριασμούς\n\n  
    που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί  Αρχικοποιούνται ως πραγματική κάτι\n\n  
    συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    Για να αντιμετωπίσουμε πιθανό σφάλματα Division Error που\n\n  
    αφορά διαίρεση με το 0  αρχικοποιούμε  σε τιμή ίση με  1.0\n
    και ταυτόχρονα αποκτάμε προαιρετική χρήση μεθόδων άλλα και\n\n  
    επιλογή ποια ορίσματα θέλουμε.\n\n  
    ### Documentation\n
    The Financial Leverage Radio class \n
    encapsulates all those accounts that its methods use.\n 
    This accounts are initialized as real something \n
    common in the way of representation in accounting.\n 
    To deal with possible Division Error errors related to division by 0\n
    we initialize to a value equal to 1.0\n 
    and at the same time get optional use\n
    of other methods and choice of which arguments we want.
    +method :
        value_total_capital-> float
        net_profit_margin-> float
        asset_turnover_velocity-> float
        return_total_capital_employed-> float

    """
    def __init__(self,
        net_profits:float=1.0,
        interest: float=1.0,
        total_capital:float=1.0,
        tax_rate: float=1.0,
        net_sales:float=1.0):
        self.net_profits = net_profits
        self.interest = interest
        self.total_capital = total_capital
        self.tax_rate =tax_rate
        self.net_sales =  net_sales 


    def value_total_capital(self)-> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος αξία του συνολικού κεφαλαίου , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n 
        ### Documentation\n
        The total capital value method inherits Accounts from the ReturnTotalCapitalEmployed class.\n 
        ### return: round(((self.net_profits + self.interest * (1-self.tax_rate))/self.total_capital), 8)
        """
        return round(((self.net_profits + self.interest * (1-self.tax_rate))/self.total_capital), 8)
    
    def net_profit_margin(self)-> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος περιθώριο καθαρού κέρδους , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n 
        ### Documentation\n
        The net_profit_margin method inherits Accounts from the ReturnTotalCapitalEmployed class.\n 
        ### Returns: round(((self.net_profits + self.interest*(1 - self.tax_rate))/self.net_sales), 2)
        """
        return round(((self.net_profits + self.interest*(1 - self.tax_rate))/self.net_sales), 2)
    
    def asset_turnover_velocity(self)-> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος ταχύτητα κύκλου εργασιών , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n 
        ### Documentation\n
        The asset turnover velocity method inherits Accounts from the ReturnTotalCapitalEmployed class.\n 
        ### return round((self.net_sales/self.total_capital), 2)     
        """
        return round((self.net_sales/self.total_capital), 2)
    
    def return_total_capital_employed(self)-> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος ταχυτητα κυκλοφοριας ενεργητικου , κληρονομεί τους λογαριασμούς από την ReturnTotalCapitalEmployed κλάση.\n 
        ### Documentation\n
        The asset turnover velocity method inherits Accounts from the ReturnTotalCapitalEmployed class.\n 
        ### return round((self.net_profit_margin()/self.asset_turnover_velocity()), 2)
        """
        return round((self.net_profit_margin()/self.asset_turnover_velocity()), 2)
    