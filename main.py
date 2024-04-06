import pprint as pp
import get_yields as gy
import get_popular_holdings as gph
import get_exp_date as ged
import get_greeks as gg


class Main:
    def __init__(self) -> None:
        data = {}
    
    def get_yields(self):
        """
        gets and returns yields **as needed**
        """
        yield_fetch = gy.GetYields()
        return yield_fetch.return_yield()

    def get_fund_holdings(self):
        """
        gets and returns fund holdings **as needed**
        """
        top_holdings = gph.GetHoldings()
        return top_holdings.return_data()

    def get_exipration_dates(self, ticker):
        """
        gets exiration dates and returns **as needed**
            - will need to refromat exiration datte for URL when getting greeks
        """
        expiration_dates = ged.ExpirationDates()
        return expiration_dates.return_expiration_dates(ticker)

    def get_greeks(self, stock, date):
        """
        Takes in a ticker and date to get greeks
        """
        greeks = gg.GetGreeks()
        return greeks.return_greeks(stock, date)

    def get_best_choice(self):
        """
        As of now, no arguments. When complete will have multiple
        """
        pass

    
# main = Main()
# main.get_exipration_dates("TSLA")
