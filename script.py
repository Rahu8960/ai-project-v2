import json
import urllib.request

def get_weather_info(city_name="London"):
    """
    Fetch basic weather data for a given city using a public API endpoint.
    """
    url = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true"
    
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        
        current_weather = data.get("current_weather", {})
        temp = current_weather.get("temperature")
        windspeed = current_weather.get("windspeed")
        
        print(f"--- Weather Report ---")
        print(f"Temperature: {temp}°C")
        print(f"Wind Speed: {windspeed} km/h")
        
    except Exception as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    print("Executing Open-Source Weather Script...")
    get_weather_info()
