import os
import dotenv
import requests
from datetime import datetime


dotenv.load_dotenv()

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = os.getenv("GENDER")
WEIGHT_KG = int(os.getenv("WEIGHT_KG"))
HEIGHT_CM = int(os.getenv("HEIGHT_CM"))
AGE = int(os.getenv("AGE"))

# Nutritionix APP ID and API Key. Actual values are stored as environment variables.
NIX_APP_ID = os.getenv("ENV_NIX_APP_ID")
NIX_API_KEY = os.getenv("ENV_NIX_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did:\n- ")

# Nutritionix API Call
nix_header = {
    "x-app-id": NIX_APP_ID,
    "x-app-key": NIX_API_KEY,
}

nix_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, headers=nix_header, json=nix_parameters)
result = response.json()
print(f"\nNutritionix API call: \n {result} \n")

# Sheety Project API.
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = os.getenv("ENV_SHEETY_ENDPOINT")

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Basic Authentication
    basic_headers = {
        "Authorization": f"Basic {os.getenv("ENV_SHEETY_BASIC_TOKEN")}"
    }

    sheet_response = requests.post(
        url=sheet_endpoint,
        json=sheet_inputs,
        headers=basic_headers,
    )

    print(f"Sheety Response: \n {sheet_response.text}")

