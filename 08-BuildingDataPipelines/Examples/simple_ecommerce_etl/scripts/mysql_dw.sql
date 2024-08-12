CREATE DATABASE IF NOT EXISTS data_warehouse;

CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    join_date DATE NOT NULL
);


CREATE TABLE IF NOT EXISTS dim_inventory (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL CHECK (quantity >= 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0)
);


CREATE TABLE IF NOT EXISTS dim_date (
    date_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    year INT NOT NULL,
    quarter INT NOT NULL CHECK (quarter BETWEEN 1 AND 4),
    month INT NOT NULL CHECK (month BETWEEN 1 AND 12),
    day_of_week INT NOT NULL CHECK (day_of_week BETWEEN 1 AND 7),
    week_of_year INT NOT NULL CHECK (week_of_year BETWEEN 1 AND 53),
    UNIQUE (date)
);

-- Example insert statement for dim_date
-- You may want to generate these rows programmatically to cover a range of dates
INSERT INTO dim_date (date, year, quarter, month, day_of_week, week_of_year)
VALUES ('2024-01-01', 2024, 1, 1, 1, 1);  -- Add more rows as needed


CREATE TABLE IF NOT EXISTS fact_sales (
    sales_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    amount_usd DECIMAL(10, 2) NOT NULL CHECK (amount_usd > 0),
    date DATETIME NOT NULL,
    -- You can add indexes for performance
    INDEX (customer_id),
    INDEX (product_id)
);
