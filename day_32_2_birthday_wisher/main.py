##################### Extra Hard Starting Project ######################

import csv
import smtplib
import datetime as dt
from random import randint

MY_EMAIL = "your_mail@gmail.com"
MY_PASSWORD = "your_password"


def send_email(name, email):
    """Selects one of three letters, inserts the value into the [NAME] field
    and sends it from my email to the birthday person's email."""

    # Preparing a letter
    letter_number = randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)

    # Sending a letter
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Alles Gute zum Geburtstag!\n\n{letter}"
        )



now = dt.datetime.now()
present_month = now.month
present_day = now.day

with open("birthdays.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[3] != "month" and row[4] != "day":
            birthday_month = int(row[3])
            birthday_day = int(row[4])
            if present_month == birthday_month and present_day == birthday_day:
                birthday_person = row[0]
                birthday_email = row[1]
                send_email(birthday_person, birthday_email)
