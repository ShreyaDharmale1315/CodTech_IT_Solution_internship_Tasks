import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch weather data
def fetch_weather(city, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data.get("cod") != 200:
            print(f"Error fetching data for {city}: {data.get('message')}")
            return None
        
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "weather": data["weather"][0]["description"].title()
        }
    except Exception as e:
        print(f"Exception: {e}")
        return None

# API Key for OpenWeatherMap
# replace with your own API key
API_KEY = "Enter Your API Key"

# Cities to analyze
cities = ["Mumbai", "Delhi", "Nagpur", "Kolkata", "Chennai", "Badnera", "Pune"]
weather_data = []

# Fetch data for each city
for city in cities:
    info = fetch_weather(city, API_KEY)
    if info:
        weather_data.append(info)

# Check data
for item in weather_data:
    print(item)

# Extract for plotting
city_names = [item["city"] for item in weather_data]
temps = [item["temperature"] for item in weather_data]
humidity = [item["humidity"] for item in weather_data]
wind_speeds = [item["wind_speed"] for item in weather_data]

#  Plot 1: Temperature Comparison
plt.figure(figsize=(10, 7))
sns.barplot(x=city_names, y=temps, palette="coolwarm")
plt.title("City-wise Temperature (°C)")
plt.xlabel("City")
plt.ylabel("Temperature")
plt.grid(True)
plt.show(block=True)


#  Plot 2: Humidity Comparison
plt.figure(figsize=(10, 7))
sns.barplot(x=city_names, y=humidity, palette="Blues")
plt.title("City-wise Humidity (%)")
plt.xlabel("City")
plt.ylabel("Humidity")
plt.grid(True)
plt.show(block=True)


#  Plot 3: Wind Speed Comparison
plt.figure(figsize=(10, 7))
sns.barplot(x=city_names, y=wind_speeds, palette="Greens")
plt.title("City-wise Wind Speed (m/s)")
plt.xlabel("City")
plt.ylabel("Wind Speed")
plt.grid(True)
plt.show(block=True)

