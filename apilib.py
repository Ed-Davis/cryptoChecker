import requests
from dotenv import dotenv_values
import json


class Api:
    secrets = dotenv_values("secrets/.env")
    baseurl = "https://binance43.p.rapidapi.com/"
    headers = {
        "X-RapidAPI-Key": secrets['API_KEY'],
        "X-RapidAPI-Host": "binance43.p.rapidapi.com"
    }

    def __init__(self) -> None:
        return

    def data(self, endpoint='ticker/24hr', querystring=None) -> dict:
        url = self.baseurl + endpoint
        response = requests.get(url=url, headers=self.headers, params=querystring)
        return response.json()

    @staticmethod
    def mocked_data(self) -> dict:
        with open('example.json') as json_file:
            return json.load(json_file)

    @staticmethod
    def top3(self, body_data: dict) -> list:
        ordered = sorted(body_data, key=lambda x: x['priceChangePercent'])
        return ordered[-3:]

