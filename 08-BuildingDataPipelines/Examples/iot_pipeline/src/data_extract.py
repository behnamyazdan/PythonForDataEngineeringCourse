import os
import pandas as pd
from sqlalchemy import create_engine
import shutil

# Database connection parameters
DB_USERNAME = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5433'
DB_NAME = 'iot_data'

# Directory paths
DATA_DIR = '../data'
ARCHIVE_DIR = '../data/archive'

# Create a PostgreSQL database connection
engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


def process_files():
    # Ensure the archive directory exists
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    # Loop through all CSV files in the data directory
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".csv"):
            file_path = os.path.join(DATA_DIR, filename)

            # Determine the sensor type from the filename
            if "temperature" in filename:
                table_name = "temperature_sensor_data"
            elif "humidity" in filename:
                table_name = "humidity_sensor_data"
            else:
                print(f"Unknown sensor type in file: {filename}")
                continue

            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Insert the data into the appropriate table in PostgreSQL
            try:
                df.to_sql(table_name, engine, if_exists='append', index=False)
                print(f"Inserted data from {filename} into {table_name} table.")
            except Exception as e:
                print(f"Error inserting data from {filename}: {e}")
                continue

            # Move the processed file to the archive directory
            archive_path = os.path.join(ARCHIVE_DIR, filename)
            shutil.move(file_path, archive_path)
            print(f"Moved {filename} to archive.")


if __name__ == "__main__":
    process_files()
