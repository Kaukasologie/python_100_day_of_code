import requests
import smtplib
from datetime import datetime

MY_LATITUDE = 51.507351  # Your latitude
MY_LONGITUDE = -0.127758  # Your longitude


def send_email():
    print("Sending email...")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="your_mail@gmail.com", password="your_password")
        connection.sendmail(
            from_addr="your_mail@gmail.com",
            to_addrs="addressee_mail@mail.com",
            msg="Subject:Look UP!\n\nThe International Space Station (ISS) flies over you!"
        )


# Get the latitude and longitude of the International Space Station
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Find out the sunrise and sunset times in your area
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


# If the ISS is close to my current position (within +5 or -5 degrees of the ISS position)
if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE:
    # and it is currently dark
    if sunset <= time_now.hour or time_now.hour <= sunrise:
        # then send a mail
        send_email()

    else:
        print("The International Space Station flies above you, but you won't be able to see it during the day.")
else:
    print("The International Space Station is not nearby.")


# BONUS: run the code every 60 seconds.



