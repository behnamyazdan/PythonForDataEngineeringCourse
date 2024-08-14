import random
import pandas as pd
from datetime import datetime, timedelta
import time


# Directory paths
DATA_DIR = '../data/'


def generate_sensor_data(sensor_type, num_records):
    data = []
    for _ in range(num_records):
        timestamp = datetime.now() - timedelta(minutes=random.randint(1, 1000))
        sensor_id = random.randint(1, 10)
        if sensor_type == "temperature":
            value = round(random.uniform(15.0, 30.0), 2)
            data.append([timestamp, sensor_id, value])
        elif sensor_type == "humidity":
            value = round(random.uniform(30.0, 80.0), 2)
            data.append([timestamp, sensor_id, value])
    df = pd.DataFrame(data, columns=["timestamp", "sensor_id", f"{sensor_type}"])
    return df


def save_data_to_file():
    while True:
        # Generate data
        temp_data = generate_sensor_data("temperature", 100)
        humidity_data = generate_sensor_data("humidity", 100)

        # Get the current timestamp to use in the filename
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Save data to CSV files with timestamp in the filename
        temp_data.to_csv(f"{DATA_DIR}temperature_data_{current_time}.csv", index=False)
        humidity_data.to_csv(f"{DATA_DIR}humidity_data_{current_time}.csv", index=False)

        print(f"Data saved at {current_time}")

        # Wait for one minute before generating and saving new data
        time.sleep(60)


if __name__ == "__main__":
    save_data_to_file()
