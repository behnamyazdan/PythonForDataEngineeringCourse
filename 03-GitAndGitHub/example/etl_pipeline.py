import pandas as pd
import sqlite3
import os


def extract_data():
    # Read raw data files
    products = pd.read_csv('raw_data/products.csv')
    sales = pd.read_csv('raw_data/sales.csv')
    customers = pd.read_csv('raw_data/customers.csv')
    print("Data extraction completed.")
    return products, sales, customers


def transform_data(products, sales, customers):

    # Ensure 'Quantity' column is of numeric type
    sales['Quantity'] = pd.to_numeric(sales['Quantity'], errors='coerce')
    products['Price'] = pd.to_numeric(products['Price'], errors='coerce')

    # Transform Product_Sales data
    product_sales = sales.merge(products, on='ProductID')
    product_sales['TotalPrice'] = product_sales['Quantity'] * product_sales['Price']
    product_sales = product_sales[['SaleID', 'ProductName', 'Category', 'Quantity', 'TotalPrice', 'SaleTimestamp']]
    product_sales.to_csv('transformed_data/product_sales.csv', index=False)

    # Transform Customer_Sales data
    customer_sales = sales.merge(customers, on='CustomerID')
    customer_sales = customer_sales[['SaleID', 'CustomerName', 'Email', 'ProductID', 'Quantity', 'SaleTimestamp']]
    customer_sales.to_csv('transformed_data/customer_sales.csv', index=False)

    print("Data transformation completed.")
    return product_sales, customer_sales


def load_data():

    if not os.path.exists("database/etl_pipeline.db"):
        os.mkdir('database')

    # Database connection
    conn = sqlite3.connect('database/etl_pipeline.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product_sales (
            SaleID INTEGER,
            ProductName TEXT,
            Category TEXT,
            Quantity INTEGER,
            TotalPrice REAL,
            SaleTimestamp TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_cales (
            SaleID INTEGER,
            CustomerName TEXT,
            Email TEXT,
            ProductID INTEGER,
            Quantity INTEGER,
            SaleTimestamp TEXT
        )
    ''')

    # Load transformed data
    product_sales = pd.read_csv('transformed_data/product_Sales.csv')
    customer_sales = pd.read_csv('transformed_data/customer_Sales.csv')

    # Insert data into tables
    product_sales.to_sql('product_sales', conn, if_exists='replace', index=False)
    customer_sales.to_sql('customer_sales', conn, if_exists='replace', index=False)

    # Commit and close connection
    conn.commit()
    conn.close()

    print("Data loading completed.")


def main():
    # Ensure directories exist
    os.makedirs('raw_data', exist_ok=True)
    os.makedirs('transformed_data', exist_ok=True)

    # Step 1: Data Extraction
    print("Starting data extraction...")
    products, sales, customers = extract_data()

    # Step 2: Data Transformation
    print("Starting data transformation...")
    transform_data(products, sales, customers)

    # Step 3: Data Loading
    print("Starting data loading...")
    load_data()

    print("ETL pipeline completed.")


if __name__ == "__main__":
    main()
