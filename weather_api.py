import requests

API_KEY = "your_openweathermap_api_key"  # Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(location):
    """
    Fetch weather data for the given location.
    :param location: City name, Zip code, or GPS coordinates (latitude,longitude)
    :return: Dictionary containing weather data or error message
    """
    try:
        # Form the request URL
        params = {"q": location, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Extract relevant data
        weather_data = {
            "location": data.get("name"),
            "latitude": data["coord"]["lat"],
            "longitude": data["coord"]["lon"],
            "temperature": data["main"]["temp"],
            "weather_condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return weather_data
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather data: {e}"}

# Example usage
if __name__ == "__main__":
    location = input("Enter location (e.g., city name, zip code): ")
    weather = get_weather_data(location)
    print(weather)
