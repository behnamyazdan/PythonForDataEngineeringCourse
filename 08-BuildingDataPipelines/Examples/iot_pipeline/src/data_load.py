import pandas as pd
import clickhouse_connect

# Directory paths
RESULT_DIR = '../data/result/'

# ClickHouse connection
client = clickhouse_connect.get_client(host='localhost', port=8123)


def load_data():
    # Load transformed data from CSV files
    temp_avg_data_hourly = pd.read_csv(f'{RESULT_DIR}hourly_temperature_avg.csv')
    temp_avg_data_daily = pd.read_csv(f'{RESULT_DIR}daily_temperature_avg.csv')
    humidity_avg_data_hourly = pd.read_csv(f'{RESULT_DIR}hourly_humidity_avg.csv')
    humidity_avg_data_daily = pd.read_csv(f'{RESULT_DIR}daily_humidity_avg.csv')

    # Convert 'date' column to datetime.date type
    temp_avg_data_hourly['date'] = pd.to_datetime(temp_avg_data_hourly['date']).dt.date
    temp_avg_data_daily['date'] = pd.to_datetime(temp_avg_data_daily['date']).dt.date
    humidity_avg_data_hourly['date'] = pd.to_datetime(humidity_avg_data_hourly['date']).dt.date
    humidity_avg_data_daily['date'] = pd.to_datetime(humidity_avg_data_daily['date']).dt.date

    # Load data into ClickHouse tables
    client.insert_df('hourly_temperature_avg', temp_avg_data_hourly)
    client.insert_df('daily_temperature_avg', temp_avg_data_daily)
    client.insert_df('hourly_humidity_avg', humidity_avg_data_hourly)
    client.insert_df('daily_humidity_avg', humidity_avg_data_daily)

# Execute data loading
load_data()
