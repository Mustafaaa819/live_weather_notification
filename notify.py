import requests
from dotenv import load_dotenv
import os
from plyer import notification

load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY = "Tank, PK"

#Scraping Data from the URL.
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

#Prsing the Data into JavaScrip Object Notation(JSON)
response = requests.get(url)
data = response.json()

#Fetching Specific Data
weather = data['weather'][0]['description']
temperature = data['main']['temp']
temp_feels_like = data['main']['feels_like']

if 'rain' in data:
    rain = data['rain'].get('1h', 0)
    rain_msg = f"\nRain (last 1-Hour): {rain}mm"
else:
    rain_msg = "No Rain Expected☀️"


message = f"{CITY} \n{weather.title()}, \n{temperature} °C, Feels like {temp_feels_like} °C, \n{rain_msg}"


notification.notify(
    title = f"Weather Update",
    message=message,
    timeout=10
)
