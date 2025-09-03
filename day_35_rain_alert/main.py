import requests
import json
from config import *
from twilio.rest import Client


# For the weather API
latitude = MY_LATITUDE
longitude = MY_LONGITUDE
api_key = OWM_API_KEY
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# For the communications API (sending SMS)
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
my_number = MY_NUMBER


weather_parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()


# # ? How to dump a dict to a JSON file? https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file
# with open("data.json", "w") as file:
#     json.dump(weather_data, file)


will_rain = False
time = []

for hour_data in weather_data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 600:
        will_rain = True
        time.append(f"{hour_data["dt_txt"].split(" ")[1].split(":")[0]}:{hour_data["dt_txt"].split(" ")[1].split(":")[1]}")


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid="MGb27c6f3149ae136ffb0b4f76eabb5553",
        body=f"\nToday rain is forecasted around this time: {", ".join(time)}.\nDon't forget to bring an umbrella ☔",
        to=my_number,
    )
    print(message.status)

