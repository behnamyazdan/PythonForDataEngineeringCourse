# Pandas Practice Project: Analyzing E-commerce Orders

This project simulates real-world data analysis using Pandas. Your task is to analyze a provided dataset of e-commerce orders and answer questions about customer behavior and purchase trends.

**Dataset:**

- Use this dataset:
  https://www.kaggle.com/datasets/carrie1/ecommerce-data

- You will be given a CSV file named 

  ```
  orders.csv
  ```

   containing data on customer orders, including:

  - `order_id`: Unique identifier for each order
  - `customer_id`: Unique identifier for each customer
  - `product_id`: Unique identifier for each product
  - `product_name`: Name of the product
  - `category`: Category the product belongs to (e.g., electronics, clothing, home)
  - `price`: Price of the product
  - `order_date`: Date of the order (format: YYYY-MM-DD)
  - `city`: Customer's city
  - `country`: Customer's country

**Tasks:**

1. **Import Libraries and Load Data:**
   - Begin by importing pandas and reading the `orders.csv` file into a pandas DataFrame.
2. **Initial Data Exploration:**
   - Get basic information about the DataFrame (shape, data types, summary statistics).
   - Identify and handle any missing values present in the data.
3. **Data Cleaning and Preprocessing:**
   - Check for inconsistencies or errors in the data (e.g., invalid dates, negative prices).
   - Clean the data by correcting errors, removing outliers, or imputing missing values (if applicable).
   - Convert the `order_date` column to a datetime format for further analysis.
4. **Data Manipulation:**
   - **Filter Data:** Filter orders based on specific criteria like order date range, product category, or customer location.
   - **Sort Data:** Sort orders by various attributes like total order value, order date, or product price.
   - **Group Data:** Group orders by customer, product category, or city and calculate aggregations like total sales, average order value, or most frequent purchases.
5. **Advanced Analysis:**
   - Calculate the number of orders per customer and identify the most frequent buyers.
   - Analyze purchase trends by category or city over time (e.g., monthly sales).
   - Explore the relationship between order value and customer location.
6. **Save Results:**
   - Save the cleaned and analyzed DataFrame to a Parquet file (`orders_cleaned.parquet`) for efficient storage and later use.

7. **Additional Tips**

   - Comment your code to explain each step.

   - Make sure to handle any potential edge cases, such as missing data or incorrect data types.

   - Test your code with different subsets of the data to ensure it works correctly in various scenarios.

**Deliverables:**

- A Jupyter Notebook or Python script documenting your analysis process, including code for each task.
- Answers to the following questions based on your analysis:
  - Which product category has the highest total sales?
  - In which city do customers tend to place the most expensive orders?
  - Which customers are the most frequent buyers?
  - Are there any seasonal trends in order patterns?

This project allows students to practice essential Pandas techniques like data loading, cleaning, filtering, sorting, grouping, aggregation, and saving to Parquet files. It encourages them to explore real-world data analysis scenarios and gain practical experience working with e-commerce datasets.