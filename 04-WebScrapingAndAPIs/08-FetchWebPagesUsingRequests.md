# Fetch Web Pages Using Requests Library

The `requests` library in Python is a powerful and user-friendly tool for making HTTP requests. It simplifies interacting with web services and handling HTTP operations, making it a go-to choice for web scraping and API interactions. Understanding how to make various types of requests, handle responses, work with headers, query parameters, and JSON data, and manage timeouts and authentication is essential for effective web scraping and API usage.

## Installation

First, you need to install the `requests` library:

```bash
pip install requests
```

## Making HTTP Requests with Requests

The `requests` library supports several HTTP methods, including `GET`, `POST`, `PUT`, `DELETE`, `HEAD`, and `OPTIONS`. Here we'll focus on the most commonly used methods: `GET` and `POST`.

### Basic Usage of Requests

1. **GET Request**

A `GET` request is used to retrieve data from a specified resource. Here's a simple example:

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

print(response.status_code)  # Output: 200
print(response.headers['content-type'])  # Output: application/json; charset=utf-8
print(response.text)
```

**Output:**

```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit repellat nisi ..."
}
```

In this example:

- `response.status_code`: Returns the HTTP status code of the response.
- `response.headers`: Returns the response headers.
- `response.text`: Returns the response body as a string.

2. **POST Request**

A `POST` request is used to send data to a server to create or update a resource. Here's an example:

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
payload = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post(url, json=payload)

print(response.status_code)  # Output: 201
print(response.json())
```

**Output:**

```json
{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}
```

In this example:

- `payload`: The data to be sent in the body of the `POST` request.
- `response.json()`: Returns the JSON response content as a dictionary.

### Handling Query Parameters

You can pass query parameters in a URL using the `params` parameter in the `requests.get()` method.

**Example:**

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}
response = requests.get(url, params=params)

print(response.url)  # Output: https://jsonplaceholder.typicode.com/posts?userId=1
print(response.json())
```

### Headers

You can specify custom headers for your request using the `headers` parameter.

**Example:**

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)

print(response.status_code)
print(response.request.headers)
```

### Timeouts

You can specify a timeout for your request to avoid waiting indefinitely.

**Example:**

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
try:
    response = requests.get(url, timeout=5)
    print(response.status_code)
except requests.Timeout:
    print('The request timed out')
```

### Authentication

The `requests` library supports various authentication methods, such as Basic Authentication.

**Example:**

```python
import requests
from requests.auth import HTTPBasicAuth

url = 'https://httpbin.org/basic-auth/user/passwd'
response = requests.get(url, auth=HTTPBasicAuth('user', 'passwd'))

print(response.status_code)  # Output: 200
```

### Handling JSON Data

The `requests` library makes it easy to work with JSON data. You can use the `json` parameter to send JSON data and `response.json()` to parse the response.

**Example:**

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
payload = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post(url, json=payload)

print(response.json())
```

### Handling Redirects

By default, `requests` follows redirects. You can disable this behavior if needed.

**Example:**

```python
import requests

url = 'http://github.com'
response = requests.get(url, allow_redirects=False)

print(response.status_code)  # Output: 301
print(response.headers['Location'])  # Output: https://github.com/
```

### Uploading Files

You can upload files using the `files` parameter.

**Example:**

```python
import requests

url = 'https://httpbin.org/post'
files = {'file': open('test_file/test.txt', 'rb')}
response = requests.post(url, files=files)

print(response.status_code)  # Output: 200
print(response.json())
```

### Example: Web Scraping with Requests

Let's put it all together in a more comprehensive example where we use the `requests` library to scrape data from a website.

**Scenario:** Scrape the titles and links of the latest posts from a blog page.

**Example Code:**

```python
import requests
from bs4 import BeautifulSoup

url = 'https://example-blog.com'

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Find all post titles and links
    posts = soup.find_all('article', class_='post')
    
    for post in posts:
        title = post.find('h2', class_='post-title').get_text()
        link = post.find('a')['href']
        print(f"Title: {title}\nLink: {link}\n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
```

In this example:

1. **Making a GET Request:** We use `requests.get()` to fetch the blog page.
2. **Checking the Response Status:** We check if the request was successful by examining `response.status_code`.
3. **Parsing HTML with BeautifulSoup:** We parse the HTML content using BeautifulSoup.
4. **Finding and Extracting Data:** We locate the post titles and links and print them.

## Error Handling

Error handling is an essential aspect of working with the `requests` library in Python. When making HTTP requests, various errors can occur, such as network issues, server errors, or invalid responses. Proper error handling ensures that your program can gracefully handle these situations and respond accordingly. Here's how you can handle errors in `requests`:

### HTTP Errors

HTTP errors occur when the server responds with a status code indicating an error. These errors typically fall into two categories: client errors (status codes 4xx) and server errors (status codes 5xx).

#### Handling HTTP Errors

You can check the status code of the response using the `.status_code` attribute of the `Response` object and raise an exception if an error occurs. The `raise_for_status()` method is a convenient way to raise an exception for HTTP errors.

```python
import requests

url = 'https://api.example.com/data'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    # Process the response
except requests.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
```

### Connection Errors

Connection errors occur when the client cannot establish a connection to the server. This can happen due to network issues, DNS resolution failures, or server unavailability.

#### Handling Connection Errors

You can handle connection errors using the `requests.exceptions.RequestException` exception, which is a base class for all `requests` exceptions.

```python
import requests

url = 'https://api.example.com/data'

try:
    response = requests.get(url)
    response.raise_for_status()
    # Process the response
except requests.RequestException as req_err:
    print(f'Request error occurred: {req_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
```

### Timeout Errors

Timeout errors occur when the server does not respond within the specified timeout period. You can set a timeout for the request using the `timeout` parameter.

#### Handling Timeout Errors

You can handle timeout errors by catching the `requests.exceptions.Timeout` exception.

```python
import requests

url = 'https://api.example.com/data'

try:
    response = requests.get(url, timeout=5)  # Set a timeout of 5 seconds
    response.raise_for_status()
    # Process the response
except requests.exceptions.Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
```

### Main exceptions that the `requests` library may raise:

| Exception                                  | Description                                                  |
| ------------------------------------------ | ------------------------------------------------------------ |
| `requests.exceptions.RequestException`     | Base class for all `requests` exceptions.                    |
| `requests.exceptions.HTTPError`            | Raised for HTTP errors, such as 4xx (client errors) and 5xx (server errors) status codes. |
| `requests.exceptions.ConnectionError`      | Raised when a connection cannot be established with the server, including DNS resolution failures and network issues. |
| `requests.exceptions.Timeout`              | Raised when the request times out before receiving a response from the server. |
| `requests.exceptions.TooManyRedirects`     | Raised when the maximum number of redirects is exceeded (default is 30). |
| `requests.exceptions.URLRequired`          | Raised when a valid URL is required but not provided.        |
| `requests.exceptions.TooManyRedirects`     | Raised when the maximum number of redirects is exceeded (default is 30). |
| `requests.exceptions.MissingSchema`        | Raised when the URL schema (e.g., http, https) is missing.   |
| `requests.exceptions.InvalidSchema`        | Raised when an invalid URL schema is provided.               |
| `requests.exceptions.InvalidURL`           | Raised when an invalid URL is provided.                      |
| `requests.exceptions.InvalidHeader`        | Raised when an invalid header is provided.                   |
| `requests.exceptions.InvalidProxyURL`      | Raised when an invalid proxy URL is provided.                |
| `requests.exceptions.ChunkedEncodingError` | Raised when the server returns chunked-encoded data that cannot be decoded. |
| `requests.exceptions.ContentDecodingError` | Raised when the response body cannot be decoded.             |
| `requests.exceptions.StreamConsumedError`  | Raised when attempting to reuse a stream that has already been consumed. |
| `requests.exceptions.ProxyError`           | Raised for proxy-related errors.                             |
| `requests.exceptions.SSLError`             | Raised when an SSL/TLS-related error occurs.                 |
