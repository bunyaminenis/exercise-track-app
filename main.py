import os
import requests
from datetime import datetime
from dotenv import load_dotenv, dotenv_values

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")


nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

exercise_params = {
    "query":   exercise_text,
    "weight_kg": 65,
    "height_cm": 175,
    "age": 29
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=nutrition_endpoint, json=exercise_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_post_endpoint = os.getenv("SHEET_POST_ENDPOINT")

bearer_auth_head = {
    "Authorization": f"Bearer {os.environ.get("TOKEN")}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    sheet_response = requests.post(url=sheet_post_endpoint, json=sheet_inputs, headers=bearer_auth_head)
    print(sheet_response.json())