from db_connection import read_records, create_record, update_record, delete_record
from export_data import export_to_csv, export_to_json, export_to_xml
from location_validation import validate_location
from weather_api import get_weather_data


def export_menu():
    """
    Menu for exporting weather data to various formats.
    """
    data = read_records()  # Fetch all records from the database
    if not data:
        print("No data available to export.")
        return

    print("Choose an export format:")
    print("1. CSV")
    print("2. JSON")
    print("3. XML")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        export_to_csv(data)
    elif choice == "2":
        export_to_json(data)
    elif choice == "3":
        export_to_xml(data)
    else:
        print("Invalid choice. Please try again.")


def crud_menu():
    """
    Menu for CRUD operations after weather data is fetched and saved.
    """
    while True:
        print("\nWhat would you like to do next?")
        print("1. Create another entry")
        print("2. Read existing entries")
        print("3. Update an entry")
        print("4. Delete an entry")
        print("5. Return to Main Menu")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            # Prompt for manual entry of weather data
            print("\n--- Create a New Weather Entry Manually ---")
            location_manual = input("Enter the location: ")
            temperature_manual = input("Enter the temperature (in °C): ")
            weather_condition_manual = input("Enter the weather condition: ")
            humidity_manual = input("Enter the humidity (%): ")
            wind_speed_manual = input("Enter the wind speed (m/s): ")
            date_range_manual = input("Enter the date range (YYYY-MM-DD to YYYY-MM-DD): ")

            # Manually created data to save
            manual_weather_data = {
                "location": location_manual,
                "temperature": temperature_manual,
                "weather_condition": weather_condition_manual,
                "humidity": humidity_manual,
                "wind_speed": wind_speed_manual,
                "latitude": None,  # Set to none/null for latitude
                "longitude": None,  # Set to none/null for longitude
            }
            try:
                create_record(manual_weather_data, date_range_manual)
                print("New weather data manually saved to the database.")
            except Exception as e:
                print(f"Failed to save manual data: {e}")

        elif choice == "2":
            location_filter = input("Enter a location to filter by (or press Enter to see all records): ")
            records = read_records(location_filter if location_filter else None)
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found.")

        elif choice == "3":
            record_id = int(input("Enter the ID of the record to update: "))
            new_temp = input("Enter the new temperature: ")
            new_condition = input("Enter the new weather condition: ")
            updated_data = {"temperature": new_temp, "weather_condition": new_condition}
            update_record(record_id, updated_data)

        elif choice == "4":
            record_id = int(input("Enter the ID of the record to delete: "))
            delete_record(record_id)

        elif choice == "5":
            break  # Return to Main Menu
        else:
            print("Invalid choice. Please try again.")


def get_weather_menu():
    """
    Menu to fetch and display weather data for a given location, with a CRUD submenu upon successful saving.
    """
    location = input("Enter a location (e.g., city name or zip code): ")
    validated = validate_location(location)

    if validated:
        weather = get_weather_data(validated["address"])
        if "error" in weather:
            print(weather["error"])
        else:
            print("\n--- Current Weather ---")
            print(f"Location: {weather['location']}")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Condition: {weather['weather_condition']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} m/s")
            print("-----------------------\n")

            # Save data to the database
            date_range = input("Enter the date (YYYY-MM-DD) or a date range (YYYY-MM-DD to YYYY-MM-DD): ")  # Allow user to specify
            try:
                create_record(weather, date_range)
                print("Weather data successfully stored in the database!")

                # After successful saving, navigate to the CRUD menu
                crud_menu()

            except Exception as e:
                print(f"Failed to save data to the database: {e}")
    else:
        print("Invalid location. Please try again.")


def main_menu():
    """
    Displays the main menu and handles user input.
    """
    while True:
        print("\n=== Weather Application ===")
        print("1. Get Weather")
        print("2. Edit existing data")
        print("3. Export Data")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            get_weather_menu()
        elif choice == "2":
            # Here we directly invoke the CRUD menu
            print("\n--- Edit Existing Data ---")
            crud_menu()  # Call the CRUD menu directly
        elif choice == "3":
            export_menu()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main_menu()
