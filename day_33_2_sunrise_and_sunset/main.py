import requests


MY_LATITUDE = 48.856613
MY_LONGITUDE = 2.352222

parameters = {
    "lat": MY_LATITUDE,     # https://www.latlong.net
    "lng": MY_LONGITUDE,
    "formatted": 0
}


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")

print(f"In the selected area with latitude {MY_LATITUDE} and longitude {MY_LONGITUDE} "
      f"the sun rises at {sunrise[0]}:{sunrise[1]} and sets at {sunset[0]}:{sunset[1]}.")
