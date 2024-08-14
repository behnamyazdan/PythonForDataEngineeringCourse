# Project and Hands-On Practice

In this section, we will apply the concepts learned throughout the course to a real-world project. By designing and building a complete data pipeline, you'll gain practical experience and reinforce your understanding of the ETL (Extract, Transform, Load) process. This hands-on approach will help you see how these concepts are used in a practical scenario, and provide you with the skills necessary to tackle similar challenges in your own work.

## Project Overview

For our project, we will focus on a data pipeline for an IoT (Internet of Things) application. IoT devices, such as sensors and smart devices, generate large volumes of data that need to be processed and analyzed to derive valuable insights. In this project, we will design a pipeline that handles data from IoT sensors, performs necessary transformations, and loads the processed data into a data warehouse for analysis.

![](../_assets/iot_project_diagram.webp)

### Requirements and Objectives

1. **Data Sources:** We will simulate data from various IoT sensors, such as temperature, humidity, and motion sensors. The data will be generated in real-time and stored in a database.
2. **Data Ingestion:** Develop Python scripts to extract data from simulated IoT devices and store it in a staging area.
3. **Data Transformation:** Implement transformation logic to clean, enrich, and aggregate the data. This might include converting raw sensor data into meaningful metrics, handling missing values, and aggregating data over time.
4. **Data Loading:** Load the transformed data into a data warehouse (e.g., MySQL) for further analysis and visualization.
5. **End-to-End Pipeline:** Integrate the ingestion, transformation, and loading components into a cohesive pipeline.
6. **Monitoring and Logging:** Implement error handling and logging to monitor the pipeline's performance and troubleshoot any issues.



## Hands-On Labs

In this hands-on lab, you will:

1. **Set Up Your Environment:** Ensure you have all necessary tools and libraries installed, such as Python, Pandas, and SQLAlchemy.
2. **Data Ingestion:** Write Python scripts to simulate IoT data generation and store it in a staging area. Use libraries like `requests` for API interactions if needed.
3. **Data Transformation:** Create transformation scripts using Pandas to clean and process the data. For instance, you might filter out outlier readings, handle missing values, and compute aggregate metrics like average temperature.
4. **Data Loading:** Develop scripts to load the transformed data into the MySQL data warehouse. Use SQLAlchemy or similar libraries to manage database connections and execute SQL queries.

## Review and Feedback

In this session, we will review the completed projects from the hands-on labs. Each project will be evaluated based on the following criteria:

1. **Functionality:** Does the pipeline successfully ingest, transform, and load data as expected?
2. **Code Quality:** Is the code well-written, maintainable, and adhering to best practices?
3. **Performance:** How well does the pipeline perform with varying data loads? Are there any bottlenecks?
4. **Error Handling and Logging:** Are errors handled gracefully? Is logging implemented to track pipeline performance and troubleshoot issues?

**Discussing Challenges and Solutions**

We will discuss common challenges encountered during the project and explore solutions. This includes issues related to data quality, performance optimization, error handling, and integration difficulties. Sharing experiences and solutions will help reinforce learning and provide insights into practical problem-solving.

This project will provide you with hands-on experience in designing, implementing, and optimizing a complete data pipeline. By applying what you've learned, you'll be well-prepared to tackle real-world data engineering challenges and build robust data pipelines for various applications.

----

### Step 1: Set Up Your Environment

**Objective:** Ensure you have all necessary tools and libraries installed for the project.

**Tasks:**

1. **Install Python and Required Libraries:**
   
   - Ensure Python is installed on your system. Use Python 3.x for this project.
   - Install the following Python libraries:
     - `pandas` for data manipulation
     - `sqlalchemy` for database interaction
     - `requests` if you need to interact with APIs
     - `mysql-connector-python` for MySQL connectivity
     - `pytest` for testing (optional)
   
   You can install these libraries using `pip`:
   ```bash
   pip install pandas sqlalchemy requests clickhouse_connect pytest schedule
   ```
   
2. **Set Up a Virtual Environment:**
   - Create a virtual environment to manage dependencies and isolate the project environment.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Docker (Optional):**
   - If you're using Docker to manage your database services, install Docker and Docker Compose.
   - Follow the installation instructions on the [Docker website](https://docs.docker.com/get-docker/).



### Step 2: Data Ingestion

**Objective:** Develop Python scripts to extract data from simulated IoT devices and store it in a **staging area**.

**Tasks:**

1. **Define the Data Schema:**
   
   - Define the schema for the simulated IoT data. For example:
     - **Temperature Sensor Data:** `timestamp`, `sensor_id`, `temperature`
     - **Humidity Sensor Data:** `timestamp`, `sensor_id`, `humidity`
   
2. **Simulate IoT Data Generation:**
   
   - Create a Python script to simulate data from IoT sensors. You can generate random data for testing purposes.
   - Example script to generate random temperature and humidity data:
     ```python
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
     ```
   
3. **Set Up Docker for Databases:**
   - Create a `docker-compose.yml` file to set up PostgreSQL and MySQL containers.
   - Example `docker-compose.yml` file:
     ```yaml
     name: iot_pipeline
     
     services:
       postgres:
         image: postgres:13-alpine
         container_name: postgres
         environment:
           POSTGRES_USER: postgres
           POSTGRES_PASSWORD: postgres
           POSTGRES_DB: iot_data
         ports:
           - "5433:5432"
         volumes:
           - postgres_data:/var/lib/postgresql/data
     
       # ClickHouse service
       clickhouse-server:
         image: clickhouse/clickhouse-server:latest
         container_name: clickhouse-server
         ports:
           - "8123:8123"  # HTTP port
           - "9000:9000"  # Native client port
         volumes:
           - clickhouse-data:/var/lib/clickhouse
           - clickhouse-config:/etc/clickhouse-server
         environment:
           - CLICKHOUSE_DB=mydatabase
     
       # Optional: Grafana for dashboarding
       grafana:
         image: grafana/grafana:latest
         container_name: grafana
         ports:
           - "3000:3000"
         depends_on:
           - clickhouse-server
         environment:
           - GF_SECURITY_ADMIN_PASSWORD=admin  # Default admin password for Grafana
           - GF_INSTALL_PLUGINS=grafana-clickhouse-datasource
     
     volumes:
       clickhouse-data:
       clickhouse-config:
       postgres_data:
     ```
     
   - Run Docker Compose to start the services:
     ```bash
     docker-compose up -d
     ```
   
4. **Create Staging Tables:**
   - Define staging tables in PostgreSQL to store the simulated data. Connect to the PostgreSQL container and create tables using SQL commands. Staging Table Schema:

     **1. Temperature Sensor Data:**
     - `timestamp`: The time when the data was recorded.
     - `sensor_id`: Unique identifier for the sensor.
     - `temperature`: Recorded temperature value.
   
     **2. Humidity Sensor Data:**
     - `timestamp`: The time when the data was recorded.
     - `sensor_id`: Unique identifier for the sensor.
     - `humidity`: Recorded humidity value.
   
     ```sql
     -- Create the 'temperature_sensor_data' table
     CREATE TABLE IF NOT EXISTS temperature_sensor_data (
         timestamp TIMESTAMPTZ NOT NULL,
         sensor_id INT NOT NULL,
         temperature DECIMAL(5, 2) NOT NULL,
         PRIMARY KEY (timestamp, sensor_id)
     );
     
     -- Create the 'humidity_sensor_data' table
     CREATE TABLE IF NOT EXISTS humidity_sensor_data (
         timestamp TIMESTAMPTZ NOT NULL,
         sensor_id INT NOT NULL,
         humidity DECIMAL(5, 2) NOT NULL,
         PRIMARY KEY (timestamp, sensor_id)
     );
     ```
   
     - **`timestamp TIMESTAMPTZ NOT NULL`**: The `timestamp` column records the date and time of the data entry. `TIMESTAMPTZ` ensures that the time zone is included, which is crucial for accurate timekeeping.
     - **`sensor_id INT NOT NULL`**: The `sensor_id` is an integer that uniquely identifies each sensor. This column is marked as `NOT NULL` because every data entry must be associated with a sensor.
     - **`temperature DECIMAL(5, 2) NOT NULL`**: For temperature data, `DECIMAL(5, 2)` allows for values up to 999.99 with two decimal places. The `NOT NULL` constraint ensures that a temperature value is always provided.
     - **`humidity DECIMAL(5, 2) NOT NULL`**: For humidity data, `DECIMAL(5, 2)` allows for values up to 999.99 with two decimal places. The `NOT NULL` constraint ensures that a humidity value is always provided.
     - **`PRIMARY KEY (timestamp, sensor_id)`**: The combination of `timestamp` and `sensor_id` is used as the primary key to uniquely identify each record in the table.
   
     
   
5. **Extracting and Load Data into Staging Area:**
   
   - Write a Python script to load the generated CSV files into the PostgreSQL staging tables.
   - Inserts the data into a PostgreSQL database, and then moves the processed files into an `archive` directory
   - Example script to load data into PostgreSQL:
     
     ```python
     import os
     import pandas as pd
     from sqlalchemy import create_engine
     import shutil
     
     # Database connection parameters
     DB_USERNAME = 'postgres'
     DB_PASSWORD = 'postgres'
     DB_HOST = 'localhost'
     DB_PORT = '5432'
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
     
     ```



### Step 4: Data Transformation

**Objective:** Transform the raw data from the staging area into a structured format suitable for analysis and reporting. This step involves cleaning, aggregating, and reshaping data to meet the requirements of downstream processes.

**Tasks:**

1. **Understand the Data:**
   - Review the schema and content of the staging tables (`temperature_sensor_data` and `humidity_sensor_data`).
   - Determine the transformations needed based on the project's objectives.

3. **Develop Transformation Scripts:**
   - Write Python scripts to perform the following transformations:

   **a. Data Cleaning:**
     - Handle missing or erroneous data.
     - Remove duplicates or outliers.

   **b. Data Aggregation:**
     - Aggregate data by time periods or sensor IDs, if needed.
     - Example: Calculate average temperature and humidity per day.

   **c. Data Formatting:**
     - Ensure that the data is in the desired format for loading into the data warehouse.

   **Example Transformation Script:**

   ```python
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
   
   ```
   
4. **Test Transformation Scripts:**
   - Run the transformation scripts and verify the output.
   - Check that the transformed data meets the required format and quality.

5. **Optimize Transformation:**
   - Ensure that the transformation processes are efficient and scalable.
   - Optimize scripts for performance and handle large datasets if needed.

### Step 4: Data Loading

**Objective:** Load the transformed data into ClickHouse, which will serve as the data warehouse. ClickHouse is known for its high-performance columnar storage and is ideal for analytical queries. This step includes setting up ClickHouse, creating the necessary tables, and ensuring the data is available for dashboarding in Grafana.

**Tasks:**

1. **Create Tables in ClickHouse:**

   - Define the schema for the target tables in ClickHouse that will store the transformed data.

   **SQL Statements to Create Tables in ClickHouse:**

   ```sql
   -- Create the 'daily_temperature_avg' table
   CREATE TABLE IF NOT EXISTS daily_temperature_avg (
       date Date,
       avg_daily_temperature Float32
   ) ENGINE = MergeTree()
   ORDER BY date;
   
   -- Create the 'daily_humidity_avg' table
   CREATE TABLE IF NOT EXISTS daily_humidity_avg (
       date Date,
       avg_daily_humidity Float32
   ) ENGINE = MergeTree()
   ORDER BY date;
   
   -- Create the 'hourly_temperature_avg' table
   CREATE TABLE IF NOT EXISTS hourly_temperature_avg (
       date Date,
       hour UInt8,
       avg_hourly_temperature Float32
   ) ENGINE = MergeTree()
   ORDER BY (date, hour);
   
   -- Create the 'hourly_humidity_avg' table
   CREATE TABLE IF NOT EXISTS hourly_humidity_avg (
       date Date,
       hour UInt8,
       avg_hourly_humidity Float32
   ) ENGINE = MergeTree()
   ORDER BY (date, hour);
   ```

2. **Load Data into ClickHouse:**
   - Use Python scripts to load the transformed data into ClickHouse.

   **Example Data Loading Script:**

   ```python
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
   
   ```



## Students Tasks

### Task 1: Refactor and Implement in an Object-Oriented Programming (OOP) Way

**Task Description:**
Your first task is to refactor the existing procedural code into an object-oriented structure. The goal is to create a more modular, maintainable, and reusable codebase. You should define appropriate classes that represent the different components of the data pipeline, such as `SensorDataGenerator`, `DataTransformer`, and `DataLoader`. Ensure that each class has clear responsibilities and interactions with other components.

**Expectations:**
- Define classes with attributes and methods that encapsulate the functionality of the data pipeline.
- Implement constructors (`__init__` methods) to initialize the necessary attributes for each class.
- Use inheritance or composition where applicable to reduce redundancy and improve code reuse.
- Ensure that the code is well-documented with docstrings explaining the purpose of each class and method.
- Refactor the main execution logic to interact with the defined classes, promoting separation of concerns and modularity.

### Task 2: Implement Logging for the Data Pipeline

**Task Description:** As you integrate and run the pipeline, it's crucial to implement a logging system that captures key events, errors, and performance metrics. This will help in monitoring the pipeline’s behavior, diagnosing issues, and maintaining a record of operations over time. You will use Python’s built-in logging module to create a robust logging mechanism.

**Expectations:**

- Set up a logging configuration that outputs logs to both console and file, with appropriate log levels (e.g., DEBUG, INFO, WARNING, ERROR).
- Include logging statements throughout the pipeline to track the flow of data, execution times, and any exceptions or errors.
- Ensure that logs are timestamped and include contextual information (e.g., which part of the pipeline generated the log).
- Implement log rotation or archival to manage log file size and maintain historical logs without overwhelming storage.
- Test the logging system to ensure it captures all critical information and provides clear insights into the pipeline's operation.

### Task 3: Integrate the Pipeline and Add Scheduling

**Task Description:**
With your newly refactored code, your next task is to integrate the pipeline into a cohesive system and add scheduling functionality using the "schedule" Python module. The scheduling should handle the periodic execution of the data pipeline, allowing for automated data generation, transformation, and loading at defined intervals.

**Expectations:**
- Integrate the OOP-based components to create a complete, functioning pipeline that can be triggered as a single unit.
- Implement a scheduling mechanism using the "schedule" module to execute the pipeline at regular intervals (e.g., every minute or hourly).
- Ensure that the scheduling is flexible and can be easily adjusted to different time intervals.
- Include logging to track the execution of the pipeline, capturing any errors or important events during the scheduled runs.
- Test the scheduling functionality to confirm that the pipeline operates as expected over multiple execution cycles.

### Task 4: Add Dashboard Using Grafana

**Task Description:**
The final task is to visualize the results of your data pipeline using Grafana. You will set up a dashboard in Grafana that connects to the ClickHouse database, allowing you to create real-time visualizations of the sensor data. The dashboard should display key metrics such as hourly and daily averages of temperature and humidity, with graphs and charts that provide clear insights.

**Expectations:**
- Set up Grafana and connect it to the ClickHouse database using the appropriate data source configuration.
- Design a dashboard that includes multiple panels displaying the key metrics produced by the pipeline (e.g., hourly and daily averages).
- Configure real-time or near-real-time data refresh intervals to ensure the dashboard reflects the latest available data.
- Use a variety of visualization types (e.g., line charts, bar charts) to effectively communicate the trends and patterns in the sensor data.
- Ensure that the dashboard is intuitive, with clear labels, legends, and tooltips that help interpret the data visualizations.

---

These tasks will guide you through building a robust, automated, and scalable data pipeline system that is both well-architected and easily monitored. Each task should be approached with a focus on clean code, maintainability, and the ability to extend the system in the future.