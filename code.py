import requests
from win10toast import ToastNotifier
import os
from dotenv import load_dotenv

load_dotenv()

#API key and City:
API_KEY = os.getenv("API_KEY")
CITY = "Tank, PK"

#Desktop Notification
notifier = ToastNotifier()

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()
# print(data)

weather = data['weather'][0]['description']
temperature = data['main']['temp']
temp_feels_like = data['main']['feels_like']

if 'rain' in data:
    rain_chances = data['rain'].get('1hr',0)
    rain_msg = f"\nRain (last 1-Hour): {rain_chances}%"
else:
    rain_msg = "No Rain Expected☀️"



notifier.show_toast("Weather Update", f"{CITY} \n{weather.title()}, \n{temperature} °C, Feels like {temp_feels_like} °C, \n{rain_msg}", duration=20)
