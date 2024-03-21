# https://www.barchart.com/etfs-funds/quotes/**Ticker**/options

"""
Will be called when a ticker symbol is choosen, will return all the option expiration dates.
Dates will need to be converted to this format -- "2024-03-19-w"
"""

class ExpirationDates:
    def __init__(self) -> None:
        self.expiration_dates = {}
    
    def get_dates(self, stock):
        pass