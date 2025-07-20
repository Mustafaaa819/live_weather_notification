# 🌦️ Live Weather Notification on Desktop — for Your City!

This is a Python project that shows **real-time weather notifications** directly on your **Windows desktop** using either `plyer` or `win10toast`.

> ⚠️ **Built for my city — Tank, Pakistan**, but fully customizable for **your own city**!  
> Just enter your city name in the code and you're good to go!

---

## 🧠 What This Project Does

- Connects to the [OpenWeatherMap API](https://openweathermap.org/api) 🌐
- Extracts current weather data (temperature, description, rainfall)
- Formats it into a readable message
- Pops up a Windows **desktop notification** when your computer starts!

---

## 📁 Files in This Project

| File        | Purpose                                                                 |
|-------------|-------------------------------------------------------------------------|
| `code.py`   | Uses `win10toast` to create a simple weather notifier.                 |
| `notify.py` | Uses `plyer.notification` for better styling and customization.        |
| `.env`      | Stores your **private API key** from OpenWeatherMap.                   |
| `weather_notify.vbs` | Used to run the script silently at Windows startup.         |
| `run_weather.bat`    | Launches the Python file via double-click or startup action. |
| `.gitignore` | Hides sensitive files (like `.env`) from being uploaded to GitHub.   |

---

## 🛠 How the Code Works (Line-by-Line)

### 🔹 `code.py` — Using `win10toast`
```python
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Weather Update", message, duration=10)


notify.py — Using plyer.notification
from plyer import notification

notification.notify(
    title = f"Weather Update in {CITY}",
    message=message,
    timeout=10
)
Pops up the weather with location, temperature, and rain info.

timeout=10 controls how long the notification stays.


.env — Store Your API Key Securely
Instead of putting your API key directly into the Python code:


API_KEY=your_secret_openweather_api_key
Then load it like this in your script:


from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
✅ Keeps your key safe
✅ Makes your code sharable

🌍 Customizing for YOUR City
Just open either code.py or notify.py and replace this line:


CITY = "Tank, PK"  # 👈 change this!
Example:

CITY = "Lahore, PK"
💡 Requirements (Install Once)

pip install requests python-dotenv plyer win10toast


🖥️ Auto Run on Windows Startup
Create run_weather.bat:


@echo off
start "" "path\to\your\python.exe" "path\to\your\notify.py"
Then create a weather_notify.vbs file:


Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "path\to\your\run_weather.bat" & Chr(34), 0
Set WshShell = Nothing
Add weather_notify.vbs to this folder:

C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
 Now your script runs automatically on every login.

🔐 Protecting Your API Key
.env
*.vbs
*.bat
__pycache__/
This ensures your .env file with the secret API key never gets uploaded to GitHub.



Make sure you're connected to the internet — this script needs live data!

Notifications will only work if:

- You’re on Windows

- Your Python environment is set up

- You correctly placed the .vbs file in the startup folder

 Built with ❤️ by Mustafaa(future==AI):

