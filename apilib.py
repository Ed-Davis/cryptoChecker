import requests
from dotenv import dotenv_values
import json


class Api:
    """This module handles API requests and the mocked alternative"""

    def __init__(self) -> None:
        self.secrets = dotenv_values(".env")
        self.baseurl = "https://binance43.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Key": self.secrets['API_KEY'],
            "X-RapidAPI-Host": "binance43.p.rapidapi.com"
        }

    def data(self, endpoint='ticker/24hr', querystring=None) -> dict:
        url = self.baseurl + endpoint
        response = requests.get(url=url, headers=self.headers, params=querystring)
        return response.json()

    @staticmethod
    def mocked_data() -> dict:
        with open('example.json') as json_file:
            return json.load(json_file)

    @staticmethod
    def top3(body_data: dict) -> list:
        ordered = sorted(body_data, key=lambda x: x['priceChangePercent'])
        return ordered[-3:]
