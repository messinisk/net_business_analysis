- library activityradios
    - Module activityradios
        - class ActivityRadio
            - inventories_turnover_radio
                - Ταχύτητα κυκλοφορίας αποθέματος είναι πόσες  φόρε  ανανεώνετε το απόθεμα σε σχέση με κόστος πωληθέντων. Κρίνετε σημαντικό να τονίσουμε  ότι  απόθεμα σε  αυτή μέθοδο εξετάζετε ως μέσο και όχι ως  συνολικό!
                - Args:
                    - self.cost_of_goods_sold (float)\n\
                    - self.average_stock (float)\n\
                    - self.days (int, optional)\n\        
                - return float: self.cost_of_goods_sold / self.average_stock
            - average_dwell_time_of_inventory_in_the_warehouse
                - Ο Μέσος χρόνος παραμονής αποθέματος στην αποθήκη σε ήμερες περιλαμβάνει της προεπιλεγμένη μεταβλητή ήμερες
                που είναι ίσες με 365 ήμερες. Αρχικά Αυτή η μέθοδος δημιουργείτε μια σχέση γινόμενου ήμερες * Μεσώ απόθεμα και κατόπιν διαιρείτε  με το  κόστος πωληθέντων.
                - Args:
                    - sale_on_credit (float): Πωλησης επι πιστωση
                    - average_requirement (float): μεσος ορος απαιτήσεων
                - return float: (self.days * self.verage_stock) / self.cost_of_goods_sold

            - speed_of_collection_of_receivables
                - Η ταχύτητα είσπραξης απαιτήσεων περιλαμβάνουν την σχέση Πώλησης επί πίστωση προς μέσος όρος απαιτήσεων.
                -  Args:
                    - sale_on_credit (float): Πωλησης επι πιστωση
                    - average_requirement (float): μεσος ορος απαιτήσεων
                    - days (int, optional): Defaults to 365.
                -  Returns: 

            - business_cycle 
                - Ο  δείκτης  λειτουργικός κύκλος της επιχείρησης,
                παρακολουθεί την ταχύτητα είσπραξης των απαιτήσεων και μέσο χρόνο παραμονής των εμπορευμάτων σε μια  αποθήκη.
                - Args:
                    -Average_dwell_time_of_inventory_in_the_warehouse 
                            :func() -> float: Μέσος χρόνος παραμονής του αποθέματος στην αποθήκη
                    -speed_of_collection_of_receivables :func() -> float: ταχύτητα είσπραξης των απαιτήσεων
                - Returns: 

            - velocity_of_current_liabilities
                - Ο  δείκτης ταχύτητας των βραχυπρόθεσμων υποχρεώσεων, παρακολουθεί τις  αγορές(που περιλαμβάνονται σε αυτές τις αγορές των αιτημάτων  προϊόντων για μεταπώληση άλλα και για παραγωγή 
                σε  ημιτελών προϊόντων, πρώτες ύλες , βοηθητικές ύλες)
                και την ανάλογη αύξηση ή μείωση της βραχυπρόθεσμες \
                υποχρεώσεις όπως γραμματεία πληρωτέα, επιταγές πληρωτέες, λογαριασμός προμηθευτών.
                - Args:
                    - sourcing (float): αγορες
                    - medium_term_short_term_liabilities (float): Μ.Ο. βραχυπρόθεσμων υποχρεώσεων

                - Returns: 

            - average_repayment_period_of_short_term_liabilities
                -  Η μέση περίοδος αποπληρωμής των βραχυπρόθεσμων 
                υποχρεώσεων είναι ένα μέσος  όρος αξιόλογη κάλυψη υποχρεώσεων στην διάρκεια ενός έτους συγκρινόμενο  με τις  πωλήσεις.
                - Args:
                    - medium_term_short_term_liabilities (float):
                            Μ.Ο. βραχυπρόθεσμων υποχρεώσεων
                    - sourcing (float): αγορες
                    - days (int, optional):  Defaults to 365.
                - Returns: 

            - net_working_capital_turnover_speed
                - ταχύτητα κυκλοφορία καθαρού κεφαλαίου κίνησης είναι ο δικτης οπου Αξιολόγηση, αποτελεσματικότητα του κεφάλαιο κίνησης σε σχέση με τις πωλητή.
                -  Args:
                    - net_working_capital (float): καθαρό κεφάλαιο κίνησης
                    - net_sales (float): καθαρες πωλησης 
                - Returns:

            - turnover_speed_total_assets
                - Ακόμα ένα δείκτης οπού συγκρίνει
                συνολική αποδοτικότητα Ενεργητικού σε σχέση με καθαρές πώλησης.
                - Args:
                    - total_assets (float): Ενεργητικό
                    - net_sales (float): Κάθαρες πώλησης
                    - Returns:

            - fixed_turnover_rate
                - Γενικά δείκτης εκτίμα παραγωγικότητα συγκρίνοντας
                δυο  μεγέθη όπως  πώλησης / έτους και μέσο όρο καθαρόν πάγιων στοιχείων ( αφού αφαιρεθούν η αποσβέσεις).
                - Args:
                    - net_sales (float): Κάθαρες πώλησης
                    - net_assets (float): πάγια
                - Returns:

            - speed_of_circulating_invested_capital
                - Τα απασολούμενα ή χρησιμοποιούμενο κεφάλαιο είναι
                ίδια κεφάλαια και μακροπρόθεμων υποχρεώσεων ή
                Καθαρό κεφάλαιο κίνησης και πάγια. Γενικά δείκτης πρέπει να είναι θετικός άνω του 1 (100%), μια πιο ουσιαστική ανάλυση όταν η τιμή δείκτη είναι κοντά εκείνη του κλάδου. Σε περιπτώσει που δείκτης είναι κάτω του 1 η επιχείρηση δεν διαχειρίζεται ορθολογικά τα κεφάλαια της.
                - Args:
                    - net_sales (float): καθαρες πωλησης
                    - invested_capital (float): χρησιμοποιούμενο κεφάλαιο
                - Returns:

                - traffic_speed_net_profit
                    - εκμηρίωση\nταχυτητα κυκλοφοριας ιδιων κεφαλαιων 
                    Αυτός ο αριθμοδείκτης μας δείχνει πόσες φορές τα  ίδια κεφάλαια ανανεώνεται ή ανακτάται μέσω των πωλήσεων. Πως λειτουργεί εχουμε την Επιχειρηση Χ
                    που πραγματοποιησε πώλησης 1.400.000 και τα ίδια κεφάλαια είναι   1.000.000 τότε αποτέλεσμα ειναι 1,4.  Αρα  η επιχειρηση κέρδισε επιπλων κεφάλαια 400.000 απο της πώλησης\ ή 40 % επιπλεων κεφαλαια.
                    - Args:
                        - net_sales (float): καθαρές πωλήσεις
                        - net_profit (float):ίδια κεφάλαια
                    - Returns : 

- library LiquidityRadios
    - Module liquidityradios
        - class LiquidityRadios
            - current_radio
            - Αριθμοδείκτης Γενικής  ή έμμεσης ρευστότητας
            -  Args: 
                - circulating_assets
                - short_term_liabilities
            - return 

            - cash_radio 
            - Αριθμοδείκτης ταμειακής ρευστότητας
            - Args: 
                - available_cash
                - short_term_liabilities
            - return

            - defensive_interval
            - Το αμυντικό διάστημα
            - Args: 
                - circulating_assets
                - forecast_daily_expenses
            - return

            - net_working_capital
            - καθαρο κεφαλαιο κινησης
            - Args: 
                - short_term_liabilities
                - circulating_assets
            - return

            - acid_test_radio
            - Άμεση ρευστότητα
            - Args: 
                - circulating_assets
                - stocks
            - return

            - quick_radio
            - Άμεση ρευστότητα
            - Args: 
                - requirements
                - available_cash
                - short_term_liabilities
            - return

- profitability_radios
    - module equity_capital
        - class EquityCapital
            - net_profit_margin
                - Η μέθοδος καθαρό περιθώριο κέρδους, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση
                - Args: 
                    - net_profits
                    - net_sales
                - return  round((self.net_profits/self.net_sales), 2)
            - asset_turnover_velocity
                -  Η μέθοδος ταχυτητα κυκλοφοριας ενεργητικου, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση.
                - Args: 
                    - net_sales
                    - fixed_asset
                - return: round((self.net_sales / self.fixed_asset), 2)
            - financial_leverage
                - Η χρηματοοικονομικη μόχλευση, κληρονομεί τους λογαριασμούς από την EquityCapital κλάση.
                - Args: 
                    - fixed_asset
                    - equity_capital
                - return: round((self.fixed_asset / self.equity_capital), 2)

            - equity_multiplier
            - Restatement_equity_multiplier
    - module financial_leverage
        - class FinancialLeverageRadio
            - financial_leverage
            - economic_benefits
    - module grossprofit
    - module maintenanceandrepair
    - total_capital_employed
