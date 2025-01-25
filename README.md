# Project Overview

**Purpose:** A Python weather app allowing users to retrieve weather data, store it in a MySQL database, and perform CRUD operations on the stored data.

**Technologies Used:**
- **Programming Language:** Python
- **API Integration:** OpenWeatherMap API (or any weather API of choice)
- **Database:** MySQL
- **Optional Exports:** CSV, JSON, XML, PDF

---

# Core Features Implementation

## 2.1 Input Validation and User Guidance

### Location Input Options:
Users can enter:
- Zip Code/Postal Code
- City Name

### Date Range Validation:
- Validate input date formats (e.g., YYYY-MM-DD).
- Ensure the start date is earlier than the end date.
- Ensure date range is realistic (e.g., not in the distant past or future).

---

## 2.2 API Integration

### Weather Data Retrieval:
- Use OpenWeatherMap API for weather data.
- Extract details like temperature, weather condition, humidity, wind speed, etc.

---

## 2.3 Database Setup

### MySQL Database Schema included.

### CRUD Operations:

- **CREATE:** Store user-entered location, date range, and retrieved weather data.
- **READ:** Allow users to query weather data by location or date range.
- **UPDATE:** Enable updates to stored weather data (e.g., temperature, conditions).
- **DELETE:** Allow deletion of specific records by ID or location.

---

# Code Structure

## Modules/Packages to Use:
- `requests` for API calls
- `pymysql` or `mysql-connector-python` for MySQL integration
- `geopy` for location validation
- `json`, `csv`, or `xml.etree.ElementTree` for export functionality

---

### File Descriptions:

- **`main.py`**: This is the entry point for the application. It initializes and runs the app.
- **`db_connection.py`**: This file contains functions for connecting to the MySQL database, as well as performing CRUD operations (Create, Read, Update, Delete) on the weather data.
- **`weather_api.py`**: Responsible for fetching weather data from the weather API (e.g., OpenWeatherMap) and processing the response.
- **`location_validation.py`**: Validates and processes the location input from the user (either city name or zip code) to ensure it is accurate and properly formatted.
- **`export_data.py`**: Provides functionality for exporting stored weather data into different formats like CSV, JSON, and XML.

---

