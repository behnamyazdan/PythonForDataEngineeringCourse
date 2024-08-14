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
