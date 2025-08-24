# import smtplib  # Simple Mail Transfer Library
#
# my_email = "your_mail@gmail.com"
# my_password = "your_password"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:  # Connect to our email provider's SMTP email server
#     connection.starttls()   # Transport Layer Security
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="addressee_mail@outlook.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )



import datetime as dt

now = (dt.datetime.now())
print(f"datetime.now(): {now},\ntype: {type(now)}\n")

year = now.year
print(f"datetime.now().year: {year},\ntype:{type(year)}\n")

month = now.month
day_of_week = now.weekday()
print(f"Day of week: {day_of_week}\n")    # 0: Monday, 1: Tuesday, ..., 6: Sunday.

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(f"Date of birth: {date_of_birth}\n")

