## Reading and Writing Data from/to Different File Formats in Pandas

Pandas excels at working with various file formats commonly used for storing tabular data. This guide explains how to read from and write to these formats with examples.

## Key File Formats:

- **CSV (Comma-Separated Values):** A popular format with data separated by commas (`,`).
- **Excel Files (XLSX, XLSX):** Spreadsheets commonly used in Microsoft Excel.
- **JSON (JavaScript Object Notation):** A text-based format using key-value pairs to represent data.
- **Parquet:** A columnar format optimized for large datasets, offering efficient storage and retrieval.

### 1- CSV (Comma-Separated Values):

- Structure:

   Line-based, with each line representing a record.

  Lines:

  - **Header (Optional):** The first line can optionally contain column names. Each column name is separated by a comma.
  - **Data Rows:** Subsequent lines represent data records. Each record consists of data values for each column, again separated by commas.

  ```
  Name,Age,City (This is the header line)
  Alice,30,New York
  Bob,25,Los Angeles
  Charlie,42,Chicago
  ```

- **Pros:**
  - Simple and human-readable.
  - Widely supported by various applications.
  - Compact and efficient for smaller datasets.
- **Cons:**
  - Limited data type support (primarily strings and numbers).
  - Can become unwieldy for large datasets due to size and lack of compression.
- **Use Cases:**
  - Sharing data between different software programs.
  - Storing basic tabular data for analysis.

#### 2- Excel Files (XLSX, XLSX):

- Structure:

   Sheet-based, with each sheet storing a two-dimensional grid of data.

  - **Sheets:** Excel files can contain multiple sheets, each with a separate name.
  - **Cells:** Each sheet is made up of cells arranged in rows and columns. A cell can contain a data value (text, number, date, etc.), formatting information, or a formula.
  - **Rows and Columns:** Rows are numbered starting from 1, and columns are lettered (A, B, C, ...).
  - **Formatting:** Excel allows applying various formatting options to cells, including font styles, borders, and background colors.

  ```
  +-----------+----------+----------+
  |  Sheet1   |          |          |
  +-----------+----------+----------+
  | Row 1 (A) |  Value1  |  Value2  |
  | Row 1 (B) |  Value3  |  Value4  |
  | Row 2 (A) |  Value5  |  Value6  |
  | Row 2 (B) |  Value7  |  Value8  |
  +-----------+----------+----------+
  ```
  
- **Pros:**

  - Rich formatting capabilities for presenting data visually.
  - Familiar and user-friendly for manual manipulation.
  - Supports various data types, including numbers, text, dates, and formulas.

- **Cons:**

  - File size can be large, especially with complex formatting and multiple sheets.
  - Potential compatibility issues across different Excel versions and software.

- **Use Cases:**

  - Data entry and manipulation for human users.
  - Sharing data with users who need visual representations.
  - Storing formatted reports and presentations.

#### 3- JSON (JavaScript Object Notation):

- **Structure:**

   Key-value pair based, representing data in a hierarchical way.

  - **Objects:** The core structure is an object, which consists of key-value pairs enclosed in curly braces `{}`. Keys are strings that identify the data, and values can be strings, numbers, booleans, arrays, or nested objects.
  - **Arrays:** Arrays are ordered lists of values enclosed in square brackets `[]`. Each element in the array can be any valid JSON data type.
  - **Nesting:** Objects and arrays can be nested within each other to represent complex data structures.

  ```json
  {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "music", "travel"]
  }
  ```

- **Pros:**

  - Human-readable and machine-readable for various programming languages.
  - Flexible for representing complex data structures.
  - Widely used for data exchange in web APIs.

- **Cons:**

  - Can be verbose compared to other formats for simple tabular data.
  - Limited data type support compared to some other formats.

- **Use Cases:**

  - Data exchange between web applications and APIs.
  - Storing configuration settings and metadata.
  - Representing complex, nested data structures.

#### 4- Parquet:

- **Structure:**

   Columnar, where data for each column is stored separately and compressed efficiently.

  - **Columns:** Data is organized into columns, with each column containing values for a specific data type (e.g., integer, string, boolean).
  - **Parquet Row Group:** A group of rows within a column that is compressed together. This allows for efficient retrieval of specific columns.
  - **Metadata:** Parquet files also store metadata about the data, such as data types, column names, and compression algorithms used.

  **Conceptual Example (Simplified):**

  ```
  +----------+----------+----------+----------+
  | Column1  | Column2  | Column3  | ...      |
  +----------+----------+----------+----------+
  | Value1_1 | Value2_1 | Value3_1 | ...      |
  | Value1_2 | Value2_2 | Value3_2 | ...      |
  | Value1_3 | Value2_3 | Value3_3 | ...      |
  +----------+----------+----------+----------+
  ```

- **Pros:**

  - Highly compressed, leading to smaller file sizes compared to CSV or JSON.
  - Faster data access, especially when querying specific columns.
  - Well-suited for big data analytics and data warehousing.

- **Cons:**

  - Requires specialized libraries for reading and writing.
  - Not as human-readable as CSV or JSON.

- **Use Cases:**

  - Storing and analyzing large datasets efficiently.
  - Data warehousing and big data pipelines.
  - When fast data access for specific columns is critical.

## Reading Data (Using `read_\*` Functions):

Pandas provides a collection of functions with the prefix `read_` to read from different file formats:

- **`read_csv()`**: Reads CSV files.
- **`read_excel()`**: Reads Excel files (supports various Excel file extensions).
- **`read_json()`**: Reads JSON files.
- **`read_parquet()`**: Reads Parquet files.

### Reading a CSV File

```python
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')
print(df.head())  # Display the first few rows
```

#### Specifying Delimiter and Handling Missing Values

```python
# Read a CSV with a different delimiter (e.g., tab-separated)
df = pd.read_csv('data.txt', sep='\t')

# Handle missing values (NaN) by replacing with a specific value
df = pd.read_csv('data.csv', na_values=['NA', ''])  # Replace 'NA' and empty strings with NaN
```

### Reading Multiple Sheets from Excel and Parquet Options:



```python
# Read specific sheets from an Excel file
df1 = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df2 = pd.read_excel('data.xlsx', sheet_name='Sheet2')

# Read a Parquet file with specific columns
df = pd.read_parquet('data.parquet', columns=['col1', 'col2'])
```

## Writing Data (Using `to_\*` Methods):

Similar to reading, Pandas offers methods with the prefix `to_` to write DataFrames to various formats:

- **`to_csv()`**: Writes to CSV format.
- **`to_excel()`**: Writes to Excel format.
- **`to_json()`**: Writes to JSON format.
- **`to_parquet()`**: Writes to Parquet format.

### Writing to a CSV File

```python
# Create a DataFrame
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']})

# Write the DataFrame to a CSV file
df.to_csv('data.csv', index=False)  # Don't write the index row
```

### Specifying Delimiter and Excel Sheet Name:

```python
# Write to a CSV with a tab delimiter
df.to_csv('data.txt', sep='\t')

# Write to a specific sheet in an Excel file
df.to_excel('data.xlsx', sheet_name='NewSheet')
```

### Writing JSON with Orient and Parquet Compression:

```python
# Write to JSON with records as rows (orient='records')
df.to_json('data.json', orient='records')

# Write to Parquet with compression
df.to_parquet('data.parquet', compression='snappy')
```

## Additional Considerations:

- **Error Handling:** Consider using `try-except` blocks to handle potential errors during reading or writing (e.g., file not found, permission issues).
- **Data Validation:** Validate the data after reading and before writing to ensure data integrity.
- **Large Datasets:** For very large datasets, consider using formats like Parquet that offer efficient storage and retrieval.

Remember, choosing the appropriate file format depends on your data characteristics, analysis needs, and storage requirements. Pandas provides a versatile set of tools to seamlessly work with various file formats, empowering you to import, analyze, and export data effectively.

### Reading Materials:

https://www.westloop.io/post/power-of-parquet-in-data-analytic-querying

https://www.youtube.com/watch?app=desktop&v=1j8SdS7s_NY