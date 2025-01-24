import pymysql

def connect_to_db():
    """
    Establish a connection to the MySQL database.
    :return: Connection object
    """
    return pymysql.connect(
        host="localhost",
        user="weatheruser",  # Replace with your MySQL username
        password="1234",  # Replace with your MySQL password
        database="weatherapp"  # Replace with your database name
    )
def create_record(weather_data, date_range):
    """
    Store weather data in the database.
    :param weather_data: Dictionary containing weather details
    :param date_range: String containing date range
    """
    query = """
    INSERT INTO WeatherData (location, latitude, longitude, weather_condition, temperature, humidity, wind_speed, date_range)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        weather_data["location"],
        weather_data["latitude"],
        weather_data["longitude"],
        weather_data["weather_condition"],
        weather_data["temperature"],
        weather_data["humidity"],
        weather_data["wind_speed"],
        date_range,
    )

    connection = connect_to_db()
    with connection.cursor() as cursor:
        cursor.execute(query, values)
        connection.commit()
    connection.close()
    print("Weather data successfully stored in the database!")

def read_records(location=None):
    """
    Fetch weather data from the database.
    :param location: Optional location filter
    :return: List of records
    """
    query = "SELECT * FROM WeatherData"
    if location:
        query += " WHERE location = %s"

    connection = connect_to_db()
    with connection.cursor() as cursor:
        cursor.execute(query, (location,) if location else None)
        results = cursor.fetchall()
    connection.close()
    return results

def update_record(record_id, updated_data):
    """
    Update a specific weather record.
    :param record_id: ID of the record to update
    :param updated_data: Dictionary of updated fields
    """
    query = """
    UPDATE WeatherData
    SET temperature = %s, weather_condition = %s
    WHERE id = %s
    """
    values = (updated_data["temperature"], updated_data["weather_condition"], record_id)

    connection = connect_to_db()
    with connection.cursor() as cursor:
        cursor.execute(query, values)
        connection.commit()
    connection.close()
    print(f"Record {record_id} updated successfully!")

def delete_record(record_id):
    """
    Delete a weather record from the database.
    :param record_id: ID of the record to delete
    """
    query = "DELETE FROM WeatherData WHERE id = %s"

    connection = connect_to_db()
    with connection.cursor() as cursor:
        cursor.execute(query, (record_id,))
        connection.commit()
    connection.close()
    print(f"Record {record_id} deleted successfully!")

