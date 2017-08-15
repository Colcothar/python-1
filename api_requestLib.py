import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")
content = response.content.decode("utf-8")
print(json.loads(content))

# Getting json from an API request
data = response.headers["content-type"]
dataJson = response.json()
print(dataJson["iss_position"])

fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

print('test')

print(json.dumps(fast_food_franchise))
