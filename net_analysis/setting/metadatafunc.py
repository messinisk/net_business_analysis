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