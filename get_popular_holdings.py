from bs4 import BeautifulSoup
import requests
import re
from datetime import date
import pprint as pp
 
class GetHoldings:
    """
    Gets and returns holdings of Nasdaq 100 and S&P500 in an object.
    Main key is current date feteched to prevent repetitve requests.
    """

    def __init__(self):
        self._data = None
    
    def fetch_holdings(self):
        """
        Fetch SPY and Nasdaq 100 holdings
        """
        today = str(date.today())
        holdings = ["https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", "https://en.wikipedia.org/wiki/Nasdaq-100"]

        # Popular holdings will be updated on a month basis, key will be MM/YYYY
        month_year = today.split("-")

        for url in holdings:
            page_source = requests.get(url)
            response = BeautifulSoup(page_source.content, "html.parser")

            targeted_patern = re.compile(r'constituents')
            table = response.find(id=targeted_patern)
            
            stocks = table.find_all("tr")

            # Temp holder to be added to data object
            temporary_data_by_day = {month_year[1]+"-"+month_year[0]: {}}

            for stock in stocks:
                if url[-1] == "0":
                    # Handle nasdaq 100
                    temp = stock.find_all("td")
                    if len(temp) > 2:
                        # Picking up additional elements, easy bypass for now.
                        stock_name = temp[0].text.strip() 
                        stock_symbol = temp[1].text.strip()

                    if stock_symbol not in temporary_data_by_day:
                        temporary_data_by_day[month_year[1]+"-"+month_year[0]][stock_symbol] = {"company_name": stock_name, "stock_symbol": stock_symbol, "as_of": today}

                else:
                    # Handle S&P500
                    temp = stock.find_all("a")
                    stock_symbol = temp[0].text.strip() 
                    stock_name = temp[1].text.strip()

                    if stock_symbol not in temporary_data_by_day:
                        temporary_data_by_day[month_year[1]+"-"+month_year[0]][stock_symbol] = {"company_name": stock_name, "stock_symbol": stock_symbol, "as_of": today}


            self._data = temporary_data_by_day

    def return_data(self):
        """
        Returns SPY and Nasdaq 100 holdings
        """

        if self._data is None:
            self.fetch_holdings()
        
        return self._data

