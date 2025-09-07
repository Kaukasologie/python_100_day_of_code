import os
from dotenv import load_dotenv

# Loading variables from .env
load_dotenv()

STOCK_API_KEY = os.getenv("STOCK_API_KEY")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_NUMBER = os.getenv("MY_NUMBER")
VIRTUAL_TWILIO_NUMBER = os.getenv("VIRTUAL_TWILIO_NUMBER")

if not STOCK_API_KEY or not NEWS_API_KEY or not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not MY_NUMBER or not VIRTUAL_TWILIO_NUMBER:
    raise ValueError("⚠️ Environment variables missing! Please create .env from .env.example")