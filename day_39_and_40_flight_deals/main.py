#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from flight_search import FlightSearch

# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)


flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()