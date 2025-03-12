class Args:
    def __init__(
        self,
        circulating_assets: float,
        short_term_liabilities: float,
        available_cash: float,
        stocks: float,
        forecast_daily_expenses: float,
        requirements: float,
    ) -> None:
        self.circulating_assets = circulating_assets
        self.short_term_liabilities = short_term_liabilities
        self.available_cash = available_cash
        self.stocks = stocks
        self.forecast_daily_expenses = forecast_daily_expenses
        self.requirements = requirements
