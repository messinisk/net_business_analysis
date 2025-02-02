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
    equity_capital = """[Τεκμηρίωση equity_capital]
[Ίδια κεφάλαια (καθαρή περιουσιακή θέση) είναι ό,τι βρίσκεται στην κυριότητά σας εάν αφαιρέσετε διάφορες χρεώσεις που σας επιβαρύνουν ή τα χρήματα που δανειστήκατε για να το αγοράσετε.]
[Όταν επενδύετε, ίδια κεφάλαια είναι οι μετοχές που σας παρέχουν ένα μερίδιο κυριότητας σε μια εταιρεία.]
[Documentation equity_capital]
[Equity (net worth) is what you own if you subtract various charges you incur or money borrowed to buy.]
[When you invest, equity is the shares that give you an ownership stake in a company.]
"""





class EquityCapital:
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
        +net_profit_margin
        +asset_turnover_velocity
        +financial_leverage
        +equity_multiplier
        +Restatement_equity_multiplier
    """
    def __init__(self,
        net_profits:float=1.0,
        net_sales: float=1.0,
        fixed_asset: float=1.0,
        equity_capital: float=1.0
        )->None:
        self.net_profits = net_profits
        self.net_sales =net_sales
        self.fixed_asset = fixed_asset
        self.equity_capital = equity_capital

    
    def net_profit_margin(self)->float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος καθαρό περιθώριο κέρδους, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n 
        ### Documentation\n
        The net profit marginmethod inherits Accounts from the EquityCapital class.
        ### Returns: round((self.net_profits/self.net_sales), 2)
        """
        return round((self.net_profits/self.net_sales), 2)

    def asset_turnover_velocity(self)->float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος ταχυτητα κυκλοφοριας ενεργητικου, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n 
        ### Documentation\n
        The asset turnover velocity inherits Accounts from the EquityCapital class.
        ### Returns:round((self.net_sales/self.asset), 2)
        """
        return round((self.net_sales/self.asset), 2)

    def financial_leverage(self)->float:
        """
        ### Τεκμηρίωση\n
        Η χρηματοοικονομικη μόχλευση, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n 
        ### Documentation\n
        The financial leverage method inherits Accounts from the EquityCapital class.
        ### Returns: round((self.asset/self.equity_capital), 2)
        """
        return round((self.fixed_asset/self.equity_capital), 2)

    def equity_multiplier (self)->float:
        """
        ### Τεκμηρίωση\n
        Ο πολλαπλασιαστή ιδίων κεφαλαίων, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n 
        Η μεθοδος απεικονίζει το άθροισμα των γινομενων τριων συναρτησεων.\n
        ### Documentation\n
        The equity multiplier  method inherits Accounts from the EquityCapital class.
        The method displays the sum of the products of three functions.\n
        ### Returns: round((self.net_profit_margin()*self.asset_turnover_velocity()*self.financial_leverage()), 2)
        """
        return round((self.net_profit_margin()*self.asset_turnover_velocity()*self.financial_leverage()), 2)
    
    def restatement_equity_multiplier(self)-> float:
        """
        ### Τεκμηρίωση\n
        Η επαναδιατύπωσης πολλαπλασιαστή ιδίων κεφαλαίων, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n 
        Η μεθοδος απεικονίζει το αποτέλεσμα διαίρεσης του μεγεθους καθαρα κερδη / ιδια κεφαλαια .\n
        ### Documentation\n
        The equity multiplier  method inherits Accounts from the EquityCapital class.
        The method depicts the result of dividing the size net profit / equity.\n
        ### Returns: round((self.net_profits/self.equity_capital), 2)
        """
        return round((self.net_profits/self.equity_capital), 2)




