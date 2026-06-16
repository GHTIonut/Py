import requests

WEATHER_API = "https://api.weatherapi.com/v1/current.json?"
SECRET_KEY = "47e4d0daa725409795d102843261606"

location = input("Give me your location: ")

params = {
    'key': SECRET_KEY,
    'q': location
}

response = requests.get(WEATHER_API, params)
response_json = response.json()

temperature = response_json['current']['temp_c']
print(f"In {location} are {temperature} degrees celcius.")

