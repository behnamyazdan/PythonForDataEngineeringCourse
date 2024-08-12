-- CREATE DATABASE ecommerce_db;

-- Create the 'customers' table
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    join_date DATE NOT NULL,
    CHECK (join_date <= CURRENT_DATE)
);

CREATE TABLE IF NOT EXISTS inventory (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL CHECK (quantity >= 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0)
);

-- Create the 'sales' table
CREATE TABLE IF NOT EXISTS sales (
    sales_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES inventory(product_id) ON DELETE CASCADE
);


-- Insert sample data into the 'customers' table
INSERT INTO customers (name, email, join_date) VALUES
('Alice Johnson', 'alice.johnson@example.com', '2024-01-15'),
('Bob Smith', 'bob.smith@example.com', '2024-02-20'),
('Charlie Brown', 'charlie.brown@example.com', '2024-03-10'),
('Diana Prince', 'diana.prince@example.com', '2024-04-05'),
('Eve Adams', 'eve.adams@example.com', '2024-05-25');

-- Insert sample data into the 'inventory' table
INSERT INTO inventory (product_name, quantity, price) VALUES
('Widget A', 100, 19.99),
('Widget B', 150, 29.99),
('Widget C', 200, 39.99),
('Widget D', 120, 49.99),
('Widget E', 180, 59.99);

-- Insert sample data into the 'sales' table
INSERT INTO sales (customer_id, product_id, amount, date) VALUES
(1, 1, 19.99, '2024-01-16'),
(2, 2, 29.99, '2024-02-22'),
(3, 3, 39.99, '2024-03-12'),
(4, 4, 49.99, '2024-04-07'),
(5, 5, 59.99, '2024-05-30'),
(1, 2, 29.99, '2024-01-18'),
(2, 3, 39.99, '2024-02-25'),
(3, 4, 49.99, '2024-03-15'),
(4, 5, 59.99, '2024-04-10'),
(5, 1, 19.99, '2024-05-28');
