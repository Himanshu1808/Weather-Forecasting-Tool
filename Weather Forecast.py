import requests
import json

def get_weather_forecast(city):
    # OpenWeatherMap API endpoint URL
    url = "http://api.openweathermap.org/data/2.5/weather"

    # API key for accessing OpenWeatherMap
    api_key = "7c8a617f6aeacfe2d581f64cdd5d17b7"

    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use metric units for Celsius
    }

    try:
        # Send GET request to OpenWeatherMap API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception if status code is not 200

        # Parse JSON response
        data = response.json()

        # Extract relevant weather information
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Print the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException as e:
        print("An error occurred while retrieving the weather forecast.")
        print(f"Error details: {e}")

    except (KeyError, IndexError, json.JSONDecodeError):
        print("Failed to parse the weather forecast data.")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather_forecast(city)