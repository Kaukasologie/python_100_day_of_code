import csv
import smtplib
from datetime import datetime
from random import randint

MY_EMAIL = "your_mail@gmail.com"
MY_PASSWORD = "your_password"

def send_email(name, email):
    """Selects one of three letters, inserts the value into the [NAME] field
    and sends it from my email to the birthday person's email."""

    # Preparing a letter
    with open(f"letter_templates/letter_{randint(1, 3)}.txt") as file:
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


today = (datetime.now().month, datetime.now().day)

with open("birthdays.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[3] != "month" and row[4] != "day":
            birthday = (int(row[3]), int(row[4]))
            if today == birthday:
                birthday_person = row[0]
                birthday_email = row[1]
                send_email(birthday_person, birthday_email)


# # Solution with pandas
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today in birthdays_dict: ...
