"""
Class dedicated to monitoring top Money Market Funds
"""
from bs4 import BeautifulSoup
import requests
from datetime import date
import pprint as pp


class MoneyMarketFunds:
    def __init__(self):
        self._funds = {}

    def search_funds(self):
        pass

    def return_yields(self):
        pass
