"""
Calculate if CSP or CC is better for exp
All calculations go into an object to be displayed on a site
"""


"""
Need to get ex-dividen amount
Need to get Hard to borrow rate
"""

class CalculateBestChoice:
    def __init__(self) -> None:
        self.best_chocie = {}

    def convert_number(self):
        """
        Will be used to convert str numbers in floats
        """
        pass


    def run_caclutions(self, stock_price, strike_price, days_until_expiration, call_premium, put_premium, MMF_rate, t_bill_rate):
        """
        7 Required Inputs 
        9 including ex-dividen amount and hard to borrow rate 

        1) Cash Difference = (stock_price - call_premiumum + put_premium) * 100 
        2) Number of years = days_until_expiration / 365 
        3) Interest on Cash Difference = Condtional Check 
        4) Annual Yield on Cash = Interst on cash / cash difference / number of years 
        5) Intrinsic value and Time value 
        6) Interest rate being priced in 

        """
        pass
