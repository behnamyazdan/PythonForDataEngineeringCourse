# What is Data Types

Data types in programming languages like Python define the type of data that a variable can hold. They specify the nature of the data and the operations that can be performed on it. Each data type has its own set of values and operations associated with it.

### Data types serve several purposes:

1. **Storage Allocation:** Data types determine how much memory space is allocated to store a particular value. For example, integers typically require less memory than floating-point numbers.
2. **Operations:** Different data types support different operations. For example, you can perform arithmetic operations like addition and subtraction on integers and floating-point numbers, but not on strings.
3. **Data Integrity:** Data types help maintain the integrity of data by ensuring that values are interpreted and manipulated correctly. For instance, treating a string as an integer could lead to unexpected behavior or errors in your program.

### Basic data types in Python include:

* **Integers (int):** Whole numbers without any decimal point.
* **Floating-Point Numbers (float):** Real numbers with a decimal point or exponent notation.
* **Strings (str):** Sequences of characters enclosed within single (' ') or double (" ") quotes.
* **Booleans (bool):** Truth values indicating either True or False.

Understanding data types is essential for writing correct and efficient code, as it helps ensure that your program behaves as expected and handles data appropriately. Different programming languages may have their own set of data types, but the concept of data types remains fundamental across all languages.


1. **Integer (`int`)**:
   - Integers represent whole numbers, both positive and negative, without any decimal point.
   - Examples of integers include -10, 0, 42, and 1000.
   - In Python, integers have unlimited precision, allowing you to perform arithmetic operations on very large or very small numbers without losing accuracy.
   - You can create an integer by simply assigning a whole number to a variable, e.g., `x = 42`.

2. **Floating-Point Number (`float`)**:
   - Floats represent real numbers with a decimal point or exponent notation.
   - Examples of floats include -3.14, 0.25, 1.0, and 6.022e23 (scientific notation).
   - Floating-point numbers have finite precision, meaning they can represent a limited range of values with a limited number of significant digits.
   - You can create a float by assigning a number with a decimal point to a variable, e.g., `pi = 3.14`.

3. **String (`str`)**:
   - Strings represent sequences of characters enclosed within single (' ') or double (" ") quotes.
   - Examples of strings include "hello", 'Python', "123", and "Data Science".
   - Strings in Python are immutable, meaning you cannot change the characters of a string after it has been created.
   - You can create a string by enclosing characters within quotes, e.g., `name = "Alice"`.

4. **Boolean (`bool`)**:
   - Booleans represent truth values, indicating either True or False.
   - Booleans are often used in conditional statements and logical operations to control the flow of a program.
   - Examples of boolean values include True and False.
   - You can create a boolean by directly assigning True or False to a variable, e.g., `is_valid = True`.

Here's a simple example demonstrating the use of these basic data types in Python:

```python
# Integer
x = 42

# Float
pi = 3.14

# String
name = "DataEngineering"

# Boolean
is_valid = True

# Printing variables and their types
print("x:", x, "Type:", type(x))
print("pi:", pi, "Type:", type(pi))
print("name:", name, "Type:", type(name))
print("is_valid:", is_valid, "Type:", type(is_valid))
```

Output:
```
x: 42 Type: <class 'int'>
pi: 3.14 Type: <class 'float'>
name: DataEngineering Type: <class 'str'>
is_valid: True Type: <class 'bool'>
```

Understanding these basic data types is essential for writing Python code effectively, as they form the building blocks for more complex data structures and operations in Python programming.

## Type casting (Type conversion):

Type casting, also known as type conversion, is the process of converting one data type into another in programming. In Python, you can perform type casting between basic data types such as integers, floats, strings, and booleans using built-in functions or constructor methods. Let's explore type casting for each data type:

1. **Integer (int) Type Casting**:
   - To convert other data types to integers, you can use the `int()` function.
   - When converting floating-point numbers to integers, the decimal part is truncated.
   - When converting strings to integers, the string must represent a valid integer value, otherwise, a `ValueError` will be raised.

   Example:
   ```python
   x = 10.5
   y = "20"
   z = True
   
   # Convert float to int
   a = int(x)  # Result: 10
   
   # Convert string to int
   b = int(y)  # Result: 20
   
   # Convert boolean to int
   c = int(z)  # Result: 1 (True is converted to 1)
   ```

2. **Floating-Point (float) Type Casting**:
   - To convert other data types to floating-point numbers, you can use the `float()` function.
   - When converting integers to floats, the resulting value will have a decimal point.

   Example:
   ```python
   x = 10
   y = "3.14"
   z = False
   
   # Convert int to float
   a = float(x)  # Result: 10.0
   
   # Convert string to float
   b = float(y)  # Result: 3.14
   
   # Convert boolean to float
   c = float(z)  # Result: 0.0 (False is converted to 0.0)
   ```

3. **String (str) Type Casting**:
   - To convert other data types to strings, you can use the `str()` function.
   - The `str()` function converts any data type into its string representation.

   Example:
   ```python
   x = 10
   y = 3.14
   z = True
   
   # Convert int to str
   a = str(x)  # Result: '10'
   
   # Convert float to str
   b = str(y)  # Result: '3.14'
   
   # Convert boolean to str
   c = str(z)  # Result: 'True'
   ```

4. **Boolean (bool) Type Casting**:
   - To convert other data types to boolean values, you can use the `bool()` function.
   - The `bool()` function returns `True` for non-zero numeric values, non-empty strings, and `True`. It returns `False` for zero numeric values, empty strings, and `False`.

   Example:
   ```python
   x = 10
   y = 0
   z = "hello"
   w = ""
   
   # Convert int to bool
   a = bool(x)  # Result: True
   
   # Convert int to bool
   b = bool(y)  # Result: False
   
   # Convert string to bool
   c = bool(z)  # Result: True
   
   # Convert string to bool
   d = bool(w)  # Result: False
   ```

Type casting allows you to convert data between different types, enabling you to perform operations and manipulations that require specific data types. It's a powerful tool for data manipulation and transformation in Python programming.