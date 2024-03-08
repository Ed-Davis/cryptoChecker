"""This module handles API requests, ENV vars, and the mocked alternative data source"""
import json
import requests
from dotenv import dotenv_values


class Api:
    """This class encapsulates the data retrieval and sorting"""

    def __init__(self) -> None:
        """Constructor method"""
        self.secrets = dotenv_values(".env")
        self.baseurl = "https://binance43.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Key": self.secrets['API_KEY'],
            "X-RapidAPI-Host": "binance43.p.rapidapi.com"
        }

    def get(self, endpoint='ticker/24hr', querystring=None) -> dict:
        """Capture real data from the API using a Get-Request"""
        url = self.baseurl + endpoint
        response = requests.get(url=url, headers=self.headers, params=querystring)
        return response.json()

    @staticmethod
    def top3(body_data: dict) -> list:
        """Sort the data by the key 'priceChangePercent' """
        ordered = sorted(body_data, key=lambda key: key['priceChangePercent'])
        return ordered[-3:]

    @staticmethod
    def mocked_data(file="all_currencies.json") -> dict:  # For solving the problem only
        """Capture mocked data from file"""
        with open(file, encoding='ascii') as json_file:
            return json.load(json_file)
