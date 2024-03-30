# Date request format -- Apr 05, 2024

from bs4 import BeautifulSoup
import requests
from datetime import date, datetime, timezone
import pprint as pp
import time


class GetGreeks:
    def __init__(self):
        self.greeks = None
    
    def fetch_greeks(self, req_stock, req_date):
        """
        # 
        Need to reformat main url, so when a data and value is passed in, we convert to ISO time 
        """
    
        stock_name = req_stock.strip()
        strike_date = self.convert_date_to_timestamp(req_date)
        
        url = f'https://finance.yahoo.com/quote/{stock_name}/options/?date={strike_date}'
        
        today = str(date.today())
        self.greeks = {today : {}}


        try:
            # Inital request with headers
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            page_source = requests.get(url, headers=headers)
            response = BeautifulSoup(page_source.content, features="lxml")
            tables = response.find_all("table")
            # Key track of current main kley 
            current = "Calls"

            # Main identifier -- current date
            self.greeks[today] = {current: {}}

            #Len(2), calls table and puts table
            for table in tables:

                # Each row in calls and puts
                rows = table.find_all("tr")

                # Holder for sub dictionary of calls or puts
                test_dic = {}

                # Each individual row of calls or puts
                for row in rows:
                    
                    # Count track of identifier (Keys)
                    count = 0
                    #Main key for sub objetcs, strike price
                    id = None
                    identifiers = ["ID", "Last_Trade", "Strike", "Last_Price", "Bid", "Ask", "Chance", "Change_Percent","Volume","Open_Interest", "Implied_Volatility" ]
                    
                    # Sub dictionary to get added to other sub dictionary
                    object = {}
                    
                    # Reformat data
                    for i in row:
                        if count > 1:
                            if count == 2:
                                id = i.text
                            object[identifiers[count]] = i.text
                        else:
                            pass
                        count += 1
                    
                    # Add sub dictionary to sub dictionary 
                    test_dic[id] = object
                # Append main sub dictionary to main data holder
                self.greeks[today][current] = test_dic

                #Switch main key to puts 
                current = "Puts"

            pp.pprint(self.greeks)
                
        except:
            return "Error"
        

    def convert_date_to_timestamp(self, date_str):
        """
        Convert date input to a timestamp
        """
        try:
            date_obj = datetime.strptime(date_str, '%b %d, %Y')
    
            # initalize utc timezone
            date_obj_utc = date_obj.replace(tzinfo=timezone.utc)
    
            # Convert the UTC datetime object to a Unix timestamp 
            timestamp = int(date_obj_utc.timestamp())
            return timestamp
        except:
            return 'Error'

    def return_greeks(self, stock, date):
        if self.greeks is None:
            self.fetch_greeks(stock, date)
        return self.greeks        