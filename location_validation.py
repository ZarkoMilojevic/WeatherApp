from geopy.geocoders import Nominatim

def validate_location(location):
    """
    Validate the given location using geopy.
    :param location: Location string provided by the user
    :return: Validated location details or None
    """
    geolocator = Nominatim(user_agent="weather_app")
    try:
        location_data = geolocator.geocode(location)
        if location_data:
            return {
                "address": location_data.address,
                "latitude": location_data.latitude,
                "longitude": location_data.longitude,
            }
        else:
            print("Location not found. Please try again.")
            return None
    except Exception as e:
        print(f"Error validating location: {e}")
        return None

# Example usage
if __name__ == "__main__":
    location = input("Enter location (e.g., city name, landmark): ")
    validated = validate_location(location)
    print(validated)
