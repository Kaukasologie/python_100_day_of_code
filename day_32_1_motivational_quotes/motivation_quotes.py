import smtplib
import datetime as dt
from random import choice


def send_email(quote_to_send):
    """Sends a quote_to_send from one email address to another"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="your_mail@gmail.com", password="your_password")
        connection.sendmail(
            from_addr="your_mail@gmail.com",
            to_addrs="addressee_mail@outlook.com",
            msg=f"Subject:Weekly Motivational Quote\n\n{quote_to_send}"
        )


# Create a list with quotes from a file
with open("quotes.txt") as quotes_file:
    quotes = [quote for quote in quotes_file]   # readlines()


# Check for a match by day of the week
today = dt.datetime.now().weekday()
if today == 5:  # Saturday Quote (0 - for Monday)
    send_email(choice(quotes))
