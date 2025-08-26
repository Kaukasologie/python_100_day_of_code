import requests
import smtplib
import time
from datetime import datetime


MY_EMAIL = "your_mail@gmail.com"
MY_PASSWORD = "your_password"
MY_LATITUDE = 51.507351  # Your latitude
MY_LONGITUDE = -0.127758  # Your longitude


def send_email():
    print("Sending email...\n")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nThe International Space Station (ISS) flies over you!"
        )


def is_iss_overhead():
    """Gets the latitude and longitude of the International Space Station via API (api.open-notify.org),
    compares it with your location and returns True if the ISS is flying over your location (+/- 5 degree)"""

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"ISS:\nLatitude: {iss_latitude}\nLongitude is: {iss_longitude}\n")
    print(f"Your:\nLatitude: {MY_LATITUDE}\nLongitude is: {MY_LONGITUDE}\n")

    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True
    return None


def is_night():
    """Find out the sunrise and sunset times in your area and if it is currently dark, return True"""

    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    #Current date and time
    time_now = datetime.now()

    if sunset <= time_now.hour or time_now.hour <= sunrise:
        return True
    return None


# MAIN
n = 0
while True:
    n += 1
    print(f"Check #{n}\n")

    if is_iss_overhead():
        if is_night():
            send_email()
        else:
            print("The International Space Station flies above you, but you won't be able to see it during the day.\n")
    else:
        print("The International Space Station is not nearby.\n")

    time.sleep(60)

