

"""
El:Αυτή η μονά περιλαμβάνει μεθόδους εκτιμούν
την δραστηριότητα  της επιχείρησης.
En:This single includes methods appreciate
the business activity
"""
class MetaData:
    """## Return:  meta data """
    cost_of_goods_sold = """[Τεκμηρίωση cost_of_goods_sold]
[Βασικό στοιχείο που επηρεάζει τα μικτά αποτελέσματα της χρήσης είναι το κόστος των πωληθέντων αποθεμάτων.]
[Το κόστος πωλήσεων περιλαμβάνει τη διαφορά μεταξύ των κονδυλίων «κύκλος εργασιών» και «μικτά αποτελέσματα εκμεταλλεύσεως».   ]\n[Documentation cost_of_goods_sold]
[A key factor affecting the mixed results for the year is the cost of inventory sold. ]
[Cost of sales includes the difference between 'turnover' and 'gross operating results]'."""
    average_stock="""[Τεκμηρίωση average_stock]
[Το μέσο απόθεμα ανέρχεται στο μισό του μέγιστου αποθέματος ( [παραγωγή ανά ημέρα - ζήτηση ανά ημέρα] χ περίοδος παραγωγής σε ημέρες).]
[Documentation average_stock]\n[The average inventory is half of the maximum inventory ( [production per day - demand per day] x production period in days).          ]
"""
    sale_on_credit = """[Τεκμηρίωση sale_on_credit]\n[Παραστατικό πώλησης επί πιστώσει είναι ένα παραστατικό - τιμολόγιο - απόδειξη που εκδίδει μία επιχείρηση όταν αγοράζουν από αυτήν προϊόντα ή υπηρεσίες, που υποδηλώνει ότι θα πληρωθούν στο μέλλον με δόσεις.]
[Είναι δηλαδή ένα είδος πίστωσης που παρέχει στους πελάτες της, ώστε να τους διευκολύνει να μην πληρώσουν άμεσα τα χρήματα που απαιτούνται, αλλά με δόσεις, στο μέλλον. ]
[Documentation sale_on_credit]\n[A credit sales document is a document - invoice - receipt issued by a business when they buy products or services from it, indicating that they will be paid in the future in installments.]
[That is, it is a type of credit that it provides to its customers, in order to make it easier for them not to pay the money required immediately, but in installments, in the future.]
"""
    average_requirement = """[Τεκμηρίωση average_requirement]\n[Οι απαιτήσεις γενικά δημιουργούνται μέσω των πωλήσεων αποθεμάτων μιας επιχείρησης,]
[παρακολουθούνται μέσω των λογαριασμών όπως  Πελάτες αλλά κύριος από Γραμμάτια Εισπρακτέα, επιταγές Εισπρακτέες που διαθέτουν μια προκαθορισμένη προθεσμία εξόφλησής.]
[Συμφωνά με την βιβλιογραφία απαίτησης μπορούν να εμφανίζονται και σε προς τρίτους και όσο  και παροχές προσωπικού παροχή πίστωσης.]
[Κατά συνέπια τον παραπάνω το μεσώ απαιτήσεις είναι Μέσος Όρος των   απαιτήσεων μια συγκεκριμένης περιόδου. ]
[Documentation average_requirement]
[Receivables are generally created through a business's sales of inventory, tracked through accounts such as Accounts Payable but principal from Notes Receivable, checks Receivable that have a predetermined maturity date.]
[According to the claim literature they can appear in third party and personal benefits credit provision. As a result of the above, the average requirements is the average of the requirements of a certain period.]
"""
    medium_term_short_term_liabilities = """[Τεκμηρίωση medium_term_short_term_liabilities]
[Βραχυπρόθεσμες υποχρεώσεις είναι εκείνες για τις ποίες η προθεσμία εξοφλήσεώς τους λήγει μέχρι το τέλος της επόμενης χρήσεως και Αποτελούν Έξοδο για την επιχείρηση.]
[Κατά συνέπια τον παραπάνω  εδώ αναφερόμαστε Μέσος Όρος των Βραχυπρόθεσμων υποχρεώσεων  μια συγκεκριμένης περιόδου.]
[Documentation medium_term_short_term_liabilities]
[Short-term liabilities are those for which their repayment term expires by the end of the next fiscal year and constitute an Outgo for the business.]
[As a result of the above, here we refer to the Average Term of the Short-term obligations of a specific period.]
"""
    sourcing = """[Τεκμηρίωση sourcing]
[Αγορές που περιλαμβάνονται όπως αυτές αιτημάτων προϊόντων για μεταπώληση, άλλα και για παραγωγή σε ημιτελών προϊόντων, πρώτες ύλες , βοηθητικές ύλες.]
[Documentation sourcing]
[Purchases included such as those of product requests for resale, others and for production of unfinished products, raw materials, auxiliary materials.]
"""
    net_working_capital = """[Τεκμηρίωση net_working_capital]
[Καθαρό κεφάλαιο κίνησης είναι η διαφορά ανάμεσα στο κυκλοφορούν Ενεργητικό και τις βραχυπρόθεσμες Υποχρεώσεις]
[Documentation net_working_capital]
[Net working capital is the difference between current Assets and current Liabilities]
"""
    net_sales = """[Τεκμηρίωση net_sales]
[Η αξία των πωλήσεων μιας οικονομικής μονάδας μετά την αφαίρεση των φόρων (πχ. ΦΠΑ), των επιστροφών, των εκπτώσεων και της αξίας των κατεστραμμένων προϊόντων]
[Documentation net_sales]
[The value of sales of an economic unit after deduction of taxes (e.g. VAT), returns, discounts and the value of damaged products]
"""
    total_assets = """[Τεκμηρίωση total_assets]
[Εξετάζοντας τα περιουσιακά στοιχεία του Ενεργητικού διαπιστώνουμε ότι:]
[Μερικά από αυτά, όπως είναι οικόπεδα, κτίρια, μηχανήματα, μεταφορικά μέσα, έπιπλα και λοιπός εξοπλισμός, διπλώματα ευρεσιτεχνίας κτλ.]
[αποτελούν μόνιμο εξοπλισμό της επιχείρησης και προορίζονται να την εξυπηρετούν για χρονικό διάστημα μεγαλύτερο του έτους. Αυτά λέγονται Πάγια.]
[Άλλα περιουσιακά στοιχεία του Ενεργητικού, όπως είναι πελάτες, πρώτες και βοηθητικές ύλες, έτοιμα, προϊόντα, χρεόγραφα, γραμμάτια εισπρακτέα, ταμείο κτλ.]
[προορίζονται να υφίστανται συνεχείς μεταβολές στη διάρκεια της χρονιάς, π.χ. η πρώτη ύλη γίνεται έτοιμο προϊόν, το έτοιμο προϊόν μετρητά, τα μετρητά πρώτη ύλη κτλ.]
[Αυτά λέγονται Κυκλοφορούντα ή Κυκλοφοριακά.]
[Documentation total_assets]
[Examining the assets of the Asset we find that:]
[Some of them, such as land, buildings, machinery, means of transport, furniture and other equipment, patents, etc.]
[are permanent equipment of the company and are intended to serve it for a period longer than a year. This is what you call a fixed asset]
[Other assets of the Assets, such as customers, raw and auxiliary materials, finished products, securities, notes receivable, cash, etc.]
[are intended to undergo continuous changes during the year, e.g. raw material becomes finished product, finished product becomes cash, cash becomes raw material, etc.]
[This is what you call Current Assets]
"""
    net_assets = """[Τεκμηρίωση net_assets]
[Η καθαρή θέση επιχείρησης, επίσης γνωστή ως καθαρό ενεργητικό ή ίδια κεφάλαια, είναι η διαφορά μεταξύ του συνολικού ενεργητικού μιας εταιρείας και του συνολικού παθητικού της.]
[Αντιπροσωπεύει το εναπομένον ιδιοκτησιακό μερίδιο στα περιουσιακά στοιχεία της εταιρείας μετά την αφαίρεση όλων των υποχρεώσεών της.]
[Documentation net_assets]
[Business equity, also known as net assets or equity, is the difference between a company's total assets and its total liabilities.]
[It represents the remaining ownership stake in the company's assets after deducting all of its liabilities.]
"""
    invested_capital = """[Τεκμηρίωση invested_capital]
[Είναι το σύνολο των  κεφάλαιον που έχει επενδυθεί στην επιχείρηση, συμπεριλαμβανομένων των ιδίων κεφαλαίων και του μακροπρόθεσμων υποχρεώσεων (χρέος σε τρίτους).]
[Documentation invested_capital]
[It is the total amount of capital that has been invested in the business, including equity and long-term liabilities (debt to third parties).]
"""
    net_profit = """[Τεκμηρίωση net_profit]
[Στις επιχειρήσεις, το καθαρό εισόδημα ή τα καθαρά κέρδη είναι τα έσοδα μείον το κόστος πωληθέντων αγαθών, τα έξοδα και τους φόρους για μια λογιστική χρήση.]
[Documentation net_profit]
[In business, net income or net profit is revenue minus cost of goods sold, expenses, and taxes for an accounting year.]
"""

    def __str__(self):
        attributes = [
            self.cost_of_goods_sold,
            self.average_stock,
            self.sale_on_credit,
            self.average_requirement,
            self.medium_term_short_term_liabilities,
            self.sourcing,
            self.net_working_capital,
            self.net_sales,
            self.total_assets,
            self.net_assets,
            self.invested_capital,
            self.net_profit,
        ]
        return "\n\n".join(map(str, attributes))




class ActivityRadio:
    def __init__(self,
        cost_of_goods_sold: float =  1.0,
        average_stock = 1.0,
        days: int = 365,
        sale_on_credit: float = 1.0,
        average_requirement: float = 1.0,
        medium_term_short_term_liabilities: float= 1.0,
        sourcing: float= 1.0,
        net_working_capital: float= 1.0,
        net_sales: float= 1.0,
        total_assets: float=1.0,
        net_assets: float = 1.0,
        invested_capital: float = 1.0,
        net_profit: float = 1.0)-> None:
        self.cost_of_goods_sold = cost_of_goods_sold
        self.average_stock = average_stock
        self.days = days
        self.sale_on_credit = sale_on_credit
        self.average_requirement = average_requirement
        self.medium_term_short_term_liabilities = medium_term_short_term_liabilities
        self.sourcing = sourcing
        self.net_working_capital = net_working_capital
        self.net_sales = net_sales
        self.total_assets =  total_assets
        self.net_assets = net_assets
        self.invested_capital = invested_capital
        self.net_profit = net_profit

    def inventories_turnover_radio(self) -> float:
        """
        ### Τεκμηρίωση\n
        Ταχύτητα κυκλοφορίας αποθέματος είναι πόσες  φόρε  ανανεώνετε το  απόθεμα σε σχέση με κόστος πωληθέντων.\n
        Κρίνετε σημαντικό  να τονίσουμε  ότι  απόθεμα σε  αυτή μέθοδο  εξετάζετε ως μέσο και όχι ως  συνολικό!\n
        Άρα προσοχή την εισαγωγή  δεδομένων. \n
        ### Documentation\n
        Inventory turnover is how often you renew inventory relative to cost of goods sold.\n
        Consider it important to emphasize that stock in this method is considered as an average and not as a total!\n
        So be careful when entering data.\n
        Args:
            cost_of_goods_sold (float) \n
            average_stock (float) \n
        Returns:
            float: self.cost_of_goods_sold / self.average_stock
        """
        if self.average_stock <= 0:
            raise ValueError("average_stock must be positive.")
        return round(self.cost_of_goods_sold / self.average_stock, 2)

    def average_dwell_time_of_inventory_in_the_warehouse(self) -> float:
        """
        ### Τεκμηρίωση\n
        Ο Μέσος χρόνος παραμονής αποθέματος στην αποθήκη σε ήμερες
        περιλαμβάνει της προεπιλεγμένη μεταβλητή ήμερες
        που είναι ίσες με 365 ήμερες.\n
        Αρχικά Αυτή η μέθοδος δημιουργείτε  μια σχέση γινόμενου ήμερες * Μεσώ απόθεμα  και\n
        κατόπιν διαιρείτε  με το  κόστος πωληθέντων.\n
        ### Documentation\n
        The Average time in warehouse in days includes the default variable days which is equal to 365 days.\n
        First This method creates a product relationship of days * Average inventory and then divides by cost of goods sold.\n
        Args:
            self.cost_of_goods_sold (float)\n
            self.average_stock (float)\n
            self.days (int, optional)\n
        Returns:
            float: self.days * self.verage_stock) / self.cost_of_goods_sold
        """
        return round((self.days * self.average_stock) / self.cost_of_goods_sold, 2)

    def speed_of_collection_of_receivables(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η ταχύτητα είσπραξης απαιτήσεων περιλαμβάνουν την σχέση  Πώλησης επί πίστωση προς μέσος όρος απαιτήσεων.
        ### Documentation\n
        The speed of collection of receivables includes the ratio of Sales on credit to average receivables.
        Args:
            sale_on_credit (float): Πωλησης επι πιστωση
            average_requirement (float): μεσος ορος απαιτήσεων
        Returns:
            float: ταχύτητα είσπραξης απαιτήσεων
        """
        return round(self.sale_on_credit / self.average_requirement, 2)

    def average_demand_period(self) -> float:
        """
        ## Τεκμηρίωση\n
        ### Μέσος Χρόνος Είσπραξης Απαιτήσεων 
        ΟΜέσος Χρόνος Είσπραξης Απαιτήσεων που αφορούν πώλησης επί πίστωση ανά ήμερα .
        ## Documentation\n
        ### Average Claims Collection Time
        Average Collection Time of Receivables related to sales on credit per day.
        Args:
            sale_on_credit (float): Πωλησης επι πιστωση
            average_requirement (float): μεσος ορος απαιτήσεων
            days (int, optional): Defaults to 365.

        Returns:
            float: μεσος χρονος απαιτησεων"""
        return round((self.days * self.average_requirement) / self.sale_on_credit, 2)

    def business_cycle(self) -> float:
        """
        ### Τεκμηρίωση\n
        Ο  δείκτης  λειτουργικός κύκλος της επιχείρησης,
        παρακολουθεί την ταχύτητα είσπραξης των απαιτήσεων και μέσο χρόνο παραμονής των εμπορευμάτων σε μια  αποθήκη.
        ### Documentation\n
        The operating cycle index of the business monitors the speed of collection of receivables and the average time the goods stay in a warehouse.
        Args:
            Average_dwell_time_of_inventory_in_the_warehouse :func()) -> float: Μέσος χρόνος παραμονής του αποθέματος στην αποθήκη
            speed_of_collection_of_receivables :func() -> float: ταχύτητα είσπραξης των απαιτήσεων
        Returns:
            float: λειτουργικος κύκλος της επιχειρησης
        """

        return round((self.average_dwell_time_of_inventory_in_the_warehouse() + self.speed_of_collection_of_receivables()), 2)

    def velocity_of_current_liabilities(self) -> float:
        """
        ### Τεκμηρίωση\n
        Ο  δείκτης ταχύτητας των βραχυπρόθεσμων υποχρεώσεων,  παρακολουθεί τις  αγορές(που περιλαμβάνονται σε αυτές τις αγορές των αιτημάτων  προϊόντων
        για μεταπώληση άλλα και για παραγωγή    σε  ημιτελών προϊόντων, πρώτες ύλες , βοηθητικές ύλες )
        και την ανάλογη αύξηση ή μείωση της βραχυπρόθεσμες  υποχρεώσεις (όπως γραμματεία πληρωτέα, επιταγές πληρωτέες, λογαριασμός προμηθευτών.
        ### Documentation\n
        The speed index of short-term liabilities monitors purchases (which are included 
        in these purchases of product requests for resale other than for production in unfinished products, raw materials,
        auxiliary materials) and the corresponding increase or decrease 
        in short-term liabilities (such as accounts payable, checks payable, accounts payable.
        Args:
            sourcing (float): αγορες
            medium_term_short_term_liabilities (float): Μ.Ο. βραχυπρόθεσμων υποχρεώσεων

        Returns:
            float: ταχύτητα βραχυπρόθεσμων υποχρεώσεων
        """
        return round(self.sourcing / self.medium_term_short_term_liabilities, 2)

    def average_repayment_period_of_short_term_liabilities(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η μέση περίοδος αποπληρωμής των βραχυπρόθεσμων υποχρεώσεων είναι ένα μέσος  όρος
        αξιόλογη κάλυψη υποχρεώσεων στην διάρκεια  ενός έτους  συγκρινόμενο  με τις  πωλήσεις .
        ### Documentation\n
        The average payback period of short-term liabilities is an average creditable 
        coverage of liabilities over the course of a year compared to sales.
        Args:
            medium_term_short_term_liabilities (float):  Μ.Ο. βραχυπρόθεσμων υποχρεώσεων
            sourcing (float): αγορες
            days (int, optional):  Defaults to 365.
        Returns:
            float: μέση περίοδος αποπληρωμής των βραχυπρόθεσμων υποχρεώσεων
        """
        return round((self.medium_term_short_term_liabilities * self.days) / self.sourcing, 2)

    def net_working_capital_turnover_speed(self) -> float:
        """
        ### Τεκμηρίωση\n
        ταχύτητα κυκλοφορία καθαρού κεφαλαίου κίνησης είναι ο δικτης 
        οπου Αξιολόγηση, αποτελεσματικότητα του κεφάλαιο κίνησης σε  σχέση με τις πωλητή.
        ### Documentation\n
        Νet working capital circulation velocity is the divisor 
        where Evaluation, efficiency of working capital in relation to the seller.
        Args:
            net_working_capital (float): καθαρό κεφάλαιο κίνησης
            net_sales (float): καθαρες πωλησης

        Returns:
            float: ταχύτητα κυκλοφορία καθαρού κεφαλαίου κίνησης
        """
        return round(self.net_sales / self.net_working_capital, 2)

    def turnover_speed_total_assets(self) -> float:
        """
        ### Τεκμηρίωση\n
        Ακόμα ένα δείκτης οπού συγκρίνει
        συνολική αποδοτικότητα Ενεργητικού σε σχέση με καθαρές πώλησης.
        ### Documentation\n
        Another indicator where it compares
        total return on Assets relative to net sales.
        Args:
            total_assets (float): Ενεργητικό
            net_sales (float): Κάθαρες πώλησης

        Returns:
            float:  ταχύτητα κυκλοφορία συνολο ενεργητικου
        """
        return round(self.net_sales / self.total_assets, 2)

    def fixed_turnover_rate(self) -> float:
        """
        ### Τεκμηρίωση\n
        Γενικά δείκτης εκτίμα παραγωγικότητα συγκρίνοντας
        δυο  μεγέθη όπως  πώλησης / έτους και
        μέσο όρο καθαρόν πάγιων στοιχείων ( αφού αφαιρεθούν η αποσβέσεις).
        ### Documentation\n
        Generally index estimate productivity comparing
        two sizes such as sales / year and
        average net fixed assets (after deducting depreciation).
        Args:
            net_sales (float): Κάθαρες πώλησης
            net_assets (float): πάγια
        Returns:
            float: Ταχύτητα κυκλοφορίας Παγίων
        """
        return round(self.net_sales / self.net_assets, 2)

    def speed_of_circulating_invested_capital(self) -> float:
        """
        ### Τεκμηρίωση\n
        Τα απασολούμενα ή χρησιμοποιούμενο κεφάλαιο είναι
        ίδια κεφάλαια και μακροπρόθεμων υποχρεώσεων ή
        Καθαρό κεφάλαιο κίνησης και πάγια.
        Γενικά δείκτης πρέπει να είναι θετικός άνω του 1 (100%),
        μια πιο ουσιαστική ανάλυση όταν η τιμή δείκτη
        είναι κοντά εκείνη του κλάδου. Σε περιπτώσει που δείκτης
        είναι κάτω του 1 η επιχείρηση δεν διαχειρίζεται
        ορθολογικά τα κεφάλαια της.
        ### Documentation\n
        The disbursed or capital employed is
        equity and long-term liabilities or
        Net working capital and fixed assets.
        Generally the ratio should be positive above 1 (100%),
        a more meaningful analysis when the ratio value is close to that of the industry.
        In cases where the index is below 1, the company is not managing its funds rationally.
        Args:
            net_sales (float): καθαρες πωλησης
            invested_capital (float): χρησιμοποιούμενο κεφάλαιο
        Returns:
            float: ταχύτητα κυκλοφορουν απασχολουμενου κεφαλαίου
        """
        return round(self.net_sales / self.invested_capital, 2)

    def traffic_speed_net_profit(self) -> float:
        """
        ### Τεκμηρίωση\nταχυτητα κυκλοφοριας ιδιων κεφαλαιων\n
        Αυτός ο αριθμοδείκτης μας δείχνει πόσες φορές τα ίδια κεφάλαια ανανεώνεται
        ή ανακτάται μέσω των πωλήσεων. Πως λειτουργεί εχουμε την Επιχειρηση Χ
        που πραγματοποιησε πώλησης 1.400.000 και τα ίδια κεφάλαια
        είναι   1.000.000 τότε αποτέλεσμα ειναι 1,4.
        Αρα  η επιχειρηση κέρδισε επιπλων κεφάλαια 400.000 απο της πώλησης ή 40 % επιπλεων κεφαλαια.
        ### Documentation\n
        This ratio shows us how many times equity is renewed or recouped through sales.
        How does it work, we have Company X that sold 1,400,000 and the equity is 1,000,000 then the result is 1.4.
        So the business earned an additional capital of 400,000 from the sale or 40% of the additional capital.
            Args:
                net_sales (float): καθαρές πωλήσεις
                net_profit (float):ίδια κεφάλαια
            Returns:
                float: traffic_speed_net_profit
        """
        return round(self.net_sales / self.net_profit, 2)
    
