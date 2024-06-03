# Pandas Practice Project: Analyzing E-commerce Orders

This project simulates real-world data analysis using Pandas. Your task is to analyze a provided dataset of e-commerce orders and answer questions about customer behavior and purchase trends.

**Dataset:**

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

   - Decide whether to fill, drop, or leave the missing values based on your analysis.

   - Ensure all data types are appropriate for analysis (e.g., convert `price` to numeric).

   - Remove any duplicates if present.

     

4. **Data Manipulation:**
   - **Filter Data:** Filter orders based on specific criteria like order date range, product category, or customer location.
   - **Sort Data:** Sort orders by various attributes like total order value, order date, or product price.
   - **Group Data:** Group orders by customer, product category, or city and calculate aggregations like total sales, average order value, or most frequent purchases.

5. **Advanced Analysis:**
   - Calculate the number of orders per customer and identify the most frequent buyers.
   - Analyze purchase trends by category or city over time (e.g., monthly sales).
   - Explore the relationship between order value and customer location.

6. **Data Visualization:**

   Create various visualizations to explore the data, such as:

   - Line plots for trends over time (if applicable).
   - Scatter plots to explore relationships between numerical variables.
   - Bar plots for categorical data counts.
   - Histograms to understand the distribution of numerical data.
   - Box plots to detect outliers.

7. **Exploratory Analysis:**

    Answer key questions about the data:
  - What is the price distribution of products?
  - Are there any patterns in product purchases over time?
  - How do prices vary by city and country?
  - Which product category has the highest total sales?
  - In which city do customers tend to place the most expensive orders?
  - Which customers are the most frequent buyers?

8. **Save Results:**

   - Save the cleaned and analyzed DataFrame to a Parquet file (`orders_cleaned.parquet`) for efficient storage and later use.

9. **Additional Tips**

   - Comment your code to explain each step.

   - Make sure to handle any potential edge cases, such as missing data or incorrect data types.

   - Test your code with different subsets of the data to ensure it works correctly in various scenarios.

**Deliverables:**

- A Jupyter Notebook or Python script documenting your analysis process, including code for each task.


This project allows students to practice essential Pandas techniques like data loading, cleaning, filtering, sorting, grouping, aggregation, and saving to Parquet files. It encourages them to explore real-world data analysis scenarios and gain practical experience working with e-commerce datasets.



-------

# Exploratory Data Analysis (EDA) using Pandas, NumPy, and Matplotlib

#### Objective:
The objective of this assignment is to perform an exploratory data analysis (EDA) on a given dataset using Pandas, NumPy, and Matplotlib. You will load the dataset, clean and preprocess the data, and create various visualizations to uncover insights and patterns.

#### Instructions:

1. **Dataset Selection:**
   - Choose one of the following datasets for your analysis. These datasets are available on [Kaggle](https://www.kaggle.com/datasets):
     - [Titanic](https://www.kaggle.com/c/titanic/data)
     - [Iris Species](https://www.kaggle.com/datasets/uciml/iris)
     - [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
     - [Wine Quality](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

2. **Loading the Dataset:**
   - Import the necessary libraries (`pandas`, `numpy`, `matplotlib.pyplot`).
   - Load the dataset into a Pandas DataFrame.
   - Display the first few rows of the DataFrame.

3. **Data Cleaning and Preprocessing:**
   - Check for missing values and handle them appropriately (e.g., filling, dropping).
   - Convert categorical variables to numerical if necessary (e.g., using `pd.get_dummies` or `LabelEncoder`).
   - Remove any duplicates if present.

4. **Descriptive Statistics:**
   - Generate descriptive statistics for numerical columns (mean, median, standard deviation, etc.).
   - Provide summary statistics for categorical columns.

5. **Data Visualization:**
   - Create at least five different types of visualizations using Matplotlib:
     1. Line Plot
     2. Scatter Plot
     3. Bar Plot
     4. Histogram
     5. Box Plot
   - Customize the plots with appropriate titles, labels, and legends.

6. **Exploratory Questions:**
   - Answer the following questions using the visualizations and analyses:
     1. What are the key characteristics of the dataset?
     2. Are there any noticeable patterns or trends in the data?
     3. How do different features relate to each other?
     4. Are there any outliers or anomalies in the data?
     5. What are the distributions of the numerical features?

7. **Reporting:**
   - Write a summary report (500-1000 words) detailing your findings from the EDA.
   - Include the visualizations and describe the insights gained from each.

#### Submission:
- Submit a Jupyter Notebook containing all the code and visualizations.

#### Evaluation Criteria:
- **Completeness:** All steps of the assignment are completed.
- **Code Quality:** Code is clean, well-documented, and follows best practices.
- **Visualizations:** Plots are clear, well-labeled, and provide meaningful insights.
- **Analysis:** Answers to exploratory questions are thorough and demonstrate a good understanding of the data.

---

### Sample EDA projects in Kaggle:
https://www.kaggle.com/code/imoore/intro-to-exploratory-data-analysis-eda-in-python
https://www.kaggle.com/code/spscientist/a-simple-tutorial-on-exploratory-data-analysis
https://www.kaggle.com/code/ekami66/detailed-exploratory-data-analysis-with-python