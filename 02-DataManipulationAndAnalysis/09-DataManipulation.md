# Data manipulation (filtering, sorting, grouping)

Data manipulation refers to techniques used to organize and arrange large sets of data for easier analysis. Three common techniques for data manipulation are filtering, sorting, and grouping.

- **Filtering:** This process involves hiding rows that don't meet certain criteria, allowing you to focus on specific subsets of your data. For instance, if you have a spreadsheet of customer details, you could filter it to show only customers from a particular region.
- **Sorting:** Sorting rearranges the order of your data based on a chosen column. You can sort data in ascending order (A to Z or lowest to highest) or descending order (Z to A or highest to lowest). Sorting by product category in a sales spreadsheet can help you identify top-selling items quickly.
- **Grouping:** Grouping organizes your data into categories based on shared characteristics. This helps you summarize and analyze information for each group.  For example, grouping a sales report by product category allows you to see total sales for each category.

By combining these techniques, you can effectively transform raw data into a format that's easier to understand and use for tasks like data analysis, identifying trends, and making data-driven decisions.

## Data Manipulation in Pandas with Examples

Pandas provides powerful tools for filtering, sorting, and grouping data in DataFrames. Here's how you can achieve these tasks with examples:

### Filtering:

- **Boolean Indexing:** Select rows based on a condition.

```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 22, 35], 'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Select rows where age is greater than 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)
```

- **Boolean Indexing with Multiple Conditions:** Combine conditions with logical operators (`&`, `|`, `~`) for intricate filtering.

```python
import pandas as pd

# Sample data with product categories and prices
data = {'Product': ['Laptop', 'Phone', 'Tablet', 'Watch', 'Speaker'],
        'Category': ['Electronics', 'Electronics', 'Electronics', 'Wearables', 'Electronics'],
        'Price': [800, 500, 300, 200, 100]}
df = pd.DataFrame(data)

# Filter for Electronics priced above $400
filtered_df = df[(df['Category'] == 'Electronics') & (df['Price'] > 400)]
print(filtered_df)

# Filter for non-Electronics or price below $250
filtered_df = df[~(df['Category'] == 'Electronics') | (df['Price'] < 250)]
print(filtered_df)
```

- **`.isin()` method:** Filter for rows where a column's value is present in a list.

```python
# Filter for products in specific categories
categories = ['Electronics', 'Wearables']
filtered_df = df[df['Category'].isin(categories)]
print(filtered_df)
```

- **`.query()` method:** Filter using a string expression like an SQL query.

```python
filtered_df = df.query('Age > 30 and City == "Los Angeles"')
print(filtered_df)
```

### Sorting:

- `.sort_values()` method: Sorts a DataFrame by a specified column.

```python
sorted_df = df.sort_values(by='Age')  # Sort by Age in ascending order
print(sorted_df)

sorted_df = df.sort_values(by='Name', ascending=False)  # Sort by Name in descending order
print(sorted_df)
```

**Sorting with Multi-level Sorting:**

- `.sort_values()` with multiple columns: Sort by multiple columns, specifying order for each.

```python
# Sort by Category (ascending) then by Price (descending)
sorted_df = df.sort_values(by=['Category', 'Price'], ascending=[True, False])
print(sorted_df)
```

### Grouping:

- `.groupby()` method: Groups data based on one or more columns.

```python
grouped_df = df.groupby('City')

# Get average age for each city
avg_age_by_city = grouped_df['Age'].mean()
print(avg_age_by_city)

# Get count of customers in each city
customer_count = grouped_df['Name'].count()
print(customer_count)
```

- `.groupby()` with aggregation functions: Apply various functions to grouped data.

```python
# Get descriptive statistics for each category (mean, std, min, max)
grouped_df = df.groupby('Category').describe()
print(grouped_df)

# Find the product with the highest price in each category
grouped_df = df.groupby('Category')['Price'].max()
print(grouped_df)
```

- `.transform()` method: Apply functions within groups and return the transformed values to the original DataFrame.

```python
# Calculate price percentiles within each category (add a 'Price Percentile' column)
def price_percentile(prices):
    return prices.rank(pct=True)

df['Price Percentile'] = df.groupby('Category')['Price'].transform(price_percentile)
print(df)
```



---

## Data manipulation complete example:

Pandas offers powerful tools for filtering, sorting, and grouping data. Let's explore these concepts in detail using a complex dataset.

### Creating a Complex Dataset

We'll create a dataset that simulates sales data for multiple products across different regions and dates.

```python
import pandas as pd
import numpy as np

# Creating a multi-index dataframe
index = pd.MultiIndex.from_product([
    ['North', 'South', 'East', 'West'],   # Regions
    pd.date_range('2024-01-01', periods=10, freq='D')  # Dates
], names=['Region', 'Date'])

data = {
    'Product': np.random.choice(['A', 'B', 'C', 'D'], len(index)),
    'Sales': np.random.randint(100, 500, len(index)),
    'Revenue': np.random.uniform(1000, 5000, len(index)).round(2)
}

df = pd.DataFrame(data, index=index)
print("Original DataFrame:")
print(df.head(10))
```

### 1. Filtering Data

Filtering is used to extract subsets of data based on specific conditions.

#### a. Filter by Column Values

```python
# Filter rows where Sales are greater than 300
filtered_sales = df[df['Sales'] > 300]
print("\nFiltered DataFrame (Sales > 300):")
print(filtered_sales.head(10))
```

#### b. Filter by Multiple Conditions

```python
# Filter rows where Sales are greater than 300 and Product is 'A'
filtered_sales_product = df[(df['Sales'] > 300) & (df['Product'] == 'A')]
print("\nFiltered DataFrame (Sales > 300 and Product is 'A'):")
print(filtered_sales_product.head(10))
```

#### c. Filter Using Index

```python
# Filter rows for the 'North' region
filtered_region = df.loc['North']
print("\nFiltered DataFrame (Region = 'North'):")
print(filtered_region.head(10))
```

### 2. Sorting Data

Sorting rearranges data based on the values in one or more columns.

#### a. Sort by Single Column

```python
# Sort by Sales in ascending order
sorted_sales = df.sort_values(by='Sales')
print("\nDataFrame sorted by Sales (ascending):")
print(sorted_sales.head(10))

# Sort by Sales in descending order
sorted_sales_desc = df.sort_values(by='Sales', ascending=False)
print("\nDataFrame sorted by Sales (descending):")
print(sorted_sales_desc.head(10))
```

#### b. Sort by Multiple Columns

```python
# Sort by Region first and then by Sales within each region
sorted_region_sales = df.sort_values(by=['Region', 'Sales'])
print("\nDataFrame sorted by Region and Sales (ascending):")
print(sorted_region_sales.head(10))
```

### 3. Grouping Data

Grouping is used to aggregate data based on one or more keys, and then apply a function to the grouped data.

#### a. Group by Single Column

```python
# Group by Product and calculate the total sales and revenue for each product
grouped_product = df.groupby('Product').agg({'Sales': 'sum', 'Revenue': 'sum'})
print("\nGrouped by Product (sum of Sales and Revenue):")
print(grouped_product)
```

#### b. Group by Multiple Columns

```python
# Group by Region and Product, and calculate the mean sales and revenue
grouped_region_product = df.groupby(['Region', 'Product']).agg({'Sales': 'mean', 'Revenue': 'mean'})
print("\nGrouped by Region and Product (mean Sales and Revenue):")
print(grouped_region_product)
```

#### c. Group by Index Level

```python
# Group by Region (index level) and calculate the sum of sales and revenue
grouped_index = df.groupby(level='Region').agg({'Sales': 'sum', 'Revenue': 'sum'})
print("\nGrouped by Region (index level) (sum of Sales and Revenue):")
print(grouped_index)
```

### Full Code with Explanations

Here's the complete code with detailed explanations:

```python
import pandas as pd
import numpy as np

# Creating a multi-index dataframe
index = pd.MultiIndex.from_product([
    ['North', 'South', 'East', 'West'],   # Regions
    pd.date_range('2024-01-01', periods=10, freq='D')  # Dates
], names=['Region', 'Date'])

data = {
    'Product': np.random.choice(['A', 'B', 'C', 'D'], len(index)),
    'Sales': np.random.randint(100, 500, len(index)),
    'Revenue': np.random.uniform(1000, 5000, len(index)).round(2)
}

df = pd.DataFrame(data, index=index)
print("Original DataFrame:")
print(df.head(10))

# Filtering Data

# Filter rows where Sales are greater than 300
filtered_sales = df[df['Sales'] > 300]
print("\nFiltered DataFrame (Sales > 300):")
print(filtered_sales.head(10))

# Filter rows where Sales are greater than 300 and Product is 'A'
filtered_sales_product = df[(df['Sales'] > 300) & (df['Product'] == 'A')]
print("\nFiltered DataFrame (Sales > 300 and Product is 'A'):")
print(filtered_sales_product.head(10))

# Filter rows for the 'North' region
filtered_region = df.loc['North']
print("\nFiltered DataFrame (Region = 'North'):")
print(filtered_region.head(10))

# Sorting Data

# Sort by Sales in ascending order
sorted_sales = df.sort_values(by='Sales')
print("\nDataFrame sorted by Sales (ascending):")
print(sorted_sales.head(10))

# Sort by Sales in descending order
sorted_sales_desc = df.sort_values(by='Sales', ascending=False)
print("\nDataFrame sorted by Sales (descending):")
print(sorted_sales_desc.head(10))

# Sort by Region first and then by Sales within each region
sorted_region_sales = df.sort_values(by=['Region', 'Sales'])
print("\nDataFrame sorted by Region and Sales (ascending):")
print(sorted_region_sales.head(10))

# Grouping Data

# Group by Product and calculate the total sales and revenue for each product
grouped_product = df.groupby('Product').agg({'Sales': 'sum', 'Revenue': 'sum'})
print("\nGrouped by Product (sum of Sales and Revenue):")
print(grouped_product)

# Group by Region and Product, and calculate the mean sales and revenue
grouped_region_product = df.groupby(['Region', 'Product']).agg({'Sales': 'mean', 'Revenue': 'mean'})
print("\nGrouped by Region and Product (mean Sales and Revenue):")
print(grouped_region_product)

# Group by Region (index level) and calculate the sum of sales and revenue
grouped_index = df.groupby(level='Region').agg({'Sales': 'sum', 'Revenue': 'sum'})
print("\nGrouped by Region (index level) (sum of Sales and Revenue):")
print(grouped_index)
```

This code demonstrates how to perform filtering, sorting, and grouping operations on a complex dataset using pandas. Each step includes detailed explanations and examples to help you understand the concepts and their practical applications.