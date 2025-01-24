import csv


def export_to_csv(data, file_name="weather_data.csv"):
    """
    Export data to a CSV file.
    :param data: List of records from the database
    :param file_name: Name of the CSV file to save
    """
    try:
        headers = ["id", "location", "latitude", "longitude", "weather_condition",
                   "temperature", "humidity", "wind_speed", "date_range", "date_requested"]

        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

        print(f"Data successfully exported to {file_name}!")
    except Exception as e:
        print(f"Failed to export data to CSV: {e}")


import json


def export_to_json(data, file_name="weather_data.json"):
    """
    Export data to a JSON file.
    :param data: List of records from the database
    :param file_name: Name of the JSON file to save
    """
    try:
        records = [
            {
                "id": row[0],
                "location": row[1],
                "latitude": row[2],
                "longitude": row[3],
                "weather_condition": row[4],
                "temperature": row[5],
                "humidity": row[6],
                "wind_speed": row[7],
                "date_range": row[8],
                "date_requested": str(row[9]),
            }
            for row in data
        ]

        with open(file_name, "w") as file:
            json.dump(records, file, indent=4)

        print(f"Data successfully exported to {file_name}!")
    except Exception as e:
        print(f"Failed to export data to JSON: {e}")

import xml.etree.ElementTree as ET

def export_to_xml(data, file_name="weather_data.xml"):
    """
    Export data to an XML file.
    :param data: List of records from the database
    :param file_name: Name of the XML file to save
    """
    try:
        root = ET.Element("WeatherData")

        for row in data:
            record = ET.SubElement(root, "Record")
            ET.SubElement(record, "ID").text = str(row[0])
            ET.SubElement(record, "Location").text = row[1]
            ET.SubElement(record, "Latitude").text = str(row[2])
            ET.SubElement(record, "Longitude").text = str(row[3])
            ET.SubElement(record, "WeatherCondition").text = row[4]
            ET.SubElement(record, "Temperature").text = str(row[5])
            ET.SubElement(record, "Humidity").text = str(row[6])
            ET.SubElement(record, "WindSpeed").text = str(row[7])
            ET.SubElement(record, "DateRange").text = row[8]
            ET.SubElement(record, "DateRequested").text = str(row[9])

        tree = ET.ElementTree(root)
        tree.write(file_name)

        print(f"Data successfully exported to {file_name}!")
    except Exception as e:
        print(f"Failed to export data to XML: {e}")
