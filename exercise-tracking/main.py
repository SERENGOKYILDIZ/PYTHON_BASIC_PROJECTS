import requests
import os
from datetime import datetime


AppID = os.environ["APP_ID"]
AppKEY = os.environ["APP_KEY"]

GENDER = "male"
WEIGHT_KG = "78"
HEIGHT_CM = "172"
AGE = "21"

nutritionix_endpoint = "https://trackapi.nutritionix.com"
exercise_point = "/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": AppID,
    "x-app-key": AppKEY,
}

exercise_text = input("Tell me which exercises you did: ")

nutritionix_bodys = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

exercise_endpoint = f"{nutritionix_endpoint}{exercise_point}"


nutritionix_response = requests.post(url=exercise_endpoint, json=nutritionix_bodys, headers=nutritionix_headers)
nutritionix_response.raise_for_status()
nutritionix_result = nutritionix_response.json()
print(nutritionix_response.text)

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

exercise_man = nutritionix_result["exercises"]

for step in exercise_man:
    exercise = step["name"].title()
    duration = int(step["duration_min"])
    calories = int(step["nf_calories"])

    print(exercise)

    sheety_endpoint = "https://api.sheety.co/da2fc92257b98d29887d5a8ca24e55f2/workoutTracking/workouts"
    sheety_key = f"Bearer {os.environ['TOKEN']}"

    sheety_headers = {
        "Authorization": sheety_key
    }
    sheety_body = {
        "workout":
            {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }
    }

    sheety_response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_body)
    sheety_response.raise_for_status()
    sheety_result = sheety_response.json()
    print(sheety_response.text)