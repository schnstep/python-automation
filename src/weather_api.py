#!/usr/bin/env python3
"""
weather_api.py - Get weather data from free API
"""

import requests
import json
from datetime import datetime

def get_weather(city="Innsbruck"):
    """
    Get weather data for a city using wttr.in API
    (No API key required!)
    """
    # API endpoint
    url = f"http://wttr.in/{city}?format=j1"

    print(f"🌤️  Fetching weather data for {city}...")

    try:
        # Make GET request
        response = requests.get(url, timeout=10)

        # Check if request was successful
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Extract current conditions
        current = data['current_condition'][0]

        print(f"\n{'='*50}")
        print(f"WEATHER REPORT: {city}")
        print(f"{'='*50}")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"Temperature: {current['temp_C']}°C (feels like {current['FeelsLikeC']}°C)")
        print(f"Condition: {current['weatherDesc'][0]['value']}")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind: {current['windspeedKmph']} km/h {current['winddir16Point']}")
        print(f"{'='*50}")
        
        return data
    
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out")
        return None
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API")
        return None
        
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return None
        
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON response")
        return None
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None
    
def get_forecast(city="Innsbruck", days=3):
    """Get weather forecast"""
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        print(f"\n{days}-DAY FORECAST: {city}")
        print("=" * 50)

        for day in data['weather'][:days]:
            date = day['date']
            max_temp = day['maxtempC']
            min_temp = day['mintempC']
            desc = day['hourly'][0]['weatherDesc'][0]['value']
            
            print(f"{date}: {min_temp}°C - {max_temp}°C | {desc}")

        print("=" * 50)
    
    except Exception as e:
        print(f"❌ Error fetching forecast: {e}")

if __name__ == "__main__":
    # Get current weather
    weather = get_weather()

    # Get forecast if current weather succeeded
    if weather:
        get_forecast("Innsbruck", days=3)