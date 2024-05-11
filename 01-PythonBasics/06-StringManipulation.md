# String Manipulation in Python

## Introduction:

String manipulation is a fundamental aspect of programming, and Python offers powerful tools and techniques for working with strings. In Python, a string is a sequence of characters enclosed within either single quotes (' ') or double quotes (" "). Strings are immutable, meaning they cannot be modified in place. However, Python provides numerous built-in methods and operators for manipulating strings efficiently.

## String Creation and Concatenation:

Strings in Python can be created using either single quotes or double quotes. For example:
```python
my_string = 'Hello, World!'
```
Strings can be concatenated using the `+` operator:
```python
greeting = 'Hello'
name = 'Alice'
message = greeting + ', ' + name + '!'
```

## String Indexing and Slicing:

Individual characters within a string can be accessed using indexing. Python uses zero-based indexing, where the first character has an index of 0:
```python
my_string = 'Hello'
first_char = my_string[0]  # 'H'
```
Slicing allows you to extract substrings from a string:
```python
substring = my_string[1:3]  # 'el'
```

## String Methods:

Python provides a wide range of built-in methods for manipulating strings:
- `len()`: Returns the length of a string.
- `upper()`, `lower()`: Converts a string to uppercase or lowercase.
- `strip()`, `lstrip()`, `rstrip()`: Removes leading and trailing whitespace.
- `split()`, `join()`: Splits a string into a list of substrings based on a delimiter, or joins a list of strings into a single string.
- `replace()`: Replaces occurrences of a substring with another substring.
- `find()`, `index()`: Searches for the occurrence of a substring within a string and returns its index.
- `count()`: Counts the occurrences of a substring within a string.
- `startswith()`, `endswith()`: Checks if a string starts or ends with a specific substring.



| Method               | Description                                                  | Example                                                      |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `capitalize()`       | Returns a copy of the string with the first character capitalized. | `'hello'.capitalize()` returns `'Hello'`                     |
| `upper()`            | Returns a copy of the string converted to uppercase.         | `'hello'.upper()` returns `'HELLO'`                          |
| `lower()`            | Returns a copy of the string converted to lowercase.         | `'HELLO'.lower()` returns `'hello'`                          |
| `title()`            | Returns a copy of the string with the first character of each word capitalized. | `'hello world'.title()` returns `'Hello World'`              |
| `swapcase()`         | Returns a copy of the string with uppercase characters converted to lowercase and vice versa. | `'Hello World'.swapcase()` returns `'hELLO wORLD'`           |
| `strip()`            | Returns a copy of the string with leading and trailing whitespace removed. | `'   hello   '.strip()` returns `'hello'`                    |
| `lstrip()`           | Returns a copy of the string with leading whitespace removed. | `'   hello   '.lstrip()` returns `'hello   '`                |
| `rstrip()`           | Returns a copy of the string with trailing whitespace removed. | `'   hello   '.rstrip()` returns `'   hello'`                |
| `startswith(prefix)` | Returns `True` if the string starts with the specified prefix; otherwise, returns `False`. | `'hello world'.startswith('hello')` returns `True`           |
| `endswith(suffix)`   | Returns `True` if the string ends with the specified suffix; otherwise, returns `False`. | `'hello world'.endswith('world')` returns `True`             |
| `replace(old, new)`  | Returns a copy of the string with all occurrences of substring `old` replaced by `new`. | `'hello world'.replace('world', 'python')` returns `'hello python'` |
| `split(sep)`         | Splits the string into a list of substrings using the specified separator `sep`. If `sep` is not specified, splits on whitespace. | `'hello world'.split()` returns `['hello', 'world']`         |
| `join(iterable)`     | Concatenates elements of an iterable using the string as a separator. | `' '.join(['hello', 'world'])` returns `'hello world'`       |
| `find(sub)`          | Searches for the first occurrence of substring `sub` and returns its index. Returns `-1` if `sub` is not found. | `'hello world'.find('world')` returns `6`                    |
| `index(sub)`         | Searches for the first occurrence of substring `sub` and returns its index. Raises a `ValueError` if `sub` is not found. | `'hello world'.index('world')` returns `6`                   |
| `count(sub)`         | Counts the number of occurrences of substring `sub` in the string. | `'hello world'.count('o')` returns `2`                       |

**More information:**
https://docs.python.org/3/library/stdtypes.html#string-methods

## String Formatting:

Python supports various methods for formatting strings:
- Using the `%` operator: Allows for string interpolation using format specifiers.

- Using the `format()` method: Provides more flexibility and readability for string formatting.

- Using f-strings (formatted string literals): Introduced in Python 3.6, f-strings offer a concise and readable way to format strings.

  String formatting in Python refers to the process of creating formatted strings by inserting values into placeholder fields within a string. Python offers several methods for string formatting, each with its own syntax and capabilities.

  #### 1. Using `%` Operator:

  The `%` operator is a legacy method for string formatting and allows for simple interpolation of values into a string using format specifiers. The general syntax is `%[flags][width][.precision]specifier`.

  - `%s`: String
  - `%d` or `%i`: Integer
  - `%f`: Float

  Example:
  ```python
  name = 'Alice'
  age = 30
  height = 1.75
  formatted_string = 'Name: %s, Age: %d, Height: %.2f meters' % (name, age, height)
  ```

  #### Using `str.format()` Method:

  The `str.format()` method provides a more flexible and readable way to format strings. It allows for positional and keyword arguments, and supports various format specifiers.

  Example:
  ```python
  name = 'Alice'
  age = 30
  height = 1.75
  formatted_string = 'Name: {}, Age: {}, Height: {:.2f} meters'.format(name, age, height)
  ```

  #### Using f-strings (Formatted String Literals):

  Introduced in Python 3.6, f-strings offer a concise and intuitive way to format strings. They allow for embedding Python expressions directly within string literals. f-strings are generally recommended for their readability and efficiency, especially in Python 3.6 and later versions.

  Example:
  ```python
  name = 'Alice'
  age = 30
  height = 1.75
  formatted_string = f'Name: {name}, Age: {age}, Height: {height:.2f} meters'
  ```

  #### Using Template Strings:

  Template strings provide a simple and safe way for string interpolation, especially when dealing with user-supplied data. They use the `$` character for placeholder substitution.

  Example:
  ```python
  from string import Template
  name = 'Alice'
  age = 30
  height = 1.75
  template = Template('Name: $name, Age: $age, Height: $height meters')
  formatted_string = template.substitute(name=name, age=age, height=height)
  ```

  ### Using Concatenation:

  Although less common, string concatenation can also be used for basic string formatting by combining strings and variables.

  Example:
  ```python
  name = 'Alice'
  age = 30
  height = 1.75
  formatted_string = 'Name: ' + name + ', Age: ' + str(age) + ', Height: ' + format(height, '.2f') + ' meters'
  ```


### String Formatting Examples:
  ##### Example 1: Using `%` Operator:

  ```python
  # Example using % operator for string formatting
  name = 'Alice'
  age = 30
  height = 1.75
  formatted_string = 'Name: %s, Age: %d, Height: %.2f meters' % (name, age, height)
  print(formatted_string)
  ```

  **Explanation:**

  - In this example, we define variables `name`, `age`, and `height`.
  - The `%` operator is used to format the string `formatted_string` with placeholders `%s`, `%d`, and `%.2f` for string, integer, and float values, respectively.
  - The values are inserted into the placeholders using the `%` operator followed by a tuple `(name, age, height)` containing the variables to be substituted.
  - The resulting formatted string is printed.

  ##### Example 2: Using `str.format()` Method:

  ```python
  # Example using str.format() method for string formatting
  name = 'Alice'
  age = 30
  height = 1.75
  formatted_string = 'Name: {}, Age: {}, Height: {:.2f} meters'.format(name, age, height)
  print(formatted_string)
  ```

  **Explanation:**

  - In this example, we define variables `name`, `age`, and `height`.
  - The `format()` method is used to format the string `formatted_string` with curly braces `{}` as placeholders.
  - Inside the curly braces, we can specify the index of the argument to be inserted, or leave it empty to use the default order.
  - The `:.2f` format specifier is used to format the float value `height` with two decimal places.
  - The resulting formatted string is printed.

  ##### Example 3: Using f-strings:

  ```python
  # Example using f-strings (formatted string literals) for string formatting
  name = 'Alice'
  age = 30
  height = 1.75
  formatted_string = f'Name: {name}, Age: {age}, Height: {height:.2f} meters'
  print(formatted_string)
  ```

  **Explanation:**
  - In this example, we define variables `name`, `age`, and `height`.
  - We use f-strings, denoted by the `f` prefix before the string literal, to directly embed Python expressions within curly braces `{}`.
  - Inside the curly braces, we can directly reference variables and expressions.
  - The `:.2f` format specifier is used to format the float value `height` with two decimal places.
  - The resulting formatted string is printed.


## Regular Expressions:

Python's `re` module provides support for working with **regular expressions**, allowing for sophisticated string manipulation operations such as pattern matching, searching, and substitution.

Regular expressions (regex) are powerful tools used for pattern matching and string manipulation. They provide a concise and flexible means of searching, extracting, and replacing patterns within text data. Regex patterns are defined using a formal syntax that allows for specifying complex search patterns with a combination of literal characters and metacharacters.

**How Regex Works:**
1. **Pattern Compilation:** Regex patterns are compiled into a finite state machine (FSM) or a deterministic finite automaton (DFA) by the regex engine.
2. **String Matching:** The compiled pattern is applied to the input string. The regex engine traverses the input string character by character, attempting to match the pattern at each position.
3. **Pattern Matching:** At each position in the input string, the regex engine attempts to match the pattern. It uses backtracking and other algorithms to find the longest possible match.
4. **Match Verification:** If a match is found, the regex engine verifies the match against the entire pattern to ensure it meets the specified criteria (e.g., capturing groups, anchors).
5. **Result Retrieval:** If a match is successful, the regex engine returns the matched substring or information about the match (e.g., captured groups).

**Common Regex Metacharacters:**
- `.` : Matches any single character except newline.
- `^` : Anchors the match to the start of the string.
- `$` : Anchors the match to the end of the string.
- `*` : Matches zero or more occurrences of the preceding character.
- `+` : Matches one or more occurrences of the preceding character.
- `?` : Matches zero or one occurrence of the preceding character.
- `\d` : Matches any digit (equivalent to `[0-9]`).
- `\w` : Matches any alphanumeric character (equivalent to `[a-zA-Z0-9_]`).
- `\s` : Matches any whitespace character (e.g., space, tab, newline).


Suppose we want to extract all email addresses from a given text using regex:

```python
import re

# Input text containing email addresses
text = "Contact us at info@example.com or support@example.org for assistance."

# Define regex pattern to match email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Search for email addresses in the text
matches = re.findall(pattern, text)

# Print the matched email addresses
for match in matches:
    print(match)
```

**Explanation:**
- We import the `re` module, which provides support for working with regular expressions in Python.
- We define the input text containing email addresses.
- We define a regex pattern `pattern` to match email addresses. The pattern `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b` matches typical email address formats.
- We use `re.findall()` to search for all occurrences of the pattern in the input text and extract the matched email addresses.
- Finally, we print the matched email addresses.



### Example 1: Matching Dates in DD/MM/YYYY Format

```python
import re

# Input text containing dates
text = "Meeting scheduled for 15/07/2022 and deadline is 31/12/2023."

# Define regex pattern to match dates in DD/MM/YYYY format
pattern = r'\b(\d{2})/(\d{2})/(\d{4})\b'

# Search for dates in the text
matches = re.findall(pattern, text)

# Print the matched dates
for match in matches:
    print("/".join(match))
```

- We start by importing the `re` module, which provides support for working with regular expressions in Python.
- The input text `text` contains dates in the format DD/MM/YYYY.
- We define a regex pattern `pattern` to match dates in the DD/MM/YYYY format. Let's break down the pattern:
  - `\b`: Matches a word boundary to ensure the date is not part of a larger word.
  - `(\d{2})`: Captures two digits (day) within parentheses `()`.
  - `/`: Matches the forward slash separator.
  - `(\d{2})`: Captures two digits (month) within parentheses `()`.
  - `/`: Matches the forward slash separator.
  - `(\d{4})`: Captures four digits (year) within parentheses `()`.

- We use the `re.findall()` function to search for all occurrences of the pattern in the input text `text`.
- The `findall()` function returns a list of tuples, where each tuple represents a match and contains the captured groups (day, month, year).
- We iterate over the matches and print each date by joining the captured groups with slashes using the `"/".join()` method.

**Output:**
```
15/07/2022
31/12/2023
```


### Example 2: Extracting Phone Numbers

```python
import re

# Input text containing phone numbers
text = "Contact us at +1 (123) 456-7890 or 555-123-4567 for assistance."

# Define regex pattern to match phone numbers
pattern = r'\b(?:\+\d{1,2}\s)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'

# Search for phone numbers in the text
matches = re.findall(pattern, text)

# Print the matched phone numbers
for match in matches:
    print(match)
```

- We begin by importing the `re` module, which provides support for working with regular expressions in Python.
- The input text `text` contains phone numbers in various formats.
- We define a regex pattern `pattern` to match phone numbers. Let's break down the pattern:
  - `\b`: Matches a word boundary to ensure the phone number is not part of a larger word.
  - `(?:\+\d{1,2}\s)?`: Optionally matches an international dialing code (\+\d{1,2}) followed by whitespace (\s). The `(?: ... )` syntax creates a non-capturing group.
  - `\(?\d{3}\)?`: Matches an optional opening parenthesis `(` followed by three digits `\d{3}` and an optional closing parenthesis `)`.
  - `[-.\s]?`: Optionally matches a hyphen, period, or whitespace.
  - `\d{3}`: Matches three digits.
  - `[-.\s]?`: Optionally matches a hyphen, period, or whitespace.
  - `\d{4}`: Matches four digits.
  - `\b`: Matches a word boundary to ensure the phone number is not part of a larger word.

- We use the `re.findall()` function to search for all occurrences of the pattern in the input text `text`.
- The `findall()` function returns a list of phone numbers that match the pattern.
- We iterate over the matched phone numbers and print each one.

**Output:**
```
+1 (123) 456-7890
555-123-4567
```



### Example 3: Tokenizing Text into Words

```python
import re

# Input text containing sentences
text = "This is a sample sentence, with punctuation and numbers like 123."

# Define regex pattern to tokenize text into words
pattern = r'\b\w+\b'

# Tokenize the text into words
words = re.findall(pattern, text)

# Print the tokenized words
for word in words:
    print(word)
```

**Explanation:**
- We start by importing the `re` module, which provides support for working with regular expressions in Python.
- The input text `text` contains sentences with words.
- We define a regex pattern `pattern` to tokenize the text into words. Let's break down the pattern:
  - `\b`: Matches a word boundary to ensure the word is not part of a larger word.
  - `\w+`: Matches one or more word characters (letters, digits, or underscores). The `+` quantifier ensures that we match entire words.
  - `\b`: Matches a word boundary to ensure the word is not part of a larger word.

- We use the `re.findall()` function to search for all occurrences of the pattern in the input text `text`.
- The `findall()` function returns a list of words that match the pattern.
- We iterate over the tokenized words and print each one.

**Output:**
```
This
is
a
sample
sentence
with
punctuation
and
numbers
like
123
```

The pattern efficiently captures individual words in the text, ignoring punctuation and whitespace, allowing for precise extraction of words for text processing and analysis.



### Example 4: Validating Password Strength

```python
import re

# Input password
password = "MyP@ssw0rd123!"

# Define regex pattern to validate password strength
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# Check if password meets the criteria
if re.match(pattern, password):
    print("Valid password.")
else:
    print("Invalid password. Password must contain at least 8 characters including uppercase, lowercase, digits, and special characters.")
```

- We begin by importing the `re` module, which provides support for working with regular expressions in Python.
- The input password `password` is provided as a string.
- We define a regex pattern `pattern` to validate the strength of the password. Let's break down the pattern:
  - `^`: Matches the start of the string.
  - `(?=.*[a-z])`: Positive lookahead assertion to ensure the presence of at least one lowercase letter.
  - `(?=.*[A-Z])`: Positive lookahead assertion to ensure the presence of at least one uppercase letter.
  - `(?=.*\d)`: Positive lookahead assertion to ensure the presence of at least one digit.
  - `(?=.*[@$!%*?&])`: Positive lookahead assertion to ensure the presence of at least one special character.
  - `[A-Za-z\d@$!%*?&]{8,}`: Matches a string consisting of at least 8 characters, including letters (uppercase and lowercase), digits, and special characters.
  - `$`: Matches the end of the string.

- We use the `re.match()` function to check if the password matches the pattern.
- If the password matches the pattern, we print "Valid password." Otherwise, we print a message indicating that the password does not meet the criteria.

**Output (for the provided password):**

```
Valid password.
```



**More Information:**

https://docs.python.org/3/howto/regex.html

## Unicode and Encoding:

Unicode is a universal character encoding standard that aims to represent every character from every language and script in a consistent and unambiguous manner. It assigns each character a unique code point, typically represented in hexadecimal format (e.g., U+0041 for the letter 'A'). Unicode supports a vast range of characters, including letters, digits, symbols, emojis, and characters from various writing systems such as **Persian**, Latin, Cyrillic, Chinese, Arabic, and more.

Encoding, on the other hand, is the process of converting text from one representation (e.g., Unicode) to another representation (e.g., bytes) for storage or transmission. Since computers work with binary data, text must be encoded into bytes before it can be stored in files, transmitted over networks, or processed by software. There are various encoding schemes available, such as UTF-8, UTF-16, UTF-32, ASCII, ISO-8859-1 (Latin-1), and more.

Here's an example to illustrate the importance of Unicode and encoding:

```python
# Unicode example
text = "سلام دنیا"  # Persian text meaning "Hello, world" in English

# Encoding text using UTF-8
encoded_text = text.encode('utf-8')

# Decoding text back to Unicode
decoded_text = encoded_text.decode('utf-8')

# Print original, encoded, and decoded text
print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)
```

**Explanation:**
- We have a Unicode string `text` containing Chinese characters meaning "Hello, world" in English.
- We encode the Unicode text using the UTF-8 encoding scheme, which represents each Unicode character as a sequence of one to four bytes.
- The encoded text `encoded_text` is a sequence of bytes suitable for storage or transmission.
- We decode the encoded text back to Unicode using the UTF-8 decoding scheme.
- The decoded text `decoded_text` is the original Unicode string reconstructed from the encoded bytes.
- Finally, we print the original, encoded, and decoded text to demonstrate the round-trip conversion without loss of information.

#### Highly Recommended to Read:

*https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/*

https://tonsky.me/blog/unicode/

## File I/O and String Manipulation:

String manipulation often plays a crucial role in file input/output operations, such as reading text files, parsing data, and formatting output.
