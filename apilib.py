"""This module handles API requests and the mocked alternative"""
import json
import requests
from dotenv import dotenv_values


class Api:
    """This class encapsulates the data retrieval and sorting, and provides a single adaptor for the requests lib"""

    def __init__(self) -> None:
        """Constructor method"""
        self.secrets = dotenv_values(".env")
        self.baseurl = "https://binance43.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Key": self.secrets['API_KEY'],
            "X-RapidAPI-Host": "binance43.p.rapidapi.com"
        }

    def api_get(self, endpoint='ticker/24hr', querystring=None) -> dict:
        """Capture real data from the API using a Get-Request with the default set to the main call"""
        url = self.baseurl + endpoint
        response = requests.get(url=url, headers=self.headers, params=querystring)
        return response.json()

    @staticmethod
    def mocked_data() -> dict:
        """capture mocked data from file"""
        with open('example.json', encoding='ascii') as json_file:
            return json.load(json_file)

    @staticmethod
    def top3(body_data: dict) -> list:
        """Sort the data by the key 'priceChangePercent' """
        ordered = sorted(body_data, key=lambda x: x['priceChangePercent'])
        return ordered[-3:]
