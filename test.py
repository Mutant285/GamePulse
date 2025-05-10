import requests

API_KEY = "1cf5d088d754ce0125125b6601921440"
params = {"q": "Солигорск", "appid": API_KEY, "units": "metric"}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
x = response.json()
print(response.json())
print(x["main"]["temp"])
