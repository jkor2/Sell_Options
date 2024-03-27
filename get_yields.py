from bs4 import BeautifulSoup
import requests
from datetime import date
import pprint as pp


class GetYields:
    def __init__(self) :
        self.yields = None
    
    def get_yield_treasury(self):
        """
        Get T-Rates from Bloomberg
        """
        url = "https://www.bloomberg.com/markets/rates-bonds/government-bonds/us"
        # Bypass bot check, pass in headers
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        
        page_source = requests.get(url, headers=headers)
        today = str(date.today())

        if page_source.status_code == 200:
            response = BeautifulSoup(page_source.content, features='lxml')
            table = response.find("table")
            list = table.find_all("tr")
            temp = {}
            for item in list:
                title = item.find("div", {'data-type': "full" })
                if title is not None:
                    data = item.find_all("td")
                    temp[title.text.strip()] = {
                        "yield" : data[2].text.strip(),
                        "price" : data[1].text.strip()
                    }
            
            self.yields = {today.strip() : temp}

        else:
            print("Failed to retrieve page with status code:", page_source.status_code)


    def return_yield(self):
        """
        Returns yield rates, will fetch rates if not yet done.
        """

        if self.yields is None:
            self.get_yield_treasury()
        
        return self.yields


gy = GetYields()
gy.get_yield_treasury()
pp.pprint(gy.return_yield())