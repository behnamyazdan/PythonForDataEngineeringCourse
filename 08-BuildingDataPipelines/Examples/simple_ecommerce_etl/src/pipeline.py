import logging
import pandas as pd
from sqlalchemy import create_engine
from config import POSTGRESQL_CONFIG, MYSQL_CONFIG
from logging_config import LoggingConfig

# Set up logging
LoggingConfig.setup_logging('../logs/etl_pipeline.logs')


class Extractor:
    def __init__(self, config):
        self.engine = create_engine(
            f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['dbname']}")

    def extract_data(self, query):
        try:
            logging.info("Starting data extraction")
            data = pd.read_sql_query(query, self.engine)
            logging.info("Data extraction completed successfully")
            return data
        except Exception as e:
            logging.error(f"Data extraction failed: {str(e)}")
            print(f"Error during extraction: {str(e)}")
            raise


class Transformer:
    def transform_data(self, data):
        try:
            logging.info("Starting data transformation")

            # Convert 'date' column to datetime if it's not already
            if not pd.api.types.is_datetime64_any_dtype(data['date']):
                data['date'] = pd.to_datetime(data['date'])

            # Example transformation: Convert amount to USD
            data['amount_usd'] = data['amount'] * 1.1

            # Create the 'dim_date' dataframe
            data['year'] = data['date'].dt.year
            data['month'] = data['date'].dt.month
            data['day'] = data['date'].dt.day
            data['quarter'] = data['date'].dt.quarter
            data['day_of_week'] = data['date'].dt.dayofweek + 1
            data['week_of_year'] = data['date'].dt.isocalendar().week
            dim_dates = data[['date', 'year', 'quarter', 'month', 'day_of_week', 'week_of_year']].drop_duplicates()
            dim_dates = dim_dates.rename(columns={'date': 'date'})

            # Create 'dim_customers' dataframe
            dim_customers = data[['customer_id', 'name', 'email', 'join_date']].drop_duplicates()

            # Create 'dim_inventory' dataframe
            dim_inventory = data[['product_id', 'product_name', 'quantity', 'price']].drop_duplicates()

            # Create 'fact_sales' dataframe
            fact_sales = data[['sales_id', 'customer_id', 'product_id', 'amount', 'date', 'amount_usd']]
            fact_sales = fact_sales.rename(columns={'date': 'date'})

            logging.info("Data transformation completed successfully")
            return fact_sales, dim_customers, dim_inventory, dim_dates
        except Exception as e:
            logging.error(f"Data transformation failed: {str(e)}")
            print(f"Error during transformation: {str(e)}")
            raise


class Loader:
    def __init__(self, config):
        self.engine = create_engine(
            f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['dbname']}")

    def load_data(self, data, table_name):
        try:
            logging.info(f"Starting data load into {table_name}")
            data.to_sql(table_name, self.engine, if_exists='append', index=False)
            logging.info(f"Data load into {table_name} completed successfully")
        except Exception as e:
            logging.error(f"Data load into {table_name} failed: {str(e)}")
            print(f"Error during loading into {table_name}: {str(e)}")
            raise


class ETL:
    def __init__(self, extract_query):
        self.extractor = Extractor(POSTGRESQL_CONFIG)
        self.transformer = Transformer()
        self.loader = Loader(MYSQL_CONFIG)
        self.extract_query = extract_query

    def run(self):
        try:
            data = self.extractor.extract_data(self.extract_query)
            fact_sales, dim_customers, dim_inventory, dim_dates = self.transformer.transform_data(data)

            # Load dimension tables
            self.loader.load_data(dim_customers, 'dim_customer')
            self.loader.load_data(dim_inventory, 'dim_inventory')
            self.loader.load_data(dim_dates, 'dim_date')

            # Load fact table
            self.loader.load_data(fact_sales, 'fact_sales')

            logging.info("ETL pipeline executed successfully")
            print("ETL pipeline executed successfully")
        except Exception as e:
            logging.error(f"ETL pipeline failed: {str(e)}")
            print(f"ETL pipeline failed: {str(e)}")


if __name__ == "__main__":
    # Define your ETL process
    extract_query = """
    SELECT s.sales_id, s.customer_id, s.product_id, s.amount, s.date, c.name, c.email, c.join_date, p.product_name, p.quantity, p.price
    FROM sales s
    JOIN customers c ON s.customer_id = c.customer_id
    JOIN inventory p ON s.product_id = p.product_id;
    """

    # Create and run the ETL process
    etl_pipeline = ETL(extract_query)
    etl_pipeline.run()
