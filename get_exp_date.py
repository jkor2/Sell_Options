"""
Each ticker will have its own collection, we can then search for last requested date based on ticker
from there insertions / updates can be made.
"""
from bs4 import BeautifulSoup
import requests
from datetime import date
import pprint as pp


class ExpirationDates:
    def __init__(self) -> None:
        self.expiration_dates = None
    
    def get_dates(self, stock):
        url = 'https://optioncharts.io/options/%s/chain/chart/open-interest' % stock
        today = str(date.today())

        try:
            # Make request to option chorts based on a given ticker 
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            page_source = requests.get(url, headers=headers)
            response = BeautifulSoup(page_source.content, features='lxml')

            # Temp holder to reformat expirations
            temp = {}

            dates = response.find("select")
            for item in dates:
                text_list = item.text.strip().split(" ")
                if len(text_list) > 1:
                    temp[text_list[0] + " " + text_list[1] + " " + text_list[2]] = {
                            "days_until_expiration": text_list[3] + " " + text_list[4],
                            "contract_type" : text_list[-1]}
                    
            # Main key will be ticker to know which collection to insert into for DB 
            self.expiration_dates = {stock.upper(): temp,
                                            "date_requested": today.strip()}
        except:
            # Must be a valid ticker
            print("Error")

    def return_expiration_dates(self, ticker):
        """
        Return expiration dates based on if the request has been made 
        """
        if self.expiration_dates is None:
            self.get_dates(ticker)
        
        return self.expiration_dates



ed = ExpirationDates()
pp.pprint(ed.return_expiration_dates("spy"))