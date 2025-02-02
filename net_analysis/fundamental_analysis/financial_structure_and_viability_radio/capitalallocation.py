from icecream import ic
import locale
locale.setlocale(locale.LC_ALL, '')


class Data:
    pass




class capital_structure:
    """_summary_
    """
    def __init__(self,
        total_assets:float=1.0,
        fixed:float=1.0,
        current_assets:float=1.0,
        liabilities :float=1.0,
        self_foreign :float=1.0,
        short_term_foreign_funds :float=1.0,
        long_term_foreign_capital:float=1.0,
        interest_rate:float = 0.1,
        market_capitalization_of_equity:float = 1.0,
        tax_rate:float = 1.0,):
        self.total_assets = total_assets
        self.fixed = fixed
        self.current_assets = current_assets
        self.liabilities = liabilities
        self.short_term_foreign_funds = short_term_foreign_funds
        self.long_term_foreign_capital = long_term_foreign_capital
        self.self_foreign = self_foreign
        self.interest_rate = interest_rate # epitokio
        self.tax_rate = tax_rate # συντελεστης φορου
        self.market_capitalization_of_equity = market_capitalization_of_equity
        self.dict = {"foreign_capital": "The total foreign capital is:"}

    def foreign_capital_ratio_calculation(self):
        import math
        epsilon = 1e-9
        """
        Υπολογίζει το συνολικό ξένο κεφάλαιο με βάση τα short-term 
        και long-term κεφάλαια, και επιστρέφει το αποτέλεσμα.
        """
        if math.isclose(self.short_term_foreign_funds, 1.0, abs_tol=epsilon) and \
                math.isclose(self.long_term_foreign_capital, 1.0, abs_tol=epsilon):
            return 0.0
    
        # Έλεγχος για την περίπτωση που και τα δύο δεν είναι 1.0
        if not math.isclose(self.short_term_foreign_funds, 1.0, abs_tol=epsilon) and \
            not math.isclose(self.long_term_foreign_capital, 1.0, abs_tol=epsilon):
            return (self.short_term_foreign_funds + self.long_term_foreign_capital)
        
        # Έλεγχος αν μόνο το short_term είναι 1.0
        if math.isclose(self.short_term_foreign_funds, 1.0, abs_tol=epsilon):
            return self.long_term_foreign_capital
        
        # Έλεγχος αν μόνο το long_term είναι 1.0
        if math.isclose(self.long_term_foreign_capital, 1.0, abs_tol=epsilon):
            return self.short_term_foreign_funds
    
    def total_capital(self)->float:
        import math
        epsilon = 1e-9
        # δουλεβει 
        if math.isclose(self.short_term_foreign_funds, 1.0, abs_tol=epsilon)  and \
            math.isclose(self.long_term_foreign_capital, 1.0, abs_tol=epsilon) and \
            math.isclose(self.self_foreign , 1.0, abs_tol=epsilon):
            return 0.0
        # δουλεβει
        if self.short_term_foreign_funds > 1.0 and self.long_term_foreign_capital > 1.0\
            and self.self_foreign > 1.0 :
            return sum([self.self_foreign, self.short_term_foreign_funds, self.long_term_foreign_capital])
        # δουλεβει 
        if math.isclose(self.long_term_foreign_capital, 1.0, abs_tol=epsilon):
            return sum([self.short_term_foreign_funds, self.self_foreign])
        # δουλεβει
        if math.isclose(self.short_term_foreign_funds, 1.0, abs_tol=epsilon):
            return sum([self.long_term_foreign_capital + self.self_foreign])
        # δουλεβει
        if math.isclose(self.self_foreign, 1.0, abs_tol=epsilon):
            return sum([self.long_term_foreign_capital + self.short_term_foreign_funds])

    def leverage_tax_reduction(self):
        if self.short_term_foreign_funds > 1.0 and \
            self.interest_rate > 0:
            interest = (self.short_term_foreign_funds * (self.interest_rate/100))
            incom_tax = (interest * (self.tax_rate/100))
            tax_reduction = ((interest - incom_tax ) / self.short_term_foreign_funds )
            return f"\nshort_term_foreign_fund: {self.short_term_foreign_funds:,.2f}\
                \tinterest: {interest:,.2f}\tincom_tax: {incom_tax:,.2f}\
                \ttax_reduction: {tax_reduction:,.2%}"
        if self.long_term_foreign_capital > 1.0 and \
            self.interest_rate > 0:
            interest = (self.long_term_foreign_capital * (self.interest_rate/100))
            incom_tax = (interest * (self.tax_rate/100))
            tax_reduction = ((interest - incom_tax ) / self.long_term_foreign_capital)
            return f"\nshort_term_foreign_fund: {self.long_term_foreign_capital:,.2f}\
                \tinterest: {interest:,.2f}\tincom_tax: {incom_tax:,.2f}\
                \ttax_reduction: {tax_reduction:,.2%}"

    def distribution_of_assets(self):
        if self.fixed > self.current_assets:
            return "low liquidity of assets"
        if self.fixed == self.current_assets:
            return "balance"
        if self.fixed < self.current_assets:
            return "High liquidity of assets"

    def radio_of_owners_equity_to_total_assets(self):
        return f"Ιδοκτησιας {(self.self_foreign/self.total_capital()):,.2%}"

    def foreign_capital_pressure_index(self):
        return f"Πιεσης {self.foreign_capital_ratio_calculation() / self.total_capital():,.2%}"
    
    def radio_of_owners_equity_to_total_liavilities(self):
        return f"Δανιακης επιβαρινσης {(self.foreign_capital_ratio_calculation() / self.self_foreign):,.2%}"
    
    def listed_radio_of_owners_equity_to_total_liavilities(self):
        return (self.foreign_capital_ratio_calculation()/self.market_capitalization_of_equity)
    
    def asset_structure_radio(self):
        self.total_assets = (self.fixed + self.current_assets)
        def asset_structure_radio_a():
            if self.fixed > 1.0:
                return (self.fixed/self.total_assets)
        def asset_structure_radio_b():
            if self.current_assets > 1.0:
                return (self.current_assets/self.total_assets)
        def asset_structure_radio_c():
            return (self.fixed/self.current_assets)
        return f"{asset_structure_radio_a()}\n{asset_structure_radio_b()}\n{asset_structure_radio_c()}"

    def radio_of_owners_qquity_to_fixed_assets(self):
        return (self.self_foreign/self.fixed)

