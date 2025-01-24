from db_connection import read_records
from export_data import export_to_csv, export_to_json, export_to_xml

# The method to display initial menu is mssing.

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
