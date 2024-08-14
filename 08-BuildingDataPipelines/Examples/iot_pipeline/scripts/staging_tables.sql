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