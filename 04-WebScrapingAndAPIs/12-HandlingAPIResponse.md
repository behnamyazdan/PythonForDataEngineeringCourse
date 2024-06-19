# Handling API Responses

When you make requests to APIs, the responses typically come in structured data formats like JSON or XML. Parsing these responses correctly is crucial for working with the data they contain.

## Parsing JSON Responses

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy to read and write for humans and easy for machines to parse and generate. JSON is built on two structures:
1. **A collection of name/value pairs**: In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
2. **An ordered list of values**: In most languages, this is realized as an array, vector, list, or sequence.

Here's a breakdown of JSON elements and how they map to Python data types:

### JSON Data Types and Corresponding Python Types

| JSON Type      | Python Type | Example                         |
| -------------- | ----------- | ------------------------------- |
| Object         | dict        | `{"name": "John", "age": 30}`   |
| Array          | list        | `["apple", "banana", "cherry"]` |
| String         | str         | `"Hello, World!"`               |
| Number (int)   | int         | `123`                           |
| Number (float) | float       | `123.45`                        |
| Boolean        | bool        | `true` or `false`               |
| Null           | None        | `null`                          |

#### Example JSON Object

```json
{
  "name": "John Doe",
  "age": 30,
  "isEmployed": true,
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "zipcode": "10001"
  },
  "phoneNumbers": ["123-456-7890", "987-654-3210"]
}
```

### Python Representation

Using Python, you can parse JSON data into native data structures like dictionaries and lists. Here's an example:

```python
import json

# Example JSON string
json_str = '''
{
  "name": "John Doe",
  "age": 30,
  "isEmployed": true,
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "zipcode": "10001"
  },
  "phoneNumbers": ["123-456-7890", "987-654-3210"]
}
'''

# Parse JSON into a Python dictionary
data = json.loads(json_str)

# Accessing data in the dictionary
name = data['name']
age = data['age']
is_employed = data['isEmployed']
street = data['address']['street']
city = data['address']['city']
zipcode = data['address']['zipcode']
phone_numbers = data['phoneNumbers']

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Employed: {is_employed}")
print(f"Address: {street}, {city}, {zipcode}")
print(f"Phone Numbers: {', '.join(phone_numbers)}")
```

### Elements of JSON

| Element     | Description                                                  | Example                         |
| ----------- | ------------------------------------------------------------ | ------------------------------- |
| **Object**  | Enclosed in curly braces `{}`. Contains key/value pairs.     | `{"name": "John", "age": 30}`   |
| **Array**   | Enclosed in square brackets `[]`. Contains ordered lists of values. | `["apple", "banana", "cherry"]` |
| **String**  | Enclosed in double quotes `""`.                              | `"Hello, World!"`               |
| **Number**  | Can be integers or floats.                                   | `123` or `123.45`               |
| **Boolean** | Represented as `true` or `false`.                            | `true`                          |
| **Null**    | Represents a null value.                                     | `null`                          |

### Parsing JSON with Python

The `json` library in Python provides methods to parse JSON from strings or files and to convert Python objects into JSON strings.

#### Parsing JSON from a String

```python
import json

json_str = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_str)
print(data)
```

#### Parsing JSON from a File

```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
```

#### Parsing JSON from API Responses

When working with APIs, it's common to receive data in JSON format. Parsing JSON allows you to convert this data into a format that can be easily manipulated within your programming environment. Python's `requests` library, combined with its built-in `json` module, makes this process straightforward.

##### Steps to Parse JSON from an API Response

1. **Make an API Request**: Use the `requests` library to make a request to the API.
2. **Check the Response**: Ensure that the request was successful by checking the response status code.
3. **Parse the JSON**: Convert the JSON response into a Python dictionary or list using the `json` method provided by the `requests` library.
4. **Access the Data**: Extract the required information from the parsed JSON structure.

### Example: Parsing JSON from an API Response

#### Scenario

Suppose we are accessing an API that provides information about users. The API endpoint is `https://api.example.com/users`, and the response is in JSON format.

1. **Making an API Request**

```python
import requests

url = 'https://api.example.com/users'
response = requests.get(url)
```

2. **Checking the Response**

Ensure that the request was successful by checking the status code.

```python
if response.status_code == 200:
    print("Request was successful")
else:
    print(f"Failed to retrieve data: {response.status_code}")
```

3. **Parsing the JSON**

If the request is successful, parse the JSON content.

```python
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
```

4. **Accessing the Data**

Assume the API returns the following JSON response:

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
]
```

To access and print the user information, you can do the following:

```python
if response.status_code == 200:
    data = response.json()
    
    # Iterate through the list of users
    for user in data:
        user_id = user['id']
        name = user['name']
        email = user['email']
        print(f"User ID: {user_id}, Name: {name}, Email: {email}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
```

### Handling Nested JSON

For more complex JSON responses, such as nested structures, you navigate through the hierarchy using dictionary keys and list indices.

#### Example: Nested JSON Response

Consider an API response with nested JSON:

```json
{
  "status": "success",
  "data": {
    "users": [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "address": {
          "street": "123 Main St",
          "city": "New York"
        }
      },
      {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "address": {
          "street": "456 Elm St",
          "city": "Los Angeles"
        }
      }
    ]
  }
}
```

To parse and access this data:

```python
if response.status_code == 200:
    data = response.json()
    
    # Access the list of users
    users = data['data']['users']
    
    # Iterate through the list of users
    for user in users:
        user_id = user['id']
        name = user['name']
        email = user['email']
        street = user['address']['street']
        city = user['address']['city']
        print(f"User ID: {user_id}, Name: {name}, Email: {email}, Address: {street}, {city}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
```

Parsing JSON responses from APIs involves:
- Making an HTTP request using the `requests` library.
- Checking the response status.
- Parsing the JSON content into a Python dictionary or list.
- Accessing and manipulating the parsed data.

Understanding how to parse JSON is crucial for working with APIs, as it allows you to interact with the data provided by various web services effectively.

## Parsing XML Responses

XML (eXtensible Markup Language) is another common format for API responses, especially in older or enterprise systems. Parsing XML responses allows you to convert the structured XML data into a format that can be easily manipulated within your programming environment. Python's `xml.etree.ElementTree` module provides a straightforward way to parse and work with XML data.

### Steps to Parse XML from an API Response

1. **Make an API Request**: Use the `requests` library to make a request to the API.
2. **Check the Response**: Ensure that the request was successful by checking the response status code.
3. **Parse the XML**: Use the `xml.etree.ElementTree` module to parse the XML content.
4. **Access the Data**: Extract the required information from the parsed XML structure.

### Example: Parsing XML from an API Response

Suppose we are accessing an API that provides information about books. The API endpoint is `https://api.example.com/books`, and the response is in XML format.

1. **Making an API Request**

```python
import requests

url = 'https://api.example.com/books'
response = requests.get(url)
```

2. **Checking the Response**

Ensure that the request was successful by checking the status code.

```python
if response.status_code == 200:
    print("Request was successful")
else:
    print(f"Failed to retrieve data: {response.status_code}")
```

3. **Parsing the XML**

If the request is successful, parse the XML content.

```python
import xml.etree.ElementTree as ET

if response.status_code == 200:
    root = ET.fromstring(response.content)
    print(ET.tostring(root, encoding='utf8').decode('utf8'))
else:
    print(f"Failed to retrieve data: {response.status_code}")
```

4. **Accessing the Data**

Assume the API returns the following XML response:

```xml
<books>
    <book>
        <id>1</id>
        <title>The Great Gatsby</title>
        <author>F. Scott Fitzgerald</author>
    </book>
    <book>
        <id>2</id>
        <title>1984</title>
        <author>George Orwell</author>
    </book>
</books>
```

To access and print the book information, you can do the following:

```python
if response.status_code == 200:
    root = ET.fromstring(response.content)
    
    # Iterate through the list of books
    for book in root.findall('book'):
        book_id = book.find('id').text
        title = book.find('title').text
        author = book.find('author').text
        print(f"Book ID: {book_id}, Title: {title}, Author: {author}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
```

### Handling Nested XML

For more complex XML responses, such as nested structures, you navigate through the hierarchy using tags.

#### Example: Nested XML Response

Consider an API response with nested XML:

```xml
<library>
    <section name="Fiction">
        <book>
            <id>1</id>
            <title>The Great Gatsby</title>
            <author>F. Scott Fitzgerald</author>
        </book>
        <book>
            <id>2</id>
            <title>1984</title>
            <author>George Orwell</author>
        </book>
    </section>
    <section name="Non-Fiction">
        <book>
            <id>3</id>
            <title>Sapiens</title>
            <author>Yuval Noah Harari</author>
        </book>
    </section>
</library>
```

To parse and access this data:

```python
if response.status_code == 200:
    root = ET.fromstring(response.content)
    
    # Iterate through the sections
    for section in root.findall('section'):
        section_name = section.attrib['name']
        print(f"Section: {section_name}")
        
        # Iterate through the list of books in each section
        for book in section.findall('book'):
            book_id = book.find('id').text
            title = book.find('title').text
            author = book.find('author').text
            print(f"  Book ID: {book_id}, Title: {title}, Author: {author}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
```

### Using XPath for Advanced XML Parsing

The `ElementTree` module also supports XPath expressions, which allow for more advanced and precise querying of XML data.

#### Example: Using XPath

```python
import xml.etree.ElementTree as ET

xml_data = '''
<library>
    <section name="Fiction">
        <book>
            <id>1</id>
            <title>The Great Gatsby</title>
            <author>F. Scott Fitzgerald</author>
        </book>
        <book>
            <id>2</id>
            <title>1984</title>
            <author>George Orwell</author>
        </book>
    </section>
    <section name="Non-Fiction">
        <book>
            <id>3</id>
            <title>Sapiens</title>
            <author>Yuval Noah Harari</author>
        </book>
    </section>
</library>
'''

root = ET.fromstring(xml_data)

# Find all books in the Fiction section
fiction_books = root.findall(".//section[@name='Fiction']/book")

for book in fiction_books:
    book_id = book.find('id').text
    title = book.find('title').text
    author = book.find('author').text
    print(f"Fiction Book - ID: {book_id}, Title: {title}, Author: {author}")
```

Parsing XML responses from APIs involves:
- Making an HTTP request using the `requests` library.
- Checking the response status.
- Parsing the XML content into an `ElementTree` object.
- Accessing and manipulating the parsed data using tag names and attributes.

