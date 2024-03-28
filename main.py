import pprint as pp
import get_yields as gy
import get_popular_holdings as gph
import get_exp_date as ged


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
        pp.pprint(expiration_dates.return_expiration_dates(ticker))
    
main = Main()
main.get_exipration_dates("TSLA")