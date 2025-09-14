import os
from dotenv import load_dotenv
import requests


# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/70441f864716b8a7e7113f065ae1aaf6/flightDeals/prices"


class DataManager:


    def __init__(self):
        self.destination_data = {}
        self._authorization = {"Authorization": f"Basic {os.getenv("SHEETY_BASIC_TOKEN")}"}


    def get_destination_data(self):
        # GET all the data in Sheety API sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self._authorization
            )
            print(response.text)

