import os
from dotenv import load_dotenv

# Loading variables from .env
load_dotenv()

OWM_API_KEY = os.getenv("OWM_API_KEY")
MY_LATITUDE = os.getenv("MY_LATITUDE")
MY_LONGITUDE = os.getenv("MY_LONGITUDE")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_NUMBER = os.getenv("MY_NUMBER")

if not OWM_API_KEY or not MY_LATITUDE or not MY_LONGITUDE or not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not MY_NUMBER:
    raise ValueError("⚠️ Environment variables missing! Please create .env from .env.example")
