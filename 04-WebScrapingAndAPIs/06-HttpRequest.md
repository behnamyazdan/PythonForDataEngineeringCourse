# HTTP Requests

## What is HTTP?

HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the web. It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.

## Basic Concepts of HTTP:

1. **Client-Server Architecture:**

   - The client (usually a web browser or a web scraping script) sends a request to the server.
   - The server processes the request and sends back a response.

   <img src="../_assets/http_connection.gif">

2. **HTTP Methods:**

   - **GET:** Requests data from a specified resource. It should not alter the state of the server.
   - **POST:** Submits data to be processed to a specified resource.
   - **PUT:** Updates a current resource with new data.
   - **DELETE:** Removes the specified resource.
   - **HEAD:** Similar to GET, but it transfers the status line and header section only.
   - **OPTIONS:** Describes the communication options for the target resource.
   - **PATCH:** Applies partial modifications to a resource.

## Anatomy of an HTTP Request

An HTTP request consists of several components: the request line, headers, and an optional body. Let's dive deeper into each part.

### 1. Request Line

The request line is the first line of an HTTP request and contains three parts:

- **HTTP Method**
- **Request URI**
- **HTTP Version**

**Example:**

```http
GET /index.html HTTP/1.1
```

- **HTTP Method:** This specifies the action to be performed on the resource. Common methods include:
  - `GET`: Retrieve data from the server.
  - `POST`: Send data to the server.
  - `PUT`: Update an existing resource.
  - `DELETE`: Remove a resource.
  - `HEAD`: Retrieve headers for a resource (without the body).
  - `OPTIONS`: Describe communication options for the target resource.
  - `PATCH`: Apply partial modifications to a resource.

- **Request URI (Uniform Resource Identifier):** This specifies the resource to be fetched or acted upon. It can be an absolute path or a complete URL.

- **HTTP Version:** This indicates the HTTP protocol version being used (e.g., `HTTP/1.1`, `HTTP/2`).

### 2. Headers

Headers provide additional information about the request and how the client expects the server to respond. They consist of key-value pairs and are placed after the request line, each on a new line.

**Example:**

```http
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept-Language: en-US,en;q=0.5
```

**Common Headers:**

- **Host:** Specifies the domain name of the server (mandatory in HTTP/1.1).

  ```http
  Host: example.com
  ```

- **User-Agent:** Identifies the client software (e.g., browser or bot).

  ```http
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
  ```

- **Accept:** Specifies the media types the client is willing to receive.

  ```http
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
  ```

- **Accept-Language:** Indicates the preferred languages for the response.

  ```http
  Accept-Language: en-US,en;q=0.5
  ```

- **Accept-Encoding:** Specifies the content encoding (e.g., gzip, deflate) that the client can understand.

  ```http
  Accept-Encoding: gzip, deflate, br
  ```

- **Connection:** Controls whether the network connection stays open after the current transaction.

  ```http
  Connection: keep-alive
  ```

- **Referer:** The URL of the page that linked to the resource being requested. Helps maintain context.

  ```http
  Referer: https://example.com/
  ```

- **Authorization:** Contains credentials for authenticating the client with the server.

  ```http
  Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
  ```

- **Cookie:** Sends stored cookies to the server.

  ```http
  Cookie: sessionId=abc123; preferredLanguage=en
  ```

### 3. Body

The body of an HTTP request is optional and typically used with methods like `POST`, `PUT`, or `PATCH` to send data to the server. The body can contain any type of data, such as form data, JSON, XML, or binary data.

**Example:**

```http
POST /login HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Content-Type: application/x-www-form-urlencoded
Content-Length: 29

username=user&password=pass
```

In this example:

- The request line indicates a `POST` request to the `/login` endpoint.
- The headers include `Host`, `User-Agent`, `Content-Type`, and `Content-Length`.
- The body contains URL-encoded form data: `username=user&password=pass`.

### Example: Making a GET Request

Let's use Python's `requests` library to make a GET request and analyze the components.

```python
import requests

# Define the URL
url = 'https://httpbin.org/get'

# Make the GET request
response = requests.get(url)

# Print the request line and headers
print(f"Request Line: {response.request.method} {response.request.url} {response.request.version}")
print("Request Headers:")
for k, v in response.request.headers.items():
    print(f"{k}: {v}")

# Print the response
print("Response Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Body:", response.text)
```

**Output:**

```
Request Line: GET https://httpbin.org/get HTTP/1.1
Request Headers:
User-Agent: python-requests/2.25.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive

Response Status Code: 200
Response Headers: {...}
Response Body: {...}
```

In this example:

- The request line shows the `GET` method, the URL, and the HTTP version.
- The request headers include `User-Agent`, `Accept-Encoding`, `Accept`, and `Connection`.
- The response includes the status code, headers, and body.

### Example: Making a POST Request with JSON Data

Let's make a POST request to send JSON data.

```python
import requests
import json

# Define the URL and the data to be sent
url = 'https://httpbin.org/post'
data = {'username': 'user', 'password': 'pass'}

# Make the POST request
response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))

# Print the request line and headers
print(f"Request Line: {response.request.method} {response.request.url} {response.request.version}")
print("Request Headers:")
for k, v in response.request.headers.items():
    print(f"{k}: {v}")

# Print the request body
print("Request Body:", response.request.body)

# Print the response
print("Response Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Body:", response.text)
```

**Output:**

```
Request Line: POST https://httpbin.org/post HTTP/1.1
Request Headers:
User-Agent: python-requests/2.25.1
Content-Type: application/json
Content-Length: 31
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive

Request Body: {"username": "user", "password": "pass"}

Response Status Code: 200
Response Headers: {...}
Response Body: {...}
```

In this example:

- The request line shows the `POST` method, the URL, and the HTTP version.
- The request headers include `User-Agent`, `Content-Type`, `Content-Length`, `Accept-Encoding`, `Accept`, and `Connection`.
- The request body contains JSON data.
- The response includes the status code, headers, and body.

The request line specifies the method, URI, and HTTP version.

Headers provide additional information about the request, such as the client type, accepted content types, and cookies.

The body is optional and used to send data to the server, primarily in POST, PUT, and PATCH requests.

## Important Headers for Web Scraping:

1. **User-Agent:**

   - Identifies the client software originating the request. Some websites block requests without a proper User-Agent header.

   ```http
   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
   ```

2. **Referer:**

   - The URL of the page that linked to the resource being requested. Helps in maintaining the context of the request.

   ```http
   Referer: https://example.com/
   ```

3. **Accept:**

   - Specifies the content types the client is willing to accept.

   ```http
   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
   ```

4. **Accept-Language:**

   - Indicates the preferred languages for the response.

   ```http
   Accept-Language: en-US,en;q=0.5
   ```

5. **Cookies:**

   - Used to send stored cookies to the server.

   ```http
   Cookie: sessionId=abc123; preferredLanguage=en
   ```

### Example: Using Requests Library

**1. Making a Basic GET Request:**

```python
import requests

url = 'https://httpbin.org/get'
response = requests.get(url)

print(response.status_code)  # Outputs: 200
print(response.text)  # Outputs the HTML content
```

**2. Adding Headers:**

```python
import requests

url = 'https://httpbin.org/headers'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'en-US,en;q=0.5'
}

response = requests.get(url, headers=headers)

print(response.status_code)  # Outputs: 200
print(response.json())  # Outputs the headers received by the server
```

**3. Sending URL Parameters:**

```python
import requests

url = 'https://httpbin.org/get'
params = {'key1': 'value1', 'key2': 'value2'}

response = requests.get(url, params=params)

print(response.status_code)  # Outputs: 200
print(response.json())  # Outputs the URL parameters received by the server
```

**4. Handling Cookies:**

```python
import requests

url = 'https://httpbin.org/cookies'
cookies = {'session_id': '123456789'}

response = requests.get(url, cookies=cookies)

print(response.status_code)  # Outputs: 200
print(response.json())  # Outputs the cookies received by the server
```

**5. Managing Sessions:**

```python
import requests

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
})

# First request
response = session.get('https://httpbin.org/cookies/set/session_id/123456789')
print(response.status_code)  # Outputs: 200

# Second request with the same session
response = session.get('https://httpbin.org/cookies')
print(response.json())  # Outputs: {'cookies': {'session_id': '123456789'}}
```

### Summary

HTTP requests are the backbone of web scraping, allowing you to interact with web servers and retrieve data. Key concepts include under	standing HTTP methods, request and response anatomy, and status codes. The `requests` library in Python provides a simple interface to make HTTP requests, handle headers, cookies, and sessions, making it an essential tool for web scraping.

Understanding how to properly form and send HTTP requests, and how to interpret the responses, is crucial for effective and ethical web scraping. This knowledge enables you to extract data reliably and handle various web scraping challenges such as dynamic content and authentication.
