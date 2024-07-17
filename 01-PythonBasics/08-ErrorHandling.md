# Error Handling in Python

Error handling is a crucial aspect of software development, allowing programs to manage and respond to unexpected events or conditions gracefully. In Python, error handling is achieved through the use of **exceptions**, which provide a mechanism for interrupting the normal flow of a program when errors or unusual conditions occur. Effective error handling ensures that programs can handle unforeseen situations without crashing, thereby improving robustness and user experience.

Python's approach to error handling has evolved significantly since its inception. Early versions of Python relied on traditional methods of error checking, such as return codes and condition checks. However, as the language matured, a more structured and powerful error-handling mechanism was introduced with the concept of exceptions. This paradigm shift allowed developers to write cleaner and more readable code by separating error-handling logic from the main program flow.

The introduction of exceptions in Python was heavily influenced by languages like C++ and Java, which already had established exception-handling mechanisms. Python adopted and extended these concepts, making error handling more intuitive and integrated into the language's syntax and semantics. Over time, Python's exception-handling capabilities have been refined, with new features and best practices emerging to help developers manage errors more effectively.

### Understanding `try` and `except` Blocks in Python

Error handling in Python revolves around the use of `try` and `except` blocks, which allow developers to manage exceptions and handle errors gracefully. These blocks help ensure that the program can continue to run smoothly even when unexpected issues arise. Let's delve deeper into how `try` and `except` blocks work, their syntax, and some practical examples.

#### The `try` Block

The `try` block is where you write the code that might raise an exception. Python will execute the code inside the `try` block, and if an exception occurs, it will immediately transfer control to the corresponding `except` block. If no exception occurs, the code in the `try` block runs to completion.

Syntax:
```python
try:
    # Code that might raise an exception
    risky_code()
```

Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
```

In this example, the code inside the `try` block attempts to divide 10 by 0, which raises a `ZeroDivisionError`. Because an exception is raised, the code execution jumps to the `except` block.

#### The `except` Block

The `except` block is used to catch and handle exceptions. You can specify the type of exception you want to catch and provide a block of code that runs when that specific exception occurs. If the type of exception matches the one raised in the `try` block, the code in the `except` block executes.

Syntax:
```python
except ExceptionType as e:
    # Code to handle the exception
    handle_exception(e)
```

Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

In this example, the `except` block catches the `ZeroDivisionError` and assigns it to the variable `e`. The error message associated with the exception is then printed.

#### Multiple `except` Blocks

You can have multiple `except` blocks to handle different types of exceptions separately. This is useful when you want to provide different handling mechanisms for different error conditions.

Syntax:
```python
try:
    # Code that might raise an exception
    risky_code()
except FirstExceptionType as e1:
    # Handle the first type of exception
    handle_first_exception(e1)
except SecondExceptionType as e2:
    # Handle the second type of exception
    handle_second_exception(e2)
```

Example:
```python
try:
    result = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
```

In this example, the code attempts to convert the string "abc" to an integer, which raises a `ValueError`. The first `except` block catches the `ValueError` and prints an appropriate message.

#### Using the `else` Clause

The `else` clause can be added to a `try` block to specify a block of code that should be executed if no exceptions are raised in the `try` block. This is useful for code that should only run if everything in the `try` block succeeds.

Syntax:
```python
try:
    # Code that might raise an exception
    risky_code()
except ExceptionType as e:
    # Handle the exception
    handle_exception(e)
else:
    # Code to run if no exception occurs
    no_exception_code()
```

Example:
```python
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"The result is {result}")
```

In this example, the division operation succeeds, so the `else` block runs and prints the result.

#### Using the `finally` Clause

The `finally` clause is optional and contains code that will run no matter what, whether an exception is raised or not. It is typically used for cleanup actions, such as closing files or releasing resources.

Syntax:
```python
try:
    # Code that might raise an exception
    risky_code()
except ExceptionType as e:
    # Handle the exception
    handle_exception(e)
finally:
    # Code to run no matter what
    cleanup_code()
```

Example:
```python
try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
finally:
    file.close()
```

In this example, the `finally` block ensures that the file is closed, whether an exception occurs or not.

#### Raising Exceptions

In Python, you can raise exceptions manually using the `raise` statement. This is useful when you want to enforce certain conditions in your code. When an exception is raised, the normal flow of the program is interrupted, and control is transferred to the `except` block if it exists.

Syntax:
```python
raise ExceptionType("Error message")
```

Example:
```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return age

try:
    age = check_age(15)
except ValueError as e:
    print(e)
```

In this example, the `check_age` function raises a `ValueError` if the age is less than 18. The exception is caught in the `except` block, and the error message is printed.

#### Creating Custom Exceptions

Python allows you to define your own exceptions by creating a new class that inherits from the built-in `Exception` class. Custom exceptions are useful when you want to handle specific error conditions in your application.

Example:
```python
class CustomError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise CustomError("Number must be positive.")
    return number

try:
    number = check_positive(-5)
except CustomError as e:
    print(e)
```

In this example, a custom exception `CustomError` is defined, and it is raised in the `check_positive` function if the number is negative. The custom exception is caught in the `except` block, and the error message is printed.

### Practical Examples

#### Example 1: Handling Multiple Exceptions

```python
try:
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    result = a / b
except ValueError as e:
    print(f"ValueError: Invalid input. {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: Cannot divide by zero. {e}")
else:
    print(f"The result of {a} divided by {b} is {result}")
finally:
    print("Execution complete.")
```

#### Example 2: Raising Custom Exceptions

```python
class CustomError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise CustomError("Number must be positive.")
    return number

try:
    number = check_positive(-5)
except CustomError as e:
    print(e)
```

`try` and `except` blocks are powerful tools for managing errors and exceptions in Python. By using these blocks effectively, you can build robust applications that handle unexpected situations gracefully, ensuring a better user experience and easier debugging. The flexibility of handling different types of exceptions, using `else` and `finally` clauses, raising custom exceptions, and creating your own exceptions allows developers to write clean, maintainable, and reliable code.

### Best Practices for Error Handling

Effective error handling involves not only using the right techniques but also following best practices to ensure that errors are managed in a consistent and maintainable manner:

#### 1- Be Specific with Exceptions:

- Catch specific exceptions rather than using a generic `except` block. This helps in diagnosing issues more accurately.
- Example:
  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError as e:
      print("Error: Division by zero is not allowed.")
  ```

#### 2- Use Finally for Cleanup:

- Always use the `finally` block to release resources, close files, or perform any necessary cleanup actions.
- Example:
  ```python
  try:
      file = open('example.txt', 'r')
      content = file.read()
  except FileNotFoundError as e:
      print("Error: File not found.")
  finally:
      file.close()
  ```

#### 3- Avoid Silent Failures:

- Avoid using empty `except` blocks that can lead to silent failures. Always log or handle the exception appropriately.
- Example:
  ```python
  try:
      result = 10 / 0
  except ZeroDivisionError as e:
      print("Error: Division by zero is not allowed.")
  ```

#### 4- Provide Meaningful Messages:

- When raising or handling exceptions, provide meaningful messages that can help in understanding the nature of the error.
- Example:
  ```python
  def check_positive(number):
      if number < 0:
          raise ValueError("Number must be positive.")
      return number
  ```

#### 5- Log Exceptions:

- Use logging to record exceptions and errors, which can be invaluable for debugging and monitoring applications.
- Example:
  ```python
  import logging
  
  logging.basicConfig(filename='app.log', level=logging.ERROR)
  
  try:
      result = 10 / 0
  except ZeroDivisionError as e:
      logging.error("Error: Division by zero.")
  ```



### Common Exception Types in Python:

| Exception Type        | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| `Exception`           | Base class for all built-in exceptions. It is not meant to be directly inherited by user-defined classes (use `BaseException` for this purpose). |
| `ArithmeticError`     | Base class for all errors that occur for numeric calculations, including overflow, division by zero, and other arithmetic-related errors. |
| `AssertionError`      | Raised when an assert statement fails. This is often used in debugging to ensure certain conditions are met in the code. |
| `AttributeError`      | Raised when an attribute reference or assignment fails. This occurs when referencing an attribute that does not exist on an object. |
| `EOFError`            | Raised when the `input()` function hits an end-of-file condition (EOF) without reading any data. This commonly occurs when input is unexpectedly terminated. |
| `FloatingPointError`  | Raised when a floating-point operation fails. These errors typically involve incorrect floating-point arithmetic operations, such as division by zero in floating-point math. |
| `GeneratorExit`       | Raised when a generator or coroutine is closed. This happens when the `close()` method of a generator is called or when a generator exits. |
| `ImportError`         | Raised when an import statement fails to find the module definition or when a `from ... import` fails to find a name that is to be imported. |
| `IndexError`          | Raised when a sequence subscript is out of range. This occurs when trying to access an index that is not present in a list, string, or other sequence. |
| `KeyError`            | Raised when a dictionary key is not found. This occurs when trying to access a dictionary with a key that doesn't exist in the dictionary. |
| `KeyboardInterrupt`   | Raised when the user hits the interrupt key (Ctrl+C or Delete). This is commonly used to gracefully handle user-initiated program interruptions. |
| `MemoryError`         | Raised when an operation runs out of memory. This happens when the program tries to use more memory than what is available. |
| `NameError`           | Raised when a local or global name is not found. This occurs when referencing a variable or function name that has not been defined. |
| `NotImplementedError` | Raised by abstract methods that need to be implemented in derived classes. This is used to signal that the derived class should implement this method. |
| `OSError`             | Raised when a system function returns a system-related error, including I/O failures such as "file not found" or "disk full". |
| `OverflowError`       | Raised when the result of an arithmetic operation is too large to be expressed within the range of the numeric type. |
| `RecursionError`      | Raised when the maximum recursion depth is exceeded. This occurs when a function calls itself too many times without an exit condition. |
| `ReferenceError`      | Raised when a weak reference proxy is used to access a garbage collected referent. This typically involves advanced memory management techniques. |
| `RuntimeError`        | Raised when an error does not fall under any other category. This is a general-purpose error for conditions that do not meet specific error type criteria. |
| `StopIteration`       | Raised by the `next()` function to signal that there are no further items produced by an iterator. This is used to end iteration over a collection. |
| `SyntaxError`         | Raised by the parser when a syntax error is encountered. This occurs when the code is not syntactically correct according to Python language rules. |
| `IndentationError`    | Raised when there is incorrect indentation. This is a specific subclass of `SyntaxError` related to incorrect use of indentation in Python code. |
| `TabError`            | Raised when indentation consists of inconsistent tabs and spaces. This is a specific subclass of `IndentationError` related to mixing tabs and spaces in indentation. |
| `SystemError`         | Raised when the interpreter detects an internal error, but the situation does not meet criteria for `MemoryError`, `OSError`, or other standard exceptions. |
| `TypeError`           | Raised when an operation or function is applied to an object of inappropriate type. This occurs when using incorrect types, like adding a string and an integer. |
| `UnboundLocalError`   | Raised when a local variable is referenced before assignment. This is a specific subclass of `NameError` for local variable issues. |
| `ValueError`          | Raised when a function gets an argument of correct type but improper value. This occurs when arguments are of correct type but fail in value-specific validation. |
| `ZeroDivisionError`   | Raised when division or modulo by zero takes place for all numeric types. This occurs when attempting to divide a number by zero, which is mathematically undefined. |

---

### Examples:

#### `AttributeError`

**Description:** Raised when an attribute reference or assignment fails.

```python
class MyClass:
    def __init__(self):
        self.name = "ChatGPT"

obj = MyClass()
print(obj.age)  # This will raise an AttributeError because 'age' is not an attribute of MyClass
```
**Output:**

```
AttributeError: 'MyClass' object has no attribute 'age'
```

#### `IndexError`

**Description:** Raised when a sequence subscript is out of range.

```python
my_list = [1, 2, 3]
print(my_list[3])  # This will raise an IndexError because there is no element at index 3
```
**Output:**
```
IndexError: list index out of range
```

#### `KeyError`

**Description:** Raised when a dictionary key is not found.

```python
my_dict = {"name": "ChatGPT"}
print(my_dict["age"])  # This will raise a KeyError because 'age' is not a key in the dictionary
```
**Output:**

```
KeyError: 'age'
```

#### `NameError`

**Description:** Raised when a local or global name is not found.

```python
print(age)  # This will raise a NameError because 'age' has not been defined
```
**Output:**
```
NameError: name 'age' is not defined
```

#### `TypeError`

**Description:** Raised when an operation or function is applied to an object of inappropriate type.

```python
result = '2' + 2  # This will raise a TypeError because you cannot add a string and an integer
```
**Output:**

```
TypeError: can only concatenate str (not "int") to str
```

#### `ValueError`

**Description:** Raised when a function gets an argument of correct type but improper value.

```python
number = int("abc")  # This will raise a ValueError because 'abc' cannot be converted to an integer
```
**Output:**

```
ValueError: invalid literal for int() with base 10: 'abc'
```

#### `ZeroDivisionError`

**Description:** Raised when division or modulo by zero takes place for all numeric types.

```python
result = 10 / 0  # This will raise a ZeroDivisionError because division by zero is not allowed
```
**Output:**
```
ZeroDivisionError: division by zero
```

#### `FileNotFoundError`

**Description:** Raised when a file or directory is requested but doesn't exist.

```python
with open('non_existent_file.txt', 'r') as file:
    content = file.read()  # This will raise a FileNotFoundError because the file does not exist
```
**Output:**

```
FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
```

#### `ImportError`

**Description:** Raised when an import statement fails to find the module definition or when a `from ... import` fails to find a name that is to be imported.

```python
import non_existent_module  # This will raise an ImportError because the module does not exist
```
**Output:**
```
ImportError: No module named 'non_existent_module'
```

#### `ModuleNotFoundError`

**Description:** A subclass of `ImportError` that is raised when a module cannot be found.

```python
import non_existent_module  # This will raise a ModuleNotFoundError because the module does not exist
```
**Output:**

```
ModuleNotFoundError: No module named 'non_existent_module'
```

These examples demonstrate common exceptions and how they occur in Python code.

Error handling in Python is a powerful feature that allows developers to build robust and reliable applications. By understanding and implementing proper error-handling techniques, developers can ensure that their programs can handle unexpected situations gracefully, provide meaningful feedback to users, and maintain overall stability.



## Optional Reading Topics



### Exception Object and Its Methods in Python

When an error occurs in Python, an exception is raised. This exception is represented by an exception object. Exception objects carry information about the error, which can be useful for debugging and handling errors gracefully. Let's explore the features and methods of the `Exception` object in Python.

#### Basic Structure of an Exception Object

All built-in, non-system-exiting exceptions in Python are derived from the `BaseException` class. The `Exception` class is the base class for all built-in exceptions except for `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit`.

#### Key Attributes of Exception Objects

1. **args**: This is a tuple of arguments given to the exception constructor. It can be used to get information about the exception.
2. **__str__()**: This method returns the string representation of the exception.
3. **__repr__()**: This method returns a string containing a printable representation of the object, which can be used for debugging.

#### Common Methods

1. **__init__(self, *args)**: Initializes the exception instance.
2. **__str__(self)**: Returns a string representation of the exception. This is called by the `str()` built-in function and the `print` statement to compute the "informal" string representation of an object.
3. **__repr__(self)**: Returns a string representation of the exception object. This is useful for debugging.

#### Example Usage

Let's look at an example to understand how these attributes and methods work.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception occurred: {e}")
    print(f"Exception args: {e.args}")
    print(f"Exception string representation: {str(e)}")
    print(f"Exception repr representation: {repr(e)}")
```

**Explanation:**

1. **Exception occurred**: This prints the exception message using the default string representation provided by the `__str__()` method of the `Exception` class.
2. **Exception args**: The `args` attribute contains a tuple of arguments that were passed to the exception constructor. For a `ZeroDivisionError`, it contains the message 'division by zero'.
3. **Exception string representation**: The `str(e)` function calls the `__str__()` method of the exception object, which returns a human-readable string representation of the exception.
4. **Exception repr representation**: The `repr(e)` function calls the `__repr__()` method, which returns a detailed string representation of the exception object, useful for debugging.

**Output:**

```
Exception occurred: division by zero
Exception args: ('division by zero',)
Exception string representation: division by zero
Exception repr representation: ZeroDivisionError('division by zero')
```

#### Custom Exception Example

You can create your own custom exceptions by inheriting from the `Exception` class and overriding its methods.

```python
class MyCustomError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f"{self.args[0]} (Error Code: {self.error_code})"

try:
    raise MyCustomError("Something went wrong", 404)
except MyCustomError as e:
    print(f"Custom Exception occurred: {e}")
    print(f"Custom Exception args: {e.args}")
    print(f"Custom Exception error code: {e.error_code}")
```

**Explanation:**

1. **Custom Exception occurred**: This prints the custom string representation of the `MyCustomError` exception.
2. **Custom Exception args**: The `args` attribute contains the message 'Something went wrong'.
3. **Custom Exception error code**: The custom `error_code` attribute is printed, showing the specific error code associated with the exception.

**Output:**

```
Custom Exception occurred: Something went wrong (Error Code: 404)
Custom Exception args: ('Something went wrong',)
Custom Exception error code: 404
```

### Summary

- The `Exception` class is the base class for all built-in exceptions in Python.
- Common methods include `__init__()`, `__str__()`, and `__repr__()`.
- The `args` attribute contains the arguments passed to the exception.
- Custom exceptions can be created by inheriting from the `Exception` class and overriding its methods.
- Exception objects provide useful information for debugging and handling errors gracefully.