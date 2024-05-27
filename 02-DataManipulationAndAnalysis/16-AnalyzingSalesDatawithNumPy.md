# Analyzing Sales Data with NumPy

You are working as a data analyst for a retail company. Your task is to analyze sales data for a given period and provide insights to the management team. The dataset contains information about sales transactions, including the date of the transaction, product ID, quantity sold, and revenue generated.

### Dataset:

The dataset 'sales_data.csv' contains the following columns:

- **Date**: Date of the transaction (format: YYYY-MM-DD).
- **Product_ID**: ID of the product sold.
- **Quantity**: Quantity of the product sold.
- **Revenue**: Revenue generated from the sale.

### Tasks:

1. **Data Loading and Preparation**

   - Load the dataset 'sales_data.csv' into a NumPy array.
   - Display the first 5 rows of the array to inspect the data.

2. **Data Analysis with NumPy**

   - Calculate the total revenue generated during the entire period.
   - Determine the average quantity sold per transaction.
   - Find the maximum revenue generated from a single transaction.

3. **Advanced Data Analysis**

   - Identify the top 5 best-selling products based on revenue.
   - Calculate the total revenue and quantity sold for each product.

   

```python
import numpy as np

# Task 1: Data Loading and Preparation
data = np.genfromtxt('./datasets/sales_data.csv', delimiter=',', dtype=None, names=True)
print("First 5 rows of the data:")
print(data[:5])

# Task 2: Data Analysis with NumPy
total_revenue = np.sum(data['Revenue'])
avg_quantity_per_transaction = np.mean(data['Quantity'])
max_revenue_per_transaction = np.max(data['Revenue'])

print("\nTotal revenue generated:", total_revenue)
print("Average quantity sold per transaction:", avg_quantity_per_transaction)
print("Maximum revenue from a single transaction:", max_revenue_per_transaction)

# Task 3: Advanced Data Analysis
sorted_indices = np.argsort(data['Revenue'])[::-1]  # Sort indices in descending order of revenue
top_5_products = data['Product_ID'][sorted_indices][:5]  # Top 5 product IDs based on revenue

print("\nTop 5 best-selling products based on revenue:")
for product_id in top_5_products:
    product_data = data[data['Product_ID'] == product_id]
    total_revenue_product = np.sum(product_data['Revenue'])
    total_quantity_product = np.sum(product_data['Quantity'])
    print(f"Product ID: {product_id}, Total Revenue: {total_revenue_product}, Total Quantity Sold: {total_quantity_product}")
```

This code performs the following tasks:
1. Loads the sales data from 'sales_data.csv' into a NumPy array.
2. Calculates the total revenue, average quantity sold per transaction, and maximum revenue from a single transaction.
3. Identifies the top 5 best-selling products based on revenue and calculates the total revenue and quantity sold for each product.
