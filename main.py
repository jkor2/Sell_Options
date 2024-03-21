# Main Functionality of API
"""
- User will be able to recive fund holdings 
- Request options data of a the week interested in by:
    1) getting exp dates
    2) Getting options greeks/quotes for the date selected
    3) Get current yield of popular MMFs / HYSAs
    4) Get current T-Bill Yield Rates
    5) Calculate if CSP or CC is better for exp
        - All calculations go into an object to be displayed on a site
"""

class Main:
    def __init__(self) -> None:
        data = {}
    
    def get_fund_list(self):
        pass

    def get_fund_holdinfs(self, fund):
        pass

    def get_options_data(self, stock):
        pass
    