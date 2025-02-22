

class MetaFunc:
    "Documentation function "

class MetaActivityRadio:
    """ActivityRadio Documentation
    """

    def inventories_turnover_radio(self) -> float:
        """
        ### Τεκμηρίωση\n
        Ταχύτητα κυκλοφορίας αποθέματος είναι πόσες  φόρε  ανανεώνετε το
        απόθεμα σε σχέση με κόστος πωληθέντων.\n Κρίνετε σημαντικό
        να τονίσουμε  ότι  απόθεμα σε  αυτή μέθοδο
        εξετάζετε ως μέσο και όχι ως  συνολικό!\n
        Άρα προσοχή την εισαγωγή  δεδομένων. \n
        ### Documentation\n
        Inventory turnover is how often you renew
        inventory relative to cost of goods sold.\n
        Consider it important to emphasize that stock in this method\
            is considered as an average and not as a total!\n
        So be careful when entering data.\n
        Args:
            cost_of_goods_sold (float) \n
            average_stock (float) \n
        Returns:
            float: self.cost_of_goods_sold / self.average_stock
        """

    def average_dwell_time_of_inventory_in_the_warehouse(self) -> float:
        """
        ### Τεκμηρίωση\n\
        Ο Μέσος χρόνος παραμονής αποθέματος στην αποθήκη σε ήμερες
        περιλαμβάνει της προεπιλεγμένη μεταβλητή ήμερες
        που είναι ίσες με 365 ήμερες.\n\
        Αρχικά Αυτή η μέθοδος δημιουργείτε μια σχέση γινόμενου ήμερες * Μεσώ απόθεμα  και\n\
        κατόπιν διαιρείτε  με το  κόστος πωληθέντων.\n\
        ### Documentation\n\
        The Average time in warehouse in days includes the default variable days which is equal to 365 days.\n
        First This method creates a product relationship of days * Average inventory and then divides by cost of goods sold.\n
        Args:
            self.cost_of_goods_sold (float)\n\
            self.average_stock (float)\n\
            self.days (int, optional)\n\
        Returns:
            float: self.days * self.verage_stock) / self.cost_of_goods_sold
        """

    def speed_of_collection_of_receivables(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η ταχύτητα είσπραξης απαιτήσεων περιλαμβάνουν την σχέση\
              Πώλησης επί πίστωση προς μέσος όρος απαιτήσεων.
        ### Documentation\n
        The speed of collection of receivables includes the ratio\
              of Sales on credit to average receivables.
        Args:
            sale_on_credit (float): Πωλησης επι πιστωση
            average_requirement (float): μεσος ορος απαιτήσεων
        Returns:
            float: ταχύτητα είσπραξης απαιτήσεων
        """

    def average_demand_period(self) -> float:
        """
        ## Τεκμηρίωση\n
        ### Μέσος Χρόνος Είσπραξης Απαιτήσεων
        ΟΜέσος Χρόνος Είσπραξης Απαιτήσεων που αφορούν\
              πώλησης επί πίστωση ανά ήμερα .
        ## Documentation\n
        ### Average Claims Collection Time
        Average Collection Time of Receivables related\
              to sales on credit per day.
        Args:
            sale_on_credit (float): Πωλησης επι πιστωση
            average_requirement (float): μεσος ορος απαιτήσεων
            days (int, optional): Defaults to 365.

        Returns:
            float: μεσος χρονος απαιτησεων"""
    
    def business_cycle(self) -> float:
        """
        ### Τεκμηρίωση\n\
        Ο  δείκτης  λειτουργικός κύκλος της επιχείρησης,
        παρακολουθεί την ταχύτητα είσπραξης των απαιτήσεων \
            και μέσο χρόνο παραμονής των εμπορευμάτων σε μια  αποθήκη.
        ### Documentation\n\
        The operating cycle index of the business monitors \
            the speed of collection of receivables and the average time the goods stay in a warehouse.
        Args:
            Average_dwell_time_of_inventory_in_the_warehouse \
                :func()) -> float: Μέσος χρόνος παραμονής του αποθέματος στην αποθήκη
            speed_of_collection_of_receivables :func() -> float:\
                  ταχύτητα είσπραξης των απαιτήσεων
        Returns:
            float: λειτουργικος κύκλος της επιχειρησης
        """

    def velocity_of_current_liabilities(self) -> float:
        """
        ### Τεκμηρίωση\n
        Ο  δείκτης ταχύτητας των βραχυπρόθεσμων υποχρεώσεων,\
                παρακολουθεί τις  αγορές(που περιλαμβάνονται\
                      σε αυτές τις αγορές των αιτημάτων  προϊόντων
        για μεταπώληση άλλα και για παραγωγή \
              σε  ημιτελών προϊόντων, πρώτες ύλες , βοηθητικές ύλες )
        και την ανάλογη αύξηση ή μείωση της βραχυπρόθεσμες \
              υποχρεώσεις (όπως γραμματεία πληρωτέα, επιταγές πληρωτέες, λογαριασμός προμηθευτών.
        ### Documentation\n
        The speed index of short-term liabilities monitors purchases (which are included
        in these purchases of product requests for \
            resale other than for production in unfinished products, raw materials,
        auxiliary materials) and the corresponding increase or decrease
        in short-term liabilities (such as accounts payable, checks payable, accounts payable.
        Args:
            sourcing (float): αγορες
            medium_term_short_term_liabilities (float): Μ.Ο. βραχυπρόθεσμων υποχρεώσεων

        Returns:
            float: ταχύτητα βραχυπρόθεσμων υποχρεώσεων
        """

    def average_repayment_period_of_short_term_liabilities(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η μέση περίοδος αποπληρωμής των βραχυπρόθεσμων\
        υποχρεώσεων είναι ένα μέσος  όρος\
        αξιόλογη κάλυψη υποχρεώσεων στην διάρκεια ενός έτους \
        συγκρινόμενο  με τις  πωλήσεις .
        ### Documentation\n
        The average payback period of short-term \
            liabilities is an average creditable
        coverage of liabilities over the course of a year compared to sales.
        Args:
            medium_term_short_term_liabilities (float):\
                    Μ.Ο. βραχυπρόθεσμων υποχρεώσεων
            sourcing (float): αγορες
            days (int, optional):  Defaults to 365.
        Returns:
            float: μέση περίοδος αποπληρωμής των βραχυπρόθεσμων υποχρεώσεων
        """

    def net_working_capital_turnover_speed(self) -> float:
        """
        ### Τεκμηρίωση\n
        ταχύτητα κυκλοφορία καθαρού κεφαλαίου κίνησης είναι ο δικτης
        οπου Αξιολόγηση, αποτελεσματικότητα του κεφάλαιο κίνησης σε \
              σχέση με τις πωλητή.
        ### Documentation\n
        Νet working capital circulation velocity is the divisor
        where Evaluation, efficiency of working capital in relation\
              to the seller.
        Args:
            net_working_capital (float): καθαρό κεφάλαιο κίνησης
            net_sales (float): καθαρες πωλησης

        Returns:
            float: ταχύτητα κυκλοφορία καθαρού κεφαλαίου κίνησης
        """
    
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

    def traffic_speed_net_profit(self) -> float:
        """
        ### Τεκμηρίωση\nταχυτητα κυκλοφοριας ιδιων κεφαλαιων\n
        Αυτός ο αριθμοδείκτης μας δείχνει πόσες φορές τα \
            ίδια κεφάλαια ανανεώνεται
        ή ανακτάται μέσω των πωλήσεων. Πως λειτουργεί εχουμε την Επιχειρηση Χ
        που πραγματοποιησε πώλησης 1.400.000 και τα ίδια κεφάλαια
        είναι   1.000.000 τότε αποτέλεσμα ειναι 1,4.
        Αρα  η επιχειρηση κέρδισε επιπλων κεφάλαια 400.000 απο της πώλησης\
             ή 40 % επιπλεων κεφαλαια.
        ### Documentation\n
        This ratio shows us how many times equity is renewed or recouped \
            through sales.
        How does it work, we have Company X that sold 1,400,000 and the equity\
            is 1,000,000 then the result is 1.4.
        So the business earned an additional capital of 400,000 from the \
            sale or 40% of the additional capital.
            Args:
                net_sales (float): καθαρές πωλήσεις
                net_profit (float):ίδια κεφάλαια
            Returns:
                float: traffic_speed_net_profit
        """

class MetaLiquidityRadios:
    """LiquidityRadios Documentation
    """

    def current_radio(self) -> float:
        """### Αριθμοδείκτης Γενικής
        ### ή έμμεσης ρευστότητας
        ### Args: 
            + circulating_assets
            + short_term_liabilities
        Returns:
            float: _description_
        """
        pass    
    
    def cash_radio(self) -> float:
        """### Αριθμοδείκτης ταμειακής ρευστότητας
        ### Args: 
            + available_cash
            + short_term_liabilities
        Returns:
            float: _description_
        """
        pass

    def defensive_interval(self) -> float:
        """### Το αμυντικό διάστημα
        ### Args: 
            + circulating_assets
            + forecast_daily_expenses
        Returns:
            float: _description_
        """
        pass
    
    def net_working_capital(self) -> float:
            """### καθαρο κεφαλαιο κινησης
            ### Args: 
            + short_term_liabilities
            + circulating_assets
            Returns:
                float: _description_
            """
            pass

    def acid_test_radio(self) -> float:
        """### Άμεση ρευστότητα
            ### Args: 
            + circulating_assets
            + stocks
            Returns:
                float: _description_
            """
        pass

    def quick_radio(self) -> float:
            """### Άμεση ρευστότητα
            ### Args: 
            + requirements
            + available_cash
            + short_term_liabilities
            Returns:
                float: _description_
            """
            pass


class MetaEquityCapital:
    """LiquidityRadios Documentation"""

    def net_profit_margin(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος καθαρό περιθώριο κέρδους, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n
        ### Documentation\n
        The net profit marginmethod inherits Accounts from the EquityCapital class.
        ### Returns: round((self.net_profits/self.net_sales), 2)
        """
        pass

    def asset_turnover_velocity(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η μέθοδος ταχυτητα κυκλοφοριας ενεργητικου, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n
        ### Documentation\n
        The asset turnover velocity inherits Accounts from the EquityCapital class.
        ### Returns:round((self.net_sales/self.asset), 2)
        """
        pass

    def financial_leverage(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η χρηματοοικονομικη μόχλευση, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n
        ### Documentation\n
        The financial leverage method inherits Accounts from the EquityCapital class.
        ### Returns: round((self.asset/self.equity_capital), 2)
        """
        pass

    def equity_multiplier(self) -> float:
        """
        ### Τεκμηρίωση\n
        Ο πολλαπλασιαστή ιδίων κεφαλαίων, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n
        Η μεθοδος απεικονίζει το άθροισμα των γινομενων τριων συναρτησεων.\n
        ### Documentation\n
        The equity multiplier  method inherits Accounts from the EquityCapital class.
        The method displays the sum of the products of three functions.\n
        ### Returns: round((self.net_profit_margin()*self.asset_turnover_velocity()*self.financial_leverage()), 2)
        """
        pass

    def restatement_equity_multiplier(self) -> float:
        """
        ### Τεκμηρίωση\n
        Η επαναδιατύπωσης πολλαπλασιαστή ιδίων κεφαλαίων, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση\n
        Η μεθοδος απεικονίζει το αποτέλεσμα διαίρεσης του μεγεθους καθαρα κερδη / ιδια κεφαλαια .\n
        ### Documentation\n
        The equity multiplier  method inherits Accounts from the EquityCapital class.
        The method depicts the result of dividing the size net profit / equity.\n
        ### Returns: round((self.net_profits/self.equity_capital), 2)
        """
        pass