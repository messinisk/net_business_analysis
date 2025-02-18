

"""
El:Αυτή η μονά περιλαμβάνει μεθόδους εκτιμούν
την δραστηριότητα  της επιχείρησης.
En:This single includes methods appreciate
the business activity
"""


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
        if self.average_stock > 0 and self.cost_of_goods_sold > 0:
            return round(self.cost_of_goods_sold / self.average_stock, 2)
        else:
            if self.cost_of_goods_sold < 0 and self.average_stock < 0:
                if self.average_stock < 0:
                    self.average_stock = abs(self.average_stock)
                    raise TypeError("Ο λογαριασμός average_stock\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")
                if self.cost_of_goods_sold < 0:
                    self.cost_of_goods_sold = abs(self.cost_of_goods_sold)
                    raise TypeError("Ο λογαριασμός cost_of_goods_sold\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")

            if self.average_stock == 0 or  self.cost_of_goods_sold ==0:
                raise ZeroDivisionError("Αυτη η πραξη δεν μπορει να πραγματοποιηθεί ['0/0', 'numbers/0']")
                return " "
       
            return abs(round(self.cost_of_goods_sold / self.average_stock, 2))

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
        if self.average_stock > 0 and self.cost_of_goods_sold > 0:
            return round((self.days * self.average_stock) / self.cost_of_goods_sold, 2)
        else:
            if self.cost_of_goods_sold < 0 and self.average_stock < 0 :
                if self.average_stock < 0:
                    self.average_stock = abs(self.average_stock)
                    raise TypeError("Ο λογαριασμός average_stock\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")
                if self.cost_of_goods_sold < 0:
                    self.cost_of_goods_sold = abs(self.cost_of_goods_sold)
                    raise TypeError("Ο λογαριασμός cost_of_goods_sold\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")

            if self.average_stock == 0 or  self.cost_of_goods_sold ==0:
                raise ZeroDivisionError("Αυτη η πραξη δεν μπορει να πραγματοποιηθεί ['0/0', 'numbers/0']")
       
            return abs(round((self.days * self.average_stock) / self.cost_of_goods_sold, 2))
        

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
        if self.sale_on_credit > 0 and self.average_requirement > 0:
            return round(self.sale_on_credit / self.average_requirement, 2)
        else:
            if self.sale_on_credit < 0 and self.average_requirement < 0:
                if self.sale_on_credit < 0:
                    self.sale_on_credit = abs(self.sale_on_credit)
                    raise TypeError("Ο λογαριασμός average_stock\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")
                if self.average_requirement < 0:
                    self.average_requirement = abs(self.average_requirement)
                    raise TypeError("Ο λογαριασμός cost_of_goods_sold\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")

            if self.sale_on_credit == 0 or  self.average_requirement == 0:
                raise ZeroDivisionError("Αυτη η πραξη δεν μπορει να πραγματοποιηθεί ['0/0', 'numbers/0']")
       
            return abs(round(self.sale_on_credit / self.average_requirement, 2))

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
        if self.average_requirement > 0 and self.sale_on_credit > 0:
            return round((self.days * self.average_requirement) / self.sale_on_credit, 2)
        else:
            if self.average_requirement < 0 and self.sale_on_credit < 0:
                if self.average_requirement < 0:
                    self.average_requirement = abs(self.average_requirement)
                    print("Ο λογαριασμός average_stock\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")
                if self.sale_on_credit < 0:
                    self.sale_on_credit = abs(self.sale_on_credit)
                    print("Ο λογαριασμός cost_of_goods_sold\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")

            if self.average_requirement == 0 or  self.sale_on_credit ==0:
                print("Αυτη η πραξη δεν μπορει να πραγματοποιηθεί ['0/0', 'numbers/0']")
                return " "
       
            return abs(round((self.days * self.average_requirement) / self.sale_on_credit, 2))


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
        try:
            the_warehouse_average = self.average_dwell_time_of_inventory_in_the_warehouse()
            collection_of_receivables = self.speed_of_collection_of_receivables()
            if the_warehouse_average > 0 and collection_of_receivables > 0:
                return round(the_warehouse_average + collection_of_receivables, 2)
        except ZeroDivisionError:
            print("προκληθηκε ZeroDivisionError επανεξεταστε τα δεδομενα ")
            return 0.0

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
        if self.sourcing > 0 and self.medium_term_short_term_liabilities > 0:
            return round(self.sourcing / self.medium_term_short_term_liabilities, 2)
        else:
            if self.sourcing < 0 and self.average_requirement:
                if self.sourcing < 0:
                    self.sourcing = abs(self.sourcing)
                    print("Ο λογαριασμός average_stock\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")
                if self.medium_term_short_term_liabilities < 0:
                    self.medium_term_short_term_liabilities = abs(self.medium_term_short_term_liabilities)
                    print("Ο λογαριασμός cost_of_goods_sold\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")

            if self.sourcing == 0 or  self.medium_term_short_term_liabilities ==0:
                print("Αυτη η πραξη δεν μπορει να πραγματοποιηθεί ['0/0', 'numbers/0']")
                return " "
       
            return abs(round(self.sourcing / self.medium_term_short_term_liabilities, 2))

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
        if self.sourcing > 0 and self.medium_term_short_term_liabilities > 0:
            return round((self.medium_term_short_term_liabilities * self.days) / self.sourcing, 2)
        else:
            if self.sourcing < 0 and self.average_requirement:
                if self.sourcing < 0:
                    self.sourcing = abs(self.sourcing)
                    print("Ο λογαριασμός average_stock\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")
                if self.medium_term_short_term_liabilities < 0:
                    self.medium_term_short_term_liabilities = abs(self.medium_term_short_term_liabilities)
                    print("Ο λογαριασμός cost_of_goods_sold\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")

            if self.sourcing == 0 or  self.medium_term_short_term_liabilities ==0:
                print("Αυτη η πραξη δεν μπορει να πραγματοποιηθεί ['0/0', 'numbers/0']")
                return " "
       
            return abs(round((self.medium_term_short_term_liabilities * self.days) / self.sourcing, 2))


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
        if self.net_sales > 0 and self.net_working_capital > 0:
            return round(self.net_sales / self.net_working_capital, 2)
        else:
            if self.net_sales < 0 and self.net_working_capital:
                if self.net_sales < 0:
                    self.net_sales = abs(self.net_sales)
                    print("Ο λογαριασμός average_stock\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")
                if self.net_working_capital < 0:
                    self.net_working_capital = abs(self.net_working_capital)
                    print("Ο λογαριασμός cost_of_goods_sold\nείχε αρνητικό πρόσημο και\nαυτόματα μετατράπηκε σε θετικό")

            if self.net_sales == 0 or  self.net_working_capital ==0:
                print("Αυτη η πραξη δεν μπορει να πραγματοποιηθεί ['0/0', 'numbers/0']")
                return " "
       
            return abs(round(self.net_sales / self.net_working_capital, 2))



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
    

# if __name__ == "__main__":
#     run = ActivityRadio(cost_of_goods_sold= -500, average_stock = 8000, sale_on_credit  = 10_000, average_requirement = 5000 )
#     print(run.business_cycle())
