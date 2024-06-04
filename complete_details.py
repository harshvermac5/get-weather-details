import json
import requests
from pprint import pprint

def get_weather_data(city):
    api_key = "60c7c2292644013f7fb8c9d434e4ec27"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Fetch temperature in Celsius
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def pretty_print_weather(data):
    if not data:
        print("No data to display.")
        return
    
    print("Weather Data for City:")
    print("="*40)
    print(f"City: {data.get('name', 'N/A')}")
    print(f"Country: {data.get('sys', {}).get('country', 'N/A')}")
    # This retrieves the value associated with the key 'coord' from the dictionary data. If the key is not found, it returns an empty dictionary {}. does the same with nested dict too.
    print(f"Coordinates: {data.get('coord', {}).get('lat', 'N/A')}, {data.get('coord', {}).get('lon', 'N/A')}")
    print("="*40)
    
    print("Main Weather:")
    print(f"Description: {data['weather'][0].get('description', 'N/A').capitalize()}")
    print(f"Temperature: {data.get('main', {}).get('temp', 'N/A')}°C")
    print(f"Feels Like: {data.get('main', {}).get('feels_like', 'N/A')}°C")
    print(f"Min Temperature: {data.get('main', {}).get('temp_min', 'N/A')}°C")
    print(f"Max Temperature: {data.get('main', {}).get('temp_max', 'N/A')}°C")
    print(f"Pressure: {data.get('main', {}).get('pressure', 'N/A')} hPa")
    print(f"Humidity: {data.get('main', {}).get('humidity', 'N/A')}%")
    print("="*40)
    
    print("Wind:")
    print(f"Speed: {data.get('wind', {}).get('speed', 'N/A')} m/s")
    print(f"Direction: {data.get('wind', {}).get('deg', 'N/A')}°")
    print("="*40)
    
    print("Cloudiness:")
    print(f"Clouds: {data.get('clouds', {}).get('all', 'N/A')}%")
    print("="*40)
    
    print("Sunrise and Sunset:")
    print(f"Sunrise: {format_unix_time(data.get('sys', {}).get('sunrise'))}")
    print(f"Sunset: {format_unix_time(data.get('sys', {}).get('sunset'))}")
    print("="*40)
    
    print("Visibility:")
    print(f"Visibility: {data.get('visibility', 'N/A')} meters")
    print("="*40)
    
    print("Rain:")
    print(f"Volume (1h): {data.get('rain', {}).get('1h', 'N/A')} mm")
    print(f"Volume (3h): {data.get('rain', {}).get('3h', 'N/A')} mm")
    print("="*40)
    
    print("Snow:")
    print(f"Volume (1h): {data.get('snow', {}).get('1h', 'N/A')} mm")
    print(f"Volume (3h): {data.get('snow', {}).get('3h', 'N/A')} mm")
    print("="*40)
    
    print("Additional Info:")
    print(f"Timezone: {data.get('timezone', 'N/A')} seconds from UTC")
    print(f"ID: {data.get('id', 'N/A')}")
    print(f"Base: {data.get('base', 'N/A')}")
    print(f"Visibility: {data.get('visibility', 'N/A')} meters")
    print(f"Weather Details: {data.get('weather', 'N/A')}")
    print(f"Sys Details: {data.get('sys', 'N/A')}")
    print(f"Main Details: {data.get('main', 'N/A')}")
    print(f"Wind Details: {data.get('wind', 'N/A')}")
    print(f"Cloud Details: {data.get('clouds', 'N/A')}")
    print("="*40)

def format_unix_time(unix_time):
    from datetime import datetime, timezone
    if unix_time:
        return datetime.fromtimestamp(unix_time, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')
    return "N/A"


def main():
    city = input('Enter the name of city: ')
    weather_data = get_weather_data(city)
    pretty_print_weather(weather_data)

if __name__ == "__main__":
    main()
