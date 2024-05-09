# `if` Statement in Python:

The if statement is a fundamental control flow statement in Python used to execute a block of code conditionally based on whether a specified condition evaluates to true or false. It allows you to control the flow of execution in your program by selectively executing code blocks based on certain conditions.

### Syntax:

```python
if condition:
    # Code block to execute if condition is True
    statement1
    statement2
    ...
elif condition:
    # Code block to execute if condition is True
    statement3
    statement4
    ...
else:
    # Code block to execute if all conditions are False
    statement5
    statement6
    ...
```

**Explanation:**

1. **Condition**:
   - The if statement begins with the keyword `if`, followed by a condition that evaluates to either True or False.
   - The condition can be any expression that returns a Boolean value (True or False).
   - If the condition is True, the code block associated with the if statement is executed. If the condition is False, the code block is skipped.

2. **Code Block**:
   - The code block associated with the if statement is indented under the if statement.
   - It consists of one or more statements that are executed if the condition is True.
   - Indentation is crucial in Python, as it defines the scope of the code block.

3. **elif (else if)**:
   - You can use the `elif` keyword to add additional conditions to the if statement.
   - `elif` allows you to check multiple conditions sequentially, executing the code block associated with the first True condition encountered.
   - You can have multiple `elif` clauses to handle different cases.

4. **else**:
   - The `else` keyword is optional and can be used to define a default code block that executes when all previous conditions are False.
   - It is used as a catch-all for cases not covered by the preceding if or elif conditions.
   - You can only have one `else` clause, and it must be placed at the end of the if statement.

**Example:**

```python
# Real-world scenario: Determining eligibility for a discount based on age
age = 25

if age < 18:
    print("You are not eligible for a discount.")
elif age >= 18 and age <= 30:
    print("You qualify for a 10% discount.")
else:
    print("You qualify for a 20% discount.")
```

**Explanation of Example:**
- In this example, the program checks the `age` variable to determine eligibility for a discount.
- If the age is less than 18, the program prints a message stating that the person is not eligible for a discount.
- If the age is between 18 and 30 (inclusive), the program prints a message indicating eligibility for a 10% discount.
- If the age is greater than 30, the program prints a message indicating eligibility for a 20% discount.

This example demonstrates how the if statement allows you to make decisions and control the flow of execution in your Python programs based on different conditions, making your code dynamic and adaptable to various scenarios.

### Conditions:

Conditions in Python are expressions that evaluate to either `True` or `False`. These expressions are used to control the flow of a program by determining which code blocks are executed based on certain conditions. Python evaluates conditions using comparison operators, logical operators, and other constructs.

* **Comparison Operators:**

   - Comparison operators are used to compare values and return `True` or `False` based on the comparison result.
   - Common comparison operators include `==` (equal), `!=` (not equal), `<` (less than), `>` (greater than), `<=` (less than or equal to), and `>=` (greater than or equal to).
   - Example:
     ```python
     x = 10
     y = 20
     print(x < y)  # Output: True
     ```

* **Logical Operators:**

   - Logical operators are used to combine multiple conditions and perform logical operations (`and`, `or`, `not`).
   - `and` returns `True` if both conditions are true.
   - `or` returns `True` if at least one condition is true.
   - `not` returns the opposite boolean value of the condition.
   - Example:
     ```python
     age = 25
     is_student = False
     if age >= 18 and not is_student:
         print("You are eligible to vote.")
     ```

* **Using `bool()` Function in Conditions:**

   - When a value is used in a condition, Python internally calls the `bool()` function to determine its truthiness.
   - The `bool()` function returns `True` for values that are considered "truthy" and `False` for values that are considered "falsy".
   - Example:
     ```python
     value = 10
     if bool(value):
         print("Value is truthy")
     ```

* **Truthiness and Falseness:**
   - In Python, non-boolean values have truthy or falsy values when evaluated in a boolean context.
   - Values that are considered falsy include `False`, `None`, numeric zero (`0`), empty sequences (`[]`, `()`, `{}`), and empty strings (`''`).
   - All other values are considered truthy.
   - Example:
     ```python
     if bool(0):  # Falsy
         print("Falsy")
     if bool(10):  # Truthy
         print("Truthy")
     ```
     
     | Type                      | Value        | Truthiness |
     | ------------------------- |--------------| ---------- |
     | Boolean                   | `False`      | False      |
     | None                      | `None`       | False      |
     | Numeric                   | `0`          | False      |
     | Empty List                | `[]`         | False      |
     | Empty Tuple and Empty Set | `()`         | False      |
     | Empty Dictionary          | `{}`         | False      |
     | String                    | `''`, `""`, `""""""` | False      |


* **Type Casting in Conditions:**
   - Python's conditional expressions perform implicit type casting to convert values to boolean before evaluating conditions.
   - For example, when using `==` operator, Python will first convert both operands to a common type before performing the comparison.
   - Example:
     ```python
     value = "10"
     if value == 10:  # Implicit type casting
         print("Equal")
     ```

* **Type Actings in Conditions:**
   - Sometimes, Python may perform unexpected type conversions, known as "type actings", which can lead to unexpected behavior.
   - It's important to be mindful of the data types being compared and to explicitly convert values when necessary to avoid unintended consequences.
   - Example:
     ```python
     value = "10"
     if int(value) == 10:  # Explicit type conversion
         print("Equal")
     ```

* **Short-circuit Evaluation:**

   - Python uses short-circuit evaluation when evaluating logical expressions.

   - In a compound `and` expression, if the first operand is `False`, the second operand is not evaluated because the entire expression will be `False` regardless of the second operand's value.

   - Similarly, in a compound `or` expression, if the first operand is `True`, the second operand is not evaluated because the entire expression will be `True` regardless of the second operand's value.

   - Example:

     ```python
     x = 5
     y = 10
     if x < y < 100:  # Short-circuit evaluation
         print("Both conditions are true.")
     ```

Understanding how Python handles type casting and evaluates conditions using the `bool()` function is crucial for writing reliable and predictable code. By being aware of truthiness, falsiness, and type casting behaviors, you can write more robust conditional expressions and avoid common pitfalls.

### Nested if:

Nested if statements are if statements that are placed inside another if statement's code block. They allow for more complex conditional logic by allowing you to check multiple conditions within the same code block. Each nested if statement adds another level of conditionality, allowing you to create branching paths in your code based on various conditions. Let's explore nested if statements with an example:

**Example: Determining Discount Eligibility with Nested If Statements**

```python
# Real-world scenario: Determining eligibility for a discount based on age and membership status

age = 25
is_member = True

if age >= 18:
    if is_member:
        print("You qualify for a discount.")
        if age >= 18 and age <= 30:
            print("You qualify for a 10% discount.")
        else:
            print("You qualify for a 5% discount.")
    else:
        print("Join our membership program to get a discount.")
else:
    print("You are not eligible for a discount.")
```

**Explanation:**

- In this example, the program first checks if the age is greater than or equal to 18.
- If the age condition is true, the program enters the outer if block and checks if the person is a member (`is_member` is True).
  - If the person is a member, the program enters the inner if block and checks additional conditions based on age to determine the discount eligibility.
  - If the age is between 18 and 30, the person qualifies for a 10% discount; otherwise, they qualify for a 5% discount.
  - If the person is not a member, the program prompts them to join the membership program to get a discount.
- If the age condition is false (i.e., age is less than 18), the program prints a message indicating that the person is not eligible for a discount.

**Key Points:**
- Nested if statements allow for hierarchical conditional logic, enabling you to handle more complex scenarios.
- Each nested if statement introduces another level of indentation, making the code structure more hierarchical.
- Be mindful of proper indentation to maintain code readability and clarity.
- Nested if statements can be nested to multiple levels, but excessive nesting can make the code difficult to understand. Use them judiciously based on the complexity of your conditions.

**Example: Categorizing Student Grades**

```python
# Real-world scenario: Categorizing student performance based on grades

# Input grade from the user
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Your grade is A.")
    if grade >= 95:
        print("Excellent performance!")
    else:
        print("Good job!")
elif grade >= 80:
    print("Your grade is B.")
    if grade >= 85:
        print("Keep up the good work!")
    else:
        print("You're doing well!")
else:
    print("Your grade is below B.")
    if grade >= 70:
        print("You can improve!")
    else:
        print("You might need to work harder.")
```

**Explanation:**

- In this example, the program categorizes a student's performance based on their grade.
- The outer if, elif, and else statements categorize the grade into three categories: A, B, or below B.
- Within each category, there are nested if and else statements that provide additional feedback based on the specific grade range.
- For example, if a student's grade is A, the program checks if it's an excellent performance (grade >= 95) or a good job (grade < 95 and grade >= 90).
- Similarly, for grade B, it checks if the student should keep up the good work (grade >= 85) or is doing well (grade < 85 and grade >= 80).
- For grades below B, it provides suggestions for improvement based on the specific grade range.
- In this example, the `input()` method is used to prompt the user to input their grade.
- The `int()` function is used to convert the input string into an integer so that it can be compared with numeric values.
- The rest of the code remains the same as the previous example, categorizing the student's performance based on the input grade and providing feedback accordingly.

**Key Points:**
- Nested if statements allow for more detailed condition checking and provide additional levels of feedback based on different conditions.
- Each nested if statement can have its own if, elif, and else clauses to handle different scenarios within the parent condition.
- Proper indentation is crucial to maintain the hierarchy and readability of nested if statements.
- The `input()` method allows the user to interact with the program by providing input from the keyboard.
- It's important to convert the input string into the appropriate data type (e.g., integer) before performing comparisons or calculations.
- With user input, the program becomes more interactive and adaptable to different scenarios based on user input.



### Ternary Operator:

The **ternary operator** in Python works like a shortcut for writing conditional statements. It consists of three parts: the condition, the expression to be executed if the condition is true, and the expression to be executed if the condition is false. If the condition is true, the value of the expression after the `if` keyword is assigned to a variable. If the condition is false, the value of the expression after the `else` keyword is assigned to the variable.result = expression_if_true if condition else expression_if_false

Here's how it operates:

- The **condition** is assessed initially.
- If the condition is true, the expression just preceding the `if` keyword is evaluated and assigned to the variable `result`.
- If the condition is false, the expression following the `else` keyword is evaluated and assigned to `result`.

For example:

```python
x = 10
y = "even" if x % 2 == 0 else "odd"
print(y)  # Output: even
```

In this example, if `x` is divisible by 2 (i.e., `x` is even), then `"even"` is assigned to `y`. Otherwise, `"odd"` is assigned to `y`.



---

## Interact with user:
The `input()` method in Python is used to interactively prompt the user for input from the keyboard. It displays a prompt message (if provided) and waits for the user to enter some text followed by pressing the Enter key. The input entered by the user is returned as a string.

Here's the syntax of the `input()` method:
```python
input(prompt)
```
- `prompt` (optional): A string that specifies the message to be displayed to the user as a prompt. If not provided, the input is taken without any prompt.

Example:
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

In this example, the `input()` method prompts the user to enter their name. The entered value is stored in the `name` variable as a string.

However, if you want to perform numerical operations or comparisons with the input, you'll need to convert the input string to the appropriate numeric type (e.g., integer, float). This is where type casting comes into play.

Type casting is the process of converting a value from one data type to another. In Python, you can use built-in functions like `int()`, `float()`, and `str()` for type casting.

To convert a string obtained from `input()` to an integer, you can use the `int()` function. Here's how you can do it:
```python
age_str = input("Enter your age: ")  # Input is received as a string
age = int(age_str)  # Convert the input string to an integer
```

Now, the variable `age` contains the user's age as an integer, allowing you to perform numeric operations or comparisons with it.

Similarly, you can use `float()` to convert a string to a floating-point number and `str()` to convert other data types to strings.

Type casting is essential for handling user input effectively, especially when you need to work with different data types in your Python programs.

---

## None value `(NoneType)`

In Python, a non-value, or absence of a value, is typically represented by the `None` object. `None` is a special constant in Python that represents the absence of a value or a null value. It is commonly used to signify that a variable or an expression has not been assigned a value.

**1. Representation:**
   - `None` is a built-in constant in Python, and it is not the same as the boolean value `False` or the integer `0`.
   - It is its own data type, often referred to as the "NoneType".
   - Example:
     ```python
     x = None
     ```

**2. Use Cases:**
   - `None` is commonly used to initialize variables or as a default return value for functions that may not always return a meaningful result.
     - It can be used as a placeholder to indicate missing or incomplete data. 
     
     Example:
     
       ```python
       def find_element(lst, target):
           for item in lst:
               if item == target:
                   return item
           return None  # Return None if target is not found
       ```

**3. Checking for `None`:**
   - You can check if a variable or expression is `None` using identity comparison (`is` operator) or truthiness/falsiness.
      Example:

     ```python
     if x is None:
         print("x has not been assigned a value")
     ```

**4. Default Argument Values:**
   - `None` is often used as a default value for function arguments when the caller does not provide a value.
      Example:
     ```python
     def greet(name=None):
         if name is None:
             print("Hello, anonymous!")
         else:
             print("Hello, " + name + "!")
     ```



#### Optional Reading

In Python, `None` is a singleton object, meaning that there is only one instance of it created during the interpreter's startup. When you assign `None` to a variable, you are essentially binding that variable to the existing `None` object in memory. Here's what happens:

**1. Memory Allocation:**
   - During the Python interpreter's initialization, a single `None` object is created and stored in memory.
   - This object is typically located in a special area of memory reserved for storing constant values.

**2. Assignment to a Variable:**
   - When you assign `None` to a variable, the variable is bound to the existing `None` object in memory.
   - No new memory allocation is performed for the variable itself; instead, it simply refers to the pre-existing `None` object.

**3. Reference Counting:**
   - The reference count of the `None` object is incremented each time a variable is assigned to it.
   - If the variable is reassigned or goes out of scope, the reference count is decremented accordingly.

**4. Garbage Collection:**
   - Python's garbage collector automatically reclaims memory allocated to objects that are no longer referenced.
   - Since `None` is a singleton object and always present in memory, it is never garbage collected as long as the Python interpreter is running.

**Example:**
```python
x = None  # Variable x is assigned to the existing None object in memory
y = None  # Another variable y is assigned to the same None object

# Both x and y now refer to the same None object
```

**Memory Diagram:**
```
    +------------------+
x ->|    None Object   |<- y
    +------------------+
```

`None` is a special singleton object in Python that represents the absence of a value. When assigned to a variable, that variable simply refers to the existing `None` object in memory. This efficient memory management helps keep Python code lightweight and responsive.