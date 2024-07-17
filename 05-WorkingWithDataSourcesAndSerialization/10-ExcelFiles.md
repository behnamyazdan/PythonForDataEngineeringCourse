# Excel Files

Excel files are a staple in both personal and professional environments for organizing, analyzing, and storing data. With their user-friendly interface and robust functionality, Excel files are widely used across various industries, from finance and marketing to education and research. These files can handle a variety of data types, including text, numbers, formulas, and charts, making them an indispensable tool for data analysis and reporting.

Excel files come in two primary formats: the older XLS format and the newer XLSX format. Each format has its own use cases, limitations, and advantages. Understanding these formats, as well as how to read from and write to Excel files using Python, can greatly enhance your ability to manage and manipulate data programmatically.

In this section, we will explore the differences between XLS and XLSX formats, discuss their use cases and limitations, and delve into practical methods for reading from and writing to Excel files using popular Python libraries such as Pandas and openpyxl.

## Overview of Excel File Formats

### XLS vs. XLSX

- **XLS (Excel 97-2003 Workbook)**:
  
  - **Format**: Binary Interchange File Format (BIFF)
  - **File Extension**: .xls
  - **Compatibility**: Compatible with older versions of Excel (Excel 97 to Excel 2003)
  - **Features**: Limited to 65,536 rows and 256 columns per sheet
  - **Use Cases**: Suitable for compatibility with older software and smaller datasets

- **XLSX (Excel 2007 and later Workbook)**:
  
  - **Format**: Office Open XML (OOXML)
  - **File Extension**: .xlsx
  - **Compatibility**: Compatible with Excel 2007 and later versions
  - **Features**: Supports up to 1,048,576 rows and 16,384 columns per sheet, larger file sizes, and improved data integrity and security
  - **Use Cases**: Ideal for large datasets, advanced data analysis, and modern Excel features

### Use Cases and Limitations

- **XLS**:
  
  - **Advantages**: Better compatibility with older systems and software
  - **Limitations**: Limited row and column capacity, larger file sizes compared to XLSX, and lack of support for newer Excel features

- **XLSX**:
  
  - **Advantages**: Greater capacity for rows and columns, improved performance and file sizes, support for modern Excel features like conditional formatting, pivot tables, and data validation
  - **Limitations**: Requires newer versions of Excel, potential compatibility issues with legacy systems

## Reading from Excel Files

### Handling Single Sheet

- **Pandas**:
  
  **Advantages**: High-level data manipulation capabilities, easy-to-use API, supports reading multiple file formats including Excel
  
  ```python
  import pandas as pd
  
  # Read Excel file into DataFrame
  df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
  print(df.head())
  ```

- **openpyxl**:
  
  **Advantages**: Low-level control over Excel files, supports reading and writing .xlsx files, ability to manipulate Excel-specific features
  
  ```python
  from openpyxl import load_workbook
  
  # Load Excel workbook and select sheet
  wb = load_workbook('data.xlsx')
  sheet = wb['Sheet1']
  
  # Read data from sheet
  for row in sheet.iter_rows(values_only=True):
      print(row)
  ```

### Handling Multiple Sheets

- **Pandas**:
  
  ```python
  # Read multiple sheets into a dictionary of DataFrames
  dfs = pd.read_excel('data.xlsx', sheet_name=None)
  for sheet_name, df in dfs.items():
      print(f'Sheet name: {sheet_name}')
      print(df.head())
  ```

- **openpyxl**:
  
  ```python
  # Load workbook and iterate over all sheets
  wb = load_workbook('data.xlsx')
  for sheet_name in wb.sheetnames:
      sheet = wb[sheet_name]
      print(f'Sheet name: {sheet_name}')
      for row in sheet.iter_rows(values_only=True):
          print(row)
  ```

## Writing to Excel Files

### Creating and Formatting Sheets

- **Pandas**:
  
  ```python
  # Write DataFrame to Excel with formatting
  df = pd.DataFrame(data={'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
  with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
      df.to_excel(writer, sheet_name='Sheet1', index=False)
      # Add formatting
      workbook = writer.book
      worksheet = writer.sheets['Sheet1']
      header_format = workbook.add_format({'bold': True, 'text_wrap': True, 'valign': 'top'})
      for col_num, value in enumerate(df.columns.values):
          worksheet.write(0, col_num, value, header_format)
  ```

- **openpyxl**:
  
  ```python
  from openpyxl import Workbook
  from openpyxl.styles import Font
  
  # Create workbook and sheet
  wb = Workbook()
  sheet = wb.active
  sheet.title = 'Sheet1'
  
  # Write data with formatting
  data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
  for col_num, (col_name, col_data) in enumerate(data.items(), start=1):
      cell = sheet.cell(row=1, column=col_num, value=col_name)
      cell.font = Font(bold=True)
      for row_num, value in enumerate(col_data, start=2):
          sheet.cell(row=row_num, column=col_num, value=value)
  
  wb.save('output.xlsx')
  ```

### Exporting Data to Excel

- **Pandas**:
  
  ```python
  # Export DataFrame to Excel
  df = pd.DataFrame(data={'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
  df.to_excel('exported_data.xlsx', sheet_name='Sheet1', index=False)
  ```

- **openpyxl**:
  
  ```python
  from openpyxl import Workbook
  
  # Create workbook and sheet
  wb = Workbook()
  sheet = wb.active
  sheet.title = 'Sheet1'
  
  # Write data to sheet
  data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
  for col_num, (col_name, col_data) in enumerate(data.items(), start=1):
      sheet.cell(row=1, column=col_num, value=col_name)
      for row_num, value in enumerate(col_data, start=2):
          sheet.cell(row=row_num, column=col_num, value=value)
  
  wb.save('exported_data.xlsx')
  ```

By understanding the differences between XLS and XLSX formats, and by utilizing libraries such as Pandas and openpyxl, you can effectively read from and write to Excel files in Python. Whether you're handling simple datasets or complex data manipulations, these tools and techniques will help streamline your workflow and enhance your data processing capabilities.



---

More Information:

[A Guide to Excel Spreadsheets in Python With openpyxl – Real Python](https://realpython.com/openpyxl-excel-spreadsheets-python/)


