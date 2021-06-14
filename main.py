import requests
from datetime import datetime

NUTRITIONIX_API_ID = "9361ea26"
NUTRITIONIX_API_KEY = "6ad9b49439e71f77c8e543ad97c48a2b"

GENDER = "male"
WEIGHT_KG = 106
HEIGHT_CM = 171
AGE = 28

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

sheet_endpoint = "https://api.sheety.co/c59c86e598757a2986b0cbd38954ef54/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
header = {
    "Authorization": "Basic bWF0ZXVzem9uZTpQb2xza2ExOTky"
}
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=header)
