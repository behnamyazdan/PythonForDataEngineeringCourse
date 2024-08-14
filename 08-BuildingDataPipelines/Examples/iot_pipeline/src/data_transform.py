import os
import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
DB_USERNAME = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'iot_data'

# Directory paths
RESULT_DIR = '../data/result/'

# Create a PostgreSQL database connection
engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


def transform_data():

    # Ensure the archive directory exists
    os.makedirs(RESULT_DIR, exist_ok=True)

    # Load data from staging tables
    temp_data = pd.read_sql('SELECT * FROM temperature_sensor_data', engine)
    humidity_data = pd.read_sql('SELECT * FROM humidity_sensor_data', engine)

    # Data Cleaning
    temp_data.dropna(inplace=True)
    humidity_data.dropna(inplace=True)
    temp_data.drop_duplicates(inplace=True)
    humidity_data.drop_duplicates(inplace=True)

    # Data Aggregation
    temp_data['date'] = temp_data['timestamp'].dt.date
    humidity_data['date'] = humidity_data['timestamp'].dt.date
    temp_data['hour'] = temp_data['timestamp'].dt.hour
    humidity_data['hour'] = humidity_data['timestamp'].dt.hour

    # Daily Mean Calculation
    daily_temp_avg = temp_data.groupby('date')['temperature'].mean().reset_index()
    daily_humidity_avg = humidity_data.groupby('date')['humidity'].mean().reset_index()

    # Hourly Mean Calculation
    hourly_temp_avg = temp_data.groupby(['date', 'hour'])['temperature'].mean().reset_index()
    hourly_humidity_avg = humidity_data.groupby(['date', 'hour'])['humidity'].mean().reset_index()

    # Round the mean values to 2 decimal places
    daily_temp_avg['temperature'] = daily_temp_avg['temperature'].round(2)
    daily_humidity_avg['humidity'] = daily_humidity_avg['humidity'].round(2)
    hourly_temp_avg['temperature'] = hourly_temp_avg['temperature'].round(2)
    hourly_humidity_avg['humidity'] = hourly_humidity_avg['humidity'].round(2)

    # Data Formatting
    daily_temp_avg.rename(columns={'temperature': 'avg_daily_temperature'}, inplace=True)
    daily_humidity_avg.rename(columns={'humidity': 'avg_daily_humidity'}, inplace=True)
    hourly_temp_avg.rename(columns={'temperature': 'avg_hourly_temperature'}, inplace=True)
    hourly_humidity_avg.rename(columns={'humidity': 'avg_hourly_humidity'}, inplace=True)

    # Save transformed data to CSV
    daily_temp_avg.to_csv(f'{RESULT_DIR}daily_temperature_avg.csv', index=False)
    daily_humidity_avg.to_csv(f'{RESULT_DIR}daily_humidity_avg.csv', index=False)
    hourly_temp_avg.to_csv(f'{RESULT_DIR}hourly_temperature_avg.csv', index=False)
    hourly_humidity_avg.to_csv(f'{RESULT_DIR}hourly_humidity_avg.csv', index=False)

    # Load transformed data to the database or data warehouse
    daily_temp_avg.to_sql('daily_temperature_avg', engine, if_exists='replace', index=False)
    daily_humidity_avg.to_sql('daily_humidity_avg', engine, if_exists='replace', index=False)
    hourly_temp_avg.to_sql('hourly_temperature_avg', engine, if_exists='replace', index=False)
    hourly_humidity_avg.to_sql('hourly_humidity_avg', engine, if_exists='replace', index=False)


# Execute transformation
transform_data()
