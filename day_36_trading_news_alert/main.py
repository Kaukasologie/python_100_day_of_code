import requests
import config
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = config.STOCK_API_KEY

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = config.NEWS_API_KEY

TWILIO_SID = config.TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN = config.TWILIO_AUTH_TOKEN
MY_NUMBER = config.MY_NUMBER
VIRTUAL_TWILIO_NUMBER = config.VIRTUAL_TWILIO_NUMBER

market_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=market_parameters)
response.raise_for_status()
stock_data = response.json()

# Get yesterday's closing stock price
first_day = str(date.today() - timedelta(days=3))
first_day_price = float(stock_data["Time Series (Daily)"][first_day]["4. close"])

# Get the day before yesterday's closing stock price
next_day = str(date.today() - timedelta(days=2))
next_day_price = float(stock_data["Time Series (Daily)"][next_day]["4. close"])

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
price_difference = (next_day_price - first_day_price) / first_day_price * 100

up_down = None
if price_difference > 0:
    up_down = "📈"
else:
    up_down = "📉"

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "from": first_day,
    "to": next_day,
    "language": "en",
    "searchln": "title",
    "sortBy": "popularity",
    "pageSize": "3"
}

# If difference percentage is greater than 5 then get the first 3 news pieces for the COMPANY_NAME.
if abs(price_difference) >= 5:
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()

    formatted_articles = [f"{STOCK}: {up_down} {round(price_difference, 2)}%\nHeadline: {article["title"]}\nBrief: {article["description"]}\n"
                          for article in news_data["articles"]]

    for article in formatted_articles:
        print(article)
    # # Send each article as a separate message via Twilio.
    # client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    # for article in formatted_articles:
    #     message = client.messages.create(
    #         body=article,
    #         from_=VIRTUAL_TWILIO_NUMBER,
    #         to=MY_NUMBER
    #     )

else:
    print("Small percentage of changes")

