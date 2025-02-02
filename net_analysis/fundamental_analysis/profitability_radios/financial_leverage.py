""" submodule inancial_leverage
"""
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
    fixed_asset  = """[Τεκμηρίωση assets]
[Εξετάζοντας τα περιουσιακά στοιχεία του Ενεργητικού διαπιστώνουμε ότι:]
[Μερικά από αυτά, όπως είναι οικόπεδα, κτίρια, μηχανήματα, μεταφορικά μέσα, έπιπλα και λοιπός εξοπλισμός, διπλώματα ευρεσιτεχνίας κτλ.]
[αποτελούν μόνιμο εξοπλισμό της επιχείρησης και προορίζονται να την εξυπηρετούν για χρονικό διάστημα μεγαλύτερο του έτους. Αυτά λέγονται Πάγια.]
[Documentation assets]
[Examining the assets of the Asset we find that:]
[Some of them, such as land, buildings, machinery, means of transport, furniture and other equipment, patents, etc.]
[are permanent equipment of the company and are intended to serve it for a period longer than a year. This is what you call a fixed asset]
"""
    equity_capital = """[Τεκμηρίωση assets]
[Ίδια κεφάλαια (καθαρή περιουσιακή θέση) είναι ό,τι βρίσκεται στην κυριότητά σας εάν αφαιρέσετε διάφορες χρεώσεις που σας επιβαρύνουν ή τα χρήματα που δανειστήκατε για να το αγοράσετε.]
[Όταν επενδύετε, ίδια κεφάλαια είναι οι μετοχές που σας παρέχουν ένα μερίδιο κυριότητας σε μια εταιρεία.]
[Documentation equity_capital]
[Equity (net worth) is what you own if you subtract various charges you incur or money borrowed to buy.]
[When you invest, equity is the shares that give you an ownership stake in a company.]
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



class FinancialLeverageRadio:
    """
    ### Τεκμηρίωση\n
    Η κλάση δείκτη χρηματοοικονομικής μόχλευσης,\n
    ενσωματώνει όλους   εκείνους τους λογαριασμούς που χρησιμοποιούν οι μέθοδοι του.\n
    Αυτή οι λογαριασμοί  Αρχικοποιούνται ως πραγματική κάτι συνηθισμένο στον τρόπο απεικόνισης στην λογιστική.\n
    Για να αντιμετωπίσουμε πιθανό σφάλματα Division Error που αφορά διαίρεση με το 0  αρχικοποιούμε  σε τιμή ίση με  1.0\n
    και ταυτόχρονα αποκτάμε προαιρετική χρήση μεθόδων άλλα και  επιλογή ποια ορίσματα θέλουμε.\n\n  
    ### Documentation\n
    The Financial Leverage Radio class encapsulates all those accounts that its methods use.\n 
    This accounts are initialized as real something common in the way of representation in accounting.\n 
    To deal with possible Division Error errors related to division by 0 we initialize to a value equal to 1.0\n 
    and at the same time get optional use of other methods and choice of which arguments we want.
    method :
        +financial_leverage
        +economic_benefits
    """
    def __init__(self,
        net_profits:float=1.0,
        equity_capital:float=1.0,
        interest:int=1,
        tax_rate:int=1
        )->None:
        self.net_profits = net_profits
        self.equity_capital = equity_capital
        self.interest = interest
        self.tax_rate = tax_rate
        self.equity_capital = equity_capital
        


    def financial_leverage(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος οικονομική μόχλευση, κληρονομεί τους λογαριασμούς από την FinancialLeverageRadio κλάση.\n 
        ### Documentation\n
        The financial leverage method inherits Accounts from the FinancialLeverageRadio class.s\n
        return:
        ### asset_turnover_velocity = self.net_profits /self.equity_capital \n
        ###  equity_capital_efficiency = (self.net_profits + self.interest*(1 - self.tax_rate)) / self.equity_capital
        ### round((asset_turnover_velocity/equity_capital_efficiency) , 2)
        """
        asset_turnover_velocity = self.net_profits / (self.equity_capital or 1.0)
        equity_capital_efficiency = (self.net_profits + self.interest * (1 - self.tax_rate)) / (self.equity_capital or 1.0)
        if equity_capital_efficiency == 0:
            return 0  # Εναλλακτικά, μπορείτε να επιστρέψετε ένα μήνυμα
        return round((asset_turnover_velocity / equity_capital_efficiency), 2)
    
    def economic_benefits(self):
        """
        ### Τεκμηρίωση\n
        Η μέθοδος επωφελείστε οικονομικά, κληρονομεί τους λογαριασμούς από την FinancialLeverageRadio κλάση\n 
        Ουσιαστικά πραγματοποιείτε τρις διαφορετική λογική έλεγχοι σύγκριση με μέθοδο οικονομική μόχλευση \n
        που επιδιώκουμε να υπολογίσουμε το μέγεθος εδώ επιδιώκουμε καθορίζουμε  \n
        αν σύνθεση επιλεγομένων λογαριασμών έχουν κάποια θετική, ουδέτερη ή αρνητική επίδραση. \n     
        ### Documentation\n
        The The you benefit financiall method inherits Accounts from the FinancialLeverageRadio class.
        Essentially you carry out three different logical checks compared with the method
        of financial leverage that we seek to calculate the size here we seek to determine whether
        the composition of selected accounts have any positive, neutral or negative effect.
        """
        asset_turnover_velocity = self.net_profits / (self.equity_capital or 1.0)
        equity_capital_efficiency = (self.net_profits + self.interest * (1 - self.tax_rate)) / (self.equity_capital or 1.0)

        # ΣΥΝΘΗΚΕΣ
        if asset_turnover_velocity > equity_capital_efficiency:
            return "Borrowing is beneficial: Ο δανεισμός ειναι επωφελής "
        elif asset_turnover_velocity == equity_capital_efficiency:
            return "Borrowing has no effect: Ο δανεισμός δεν ασκεί καμία επίδραση "
        else:
            return "Borrowing is harmful: Ο δανεισμός είναι επιβλαβής "
                
            