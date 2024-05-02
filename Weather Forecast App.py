# Weather Forecast App
import requests

def get_weather(city):
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data['cod'] == 200:
        kelvin = 273.15
        temp = weather_data['main']['temp'] - kelvin
        print(f"Weather in {city}:")
        print(f"Temperature: {temp:.2f}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("City not found.")

city = input("Enter city name: ")
get_weather(city)
