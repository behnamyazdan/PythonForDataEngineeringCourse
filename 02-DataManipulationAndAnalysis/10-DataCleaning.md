# Data cleaning in Pandas:

## What is Data Cleaning:

Data cleaning, a crucial step in data analysis, involves identifying and correcting errors, inconsistencies, and missing values within a dataset. It ensures your data is accurate and ready for further exploration and modeling. 

### Importance:

Imagine building a house – dirty bricks lead to a shaky foundation. Similarly, unclean data leads to unreliable analysis and misleading conclusions. Data cleaning is like laying a solid foundation for your data analysis journey.

### Common Issues:

- **Missing Values:** Data points might be absent for various reasons.
- **Inconsistent Formatting:** Dates, currencies, or names may have different formats (e.g., "01/01/2023" vs. "2023-01-01").
- **Data Type Errors:** Numbers might be stored as text (e.g., "123" instead of 123).
- **Typos and Outliers:** Errors in spelling or data points far outside the expected range.

### Techniques:

- **Identifying Missing Values:** Use functions like `isnull()` or `.dropna()` in Pandas to find and potentially remove or fill missing entries.
- **Handling Inconsistent Formatting:** Employ functions like `pd.to_datetime()` or string manipulation methods to standardize formats.
- **Data Type Conversion:** Use `pd.to_numeric()` or similar functions to convert data types appropriately.
- **Checking for Typos and Outliers:** Visually inspect your data or use statistical methods to identify them. Consider removing outliers if they significantly skew results.

- **Data Validation:** Establish rules to ensure data quality and consistency. Define data types, acceptable ranges, and expected formats for your data.
- **Regular Expressions:** Utilize powerful patterns in regular expressions to clean and extract specific information from text data (e.g., email addresses, phone numbers).
- **Conditional Cleaning:** Leverage boolean indexing and conditions to target specific data subsets for cleaning based on logic.
- **Custom Functions:** Create functions tailored to your specific cleaning needs. This allows for complex cleaning logic and reusability.
- **Error Handling:** Anticipate and gracefully handle potential errors during cleaning using `try-except` blocks or data validation checks.
- **Feature Engineering:** Sometimes, cleaning involves creating new features from existing data. Calculate new metrics or combine existing ones to enhance your analysis capabilities.

**Remember:** Data cleaning is an iterative process. As you explore your data and refine your analysis, you might revisit cleaning steps for further refinement. The key is to strike a balance between cleaning enough for accurate analysis and not wasting time on unnecessary cleaning efforts.

---

## Data cleaning methods in Pandas

### Identifying Missing Values:

Imagine a dataset (`data.csv`) containing customer information with a "phone number" column:

```python
import pandas as pd

data = pd.read_csv("./datasets/personal_info.csv")

# Check for missing values
missing_values = data["phone number"].isnull()
print(missing_values.sum())  # This will count the number of missing values
```

This code snippet first imports pandas and reads the data from the CSV file. Then, we use the `isnull()` function on the "phone number" column to create a boolean Series indicating missing values (True) and existing values (False). Finally, we use `sum()` to count the number of missing entries in the column.

### Handling Missing Values - Dropping Rows:

We decide to drop rows with missing phone numbers:

```python
# Drop rows with missing phone numbers (careful, data loss!)
cleaned_data = data.dropna(subset=["phone number"])
```

Here, we use the `dropna()` function on the DataFrame (`data`), specifying the subset of columns ("phone number") to consider. This will create a new DataFrame (`cleaned_data`) excluding rows with missing phone numbers in the specified column. **Be cautious** with this method, as it can lead to data loss.

### Handling Missing Values - Filling with a Constant:

Instead of dropping, we can fill missing phone numbers with a placeholder:

```python
# Fill missing values with "NA"
cleaned_data = data["phone number"].fillna("NA")

# Insert the cleaned column back into the DataFrame
data["phone number"] = cleaned_data
```

This example focuses on the "phone number" column. We use `fillna("NA")` to replace missing values with the string "NA". Then, we assign the cleaned column back to the original DataFrame, effectively replacing missing entries.

### Basic Data Type Conversion:

Suppose the "age" column is currently stored as strings. We can convert it to numeric:

```python
# Convert "age" column to numeric (assuming valid integer data)
data["age"] = pd.to_numeric(data["age"])
```

This line uses `pd.to_numeric()` to convert the "age" column to numeric format. This assumes the data in the column represents valid integers. Make sure your data is compatible with the target data type before conversion.

### Tidying Text Data:

Let's clean the "name" column by removing leading/trailing spaces:

Python

```
# Remove leading/trailing spaces from names
data["name"] = data["name"].str.strip()

# Convert names to uppercase (optional)
data["name"] = data["name"].str.upper()
```

We use the `str` accessor on the "name" column to access string methods. `str.strip()` removes extra spaces, and `str.upper()` converts the names to uppercase (optional, depending on your needs).

We've covered the basics, now let's delve into advanced data cleaning techniques using Pandas. 

#### Dataset description (orders.csv):

This dataset includes various data types, inconsistencies, and missing values to allow you to practice the techniques we discussed:

- **Product Description:** May require unit extraction with regular expressions.
- **Price:** Contains missing values, a non-numeric entry, and a price string with a dollar sign.
- **Category:** Needs to be populated based on keywords in "Product Name".
- **Order ID, City:** These columns are relatively clean for reference.

### Using Regular Expressions for Text Cleaning:

Regular expressions offer powerful pattern matching for complex text cleaning. Imagine a "Product Description" column with inconsistent units:

```python
import pandas as pd
import re

# Read data
df = pd.read_csv("./datasets/orders.csv")

# Clean product descriptions (assuming format "100g" or "100 ml")
def clean_description(text):
  pattern = r"(\d+)(\s*(g|ml))?"  # Matches number, optional space, and unit (g/ml)
  match = re.search(pattern, text)
  if match:
    return f"{match.group(1)} {match.group(2)}"  # Extract number and unit (if present)
  else:
    return text  # Return original text if no match

df["Product Description"] = df["Product Description"].apply(clean_description)

# Print cleaned descriptions
print(df["Product Description"].head())
```

This code:

1. Imports necessary libraries.
2. Reads the CSV data.
3. Defines a function `clean_description` that uses a regular expression to extract numerical values and units (grams or milliliters) from the descriptions.
4. Applies the function to the "Product Description" column using `apply()`.
5. Prints the first few entries of the cleaned column.

###  Conditional Cleaning with Boolean Indexing:

Conditional cleaning allows you to focus on specific data subsets based on conditions. For example, let's identify outliers in a "Price" column:

```python
# Identify outliers (assuming prices below $10 or above $1000 are outliers)
outlier_mask = (df["Price"] < 10) | (df["Price"] > 1000)
outlier_data = df[outlier_mask]

# Print outliers for further analysis
print(outlier_data)

# Optionally, replace outliers with appropriate values (e.g., median)
df.loc[outlier_mask, "Price"] = df["Price"].median()
```

Here, we:

1. Create a boolean mask (`outlier_mask`) using conditions to identify outlier prices.
2. Use the mask to filter the DataFrame and obtain outlier data (`outlier_data`).
3. Print the outliers for inspection.
4. Optionally, replace outliers with a chosen value (here, median) using boolean indexing to target specific rows.

### Custom Functions with `apply()` or `applymap()`:

For complex cleaning logic, you can create custom functions. Let's say you want to categorize product names based on keywords:

```python
def categorize_product(name):
  if "shirt" in name.lower():
    return "Clothing"
  elif "computer" in name.lower():
    return "Electronics"
  else:
    return "Other"

df["Category"] = df["Product Name"].apply(categorize_product)

# Print categories
print(df["Category"].value_counts())
```

This example:

1. Defines a function `categorize_product` that checks keywords in lowercase product names and assigns categories.
2. Applies the function to the "Product Name" column using `apply()`.
3. Creates a new "Category" column with the assigned categories.
4. Prints the category counts to see distribution.

### Error Handling and Data Validation:

As you deal with complex data, errors and unexpected values might arise. Here's how to handle potential issues:

```python
def convert_price(price_str):
  try:
    return float(price_str.replace("$", ""))  # Remove dollar sign and convert to float
  except ValueError:
    return None  # Handle conversion errors (e.g., invalid price format)

# Apply with error handling
df["Price"] = df["Price"].apply(convert_price)

# Validate data types after cleaning
if df["Price"].dtypes == np.float64:
  print("Price data type is valid (float)")
else:
  print("Potential issues with Price data type")
```

This code:

1. Defines a function `convert_price` that attempts to convert a price string to a float, removing the dollar sign.
2. Uses `try-except` to handle potential conversion errors

### Handling Inconsistent Dates:

Real-world data often has inconsistent date formats. Let's tackle a "Transaction Date" column with mixed formats:

```python
import pandas as pd

# Sample data with inconsistent dates
data = {
  "Transaction ID": [1, 2, 3, 4, 5],
  "Transaction Date": ["01/01/2023", "2023-02-14", "14th March 2023", "04-April-23", "Invalid Date"]
}

df = pd.DataFrame(data)

# Define a custom function to parse various date formats
def parse_date(date_str):
  try:
    # Attempt multiple formats (modify as needed for your data)
    return pd.to_datetime(date_str, format="%m/%d/%Y")  # MM/DD/YYYY
  except ValueError:
    try:
      return pd.to_datetime(date_str, format="%Y-%m-%d")  # YYYY-MM-DD
    except ValueError:
      try:
        return pd.to_datetime(date_str, format="%d %B %Y")  # DD MonthName YYYY
      except ValueError:
        return None  # Handle invalid dates

# Apply the function and set the column as datetime format
df["Transaction Date"] = df["Transaction Date"].apply(parse_date)
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

# Print cleaned dates
print(df)
```

Explanation:

1. We create a DataFrame with inconsistent date formats in the "Transaction Date" column.
2. We define a function `parse_date` that attempts to parse the date string using multiple common formats (modify these formats based on your specific data).
3. It uses `try-except` blocks to handle potential parsing errors for different formats.
4. We apply the function to the "Transaction Date" column using `apply()`.
5. Finally, we convert the parsed Series to a datetime format using `pd.to_datetime()`.

### Combining Techniques for Address Cleaning:

Imagine an "Address" column containing missing information, inconsistencies, and extra characters:

```python
# Sample data with messy addresses
data = {
  "Customer ID": [100, 101, 102, 103, 104],
  "Address": ["123 Main St. Apt. A", "456 Elm St, Anytown", "789  Oak Dr", None, "1000, Cherry Lane"]
}

df = pd.DataFrame(data)

import re

def extract_street_number(address):
  pattern = r"(\d+)(?:\s*(?:st|nd|rd|th)?)?\s*(\w*)\b"  # Matches digits, optional ordinal suffix, and street type
  match = re.search(pattern, address)
  if match:
    return match.group(1)  # Return the captured digit group (street number)
  else:
    return None  # No match found

def extract_street_name(address):
  pattern = r"(?<=^\d+\s*(?:st|nd|rd|th)?\s*)(\w+(?:\s+\w+)*)"  # Matches words after street number and optional suffix
  match = re.search(pattern, address)
  if match:
    return match.group(1)  # Return the captured group (street name)
  else:
    return None  # No match found

def extract_apartment(address):
  pattern = r"(?:\bapt|unit|#)\s*(\w+)"  # Matches "apt", "unit", or "#" followed by alphanumeric characters (apartment number)
  match = re.search(pattern, address, flags=re.IGNORECASE)  # Case-insensitive search
  if match:
    return match.group(1)  # Return the captured group (apartment number)
  else:
    return None  # No match found

# Clean and standardize addresses
df["Street Number"] = df["Address"].apply(extract_street_number)
df["Street Name"] = df["Address"].apply(extract_street_name)
df["Apartment"] = df["Address"].apply(extract_apartment)
df["Address"] = df.fillna("")  # Fill missing addresses with empty string (optional)
df["Address"] = df["Street Number"].str.cat(df["Street Name"], sep=" ") + df["Apartment"].str.cat("", sep=", ")

# Print cleaned addresses
print(df)
```

**Explanation:**

1. We create a DataFrame with messy address entries in the "Address" column.
2. We define separate functions (not shown here for brevity) to extract street numbers, street names, and apartment numbers using regular expressions (refer to regular expression documentation for specific patterns).
3. We apply these functions to the "Address" column to create separate columns for each address component.
4. We handle missing addresses with `fillna("")` (optional).
5. Finally, we concatenate the cleaned elements (street number, street name, apartment) into a standardized "Address" format.

### Feature Engineering and Data Cleaning:

Data cleaning can sometimes involve creating new features from existing data. Here's an example:

```python
# Sample data with customer purchase data (continued)
data = {
  "Customer ID": [1, 1, 2, 2, 3, 3],
  "Product Name": ["Shirt", "Headphones", "Shirt", "Laptop", "Trousers", "Coffee"],
  "Transaction Date": pd.to_datetime(["2023-01-10", "2023-01-15", "2023-02-01", "2023-02-10", "2023-03-05", "2023-03-12"])
}

df = pd.DataFrame(data)

# Calculate days since first purchase for each customer
def days_since_first_purchase(df, customer_id):
  customer_data = df[df["Customer ID"] == customer_id]
  first_purchase = customer_data["Transaction Date"].min()
  return (df["Transaction Date"] - first_purchase).dt.days.min()  # Minimum days for each customer

df["Days Since First Purchase"] = df.groupby("Customer ID")["Transaction Date"].apply(days_since_first_purchase, df)

# Print results with new feature
print(df)
```

**Explanation:**

1. We build upon the previous example, adding a "Transaction Date" column with datetime format.
2. We define a function `days_since_first_purchase` that calculates the minimum days elapsed since a customer's first purchase, considering grouping by customer ID.
3. We use `groupby()` and apply the function to calculate this new feature for each customer.
4. The result is a new column named "Days Since First Purchase" indicating customer purchase behavior.

These are just a few examples of data cleaning techniques in Pandas applicable to real-world scenarios. Remember to tailor your approach based on the specific data structure, inconsistencies, and desired outcomes for your analysis.



## Character Encodings:

Imagine a computer storing text data. Each character (letter, number, symbol) needs to be represented as a sequence of bits (0s and 1s) for the computer to understand it. Different encoding schemes define how these bits map to characters.

- **UTF-8:** Stands for "Unicode Transformation Format - 8-bit". It's the dominant encoding standard due to its ability to represent a vast range of characters from various languages and symbols.
- **ASCII:** Stands for "American Standard Code for Information Interchange". A simpler encoding limited to representing basic English characters (letters, numbers, and some symbols).
- **Latin-1 (ISO-8859-1):** Similar to ASCII but includes Western European characters (accents, special characters).
- **Other Encodings:** Many regional encodings exist, tailored to specific language requirements (e.g., CP1252 for Windows).

### Data Cleaning Challenges with Encodings

Problems arise when you work with data from diverse sources that might use different encodings. Pandas, by default, might not be able to interpret the bytes correctly, leading to data cleaning issues:

1. **Garbled Text (Mojibake):** If Pandas encounters text encoded in a way it doesn't expect, you might see strange characters or symbols instead of the intended text. This is often referred to as "mojibake."
2. **Incorrect Data Interpretation:** If numerical data is accidentally encoded as text due to encoding issues, Pandas might interpret it as strings instead of numbers. This leads to analysis errors, for example, when trying to perform calculations on "123" (encoded as text) instead of the number 123.

**Example: Let's Simulate Encoding Issues**

Here's a CSV file named "data.csv" containing product names in English and German (assuming it's saved with Latin-1 encoding):

```
Product ID,Name
1001,T-Shirt
1002,Äpfel (Apples)
1003,Coffee Mug
```

#### Scenario 1: Reading Without Specifying Encoding

```python
import pandas as pd

# Read data without specifying encoding (assuming UTF-8)
df = pd.read_csv("data.csv")

# Print data
print(df)
```

**Output:**

```
   Product ID        Name
0        1001      T-Shirt
1        1002  Ã¶pfel (Apples)  # Incorrect characters due to encoding mismatch
2        1003  Coffee Mug
```

As you can see, the German characters (Äpfel) are displayed incorrectly because Pandas interprets the bytes using UTF-8 encoding by default. This is a classic example of mojibake.

#### Scenario 2: Identifying and Addressing Encoding

```python
import pandas as pd
import chardet

# Detect encoding using chardet library
with open("data.csv", 'rb') as f:
  rawdata = f.read()
  encoding = chardet.detect(rawdata)['encoding']

# Read data with the detected encoding (Latin-1)
df = pd.read_csv("data.csv", encoding=encoding)

# Print data
print(df)
```

**Output:**

```
   Product ID        Name
0        1001      T-Shirt
1        1002   Äpfel (Apples)  # Correct characters after specifying encoding
2        1003  Coffee Mug
```

By detecting and specifying the correct encoding (Latin-1) during reading, we resolved the character display issue.

### Handling Encoding Errors:

The `errors` parameter in `pd.read_csv()` allows you to define how Pandas handles encoding issues:

- `'coerce'`: Attempts to convert characters but may replace unknown characters with a replacement marker (e.g., '?'). Use with caution as it might introduce data loss.
- `'replace'`: Replaces unknown characters with a specified value (e.g., '?').
- `'ignore'`: Skips unreadable characters but might lead to data loss.

### Best Practices:

- **Strive for UTF-8:** When possible, ensure your data is saved and processed in UTF-8 encoding for maximum compatibility.
- **Check Encoding Early:** Identify and address encoding mismatches early in your data cleaning process to prevent downstream errors.
- **Document Encoding Choices:**  Clearly document the encoding used in your data to maintain consistency and avoid issues in future collaborations.

### Additional Considerations:

- **Non-breaking Spaces and Special Characters:** Some encodings might not handle non-breaking spaces or special characters correctly. You might need to use regular expressions or specific libraries for proper handling.
- **Legacy Data:** Working with older data sources might require knowledge of historical encoding standards used at that time.
- **Mixing Encodings:** In rare cases, a single data file might contain mixed encodings. You might need to employ techniques like segmenting the data based on encoding markers or using specialized libraries for handling mixed encodings.

### Tips for Robust Data Cleaning:

- **Validate Data Sources:** If possible, understand the encoding used when obtaining data from external sources.
- **Test with Different Encodings:** If encoding is unclear, try reading the data with different encoding options to see which one yields the most consistent results.
- **Utilize Visual Inspection:** While working with text data, visually inspect the output after reading with different encodings to identify any remaining character display issues.

By understanding these considerations and best practices, you can effectively address encoding challenges during data cleaning in Pandas. 

### Reading materials:

https://realpython.com/lessons/python-unicode-overview/

https://www.kaggle.com/learn/data-cleaning

https://towardsdatascience.com/the-ultimate-guide-to-data-cleaning-3969843991d4

