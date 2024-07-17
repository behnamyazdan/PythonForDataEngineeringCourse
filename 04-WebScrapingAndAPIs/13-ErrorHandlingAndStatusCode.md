# Error Handling and Status Codes

When working with APIs, handling errors and understanding HTTP status codes are crucial for building robust applications. Proper error handling ensures that your application can gracefully handle unexpected situations, such as network issues or invalid responses from the server.

## Understanding HTTP Status Codes

HTTP status codes are issued by a server in response to a client's request made to the server. They help indicate whether the request was successfully processed or if there were any issues.

Here is a table summarizing common HTTP status codes and their meanings:

| Status Code | Meaning               | Description                                                  |
| ----------- | --------------------- | ------------------------------------------------------------ |
| 200         | OK                    | The request was successful.                                  |
| 201         | Created               | The request was successful and a resource was created.       |
| 204         | No Content            | The request was successful but there is no content to send in the response. |
| 400         | Bad Request           | The server could not understand the request due to invalid syntax. |
| 401         | Unauthorized          | The client must authenticate itself to get the requested response. |
| 403         | Forbidden             | The client does not have access rights to the content.       |
| 404         | Not Found             | The server can not find the requested resource.              |
| 500         | Internal Server Error | The server has encountered a situation it doesn't know how to handle. |
| 502         | Bad Gateway           | The server, while acting as a gateway or proxy, received an invalid response from the upstream server. |
| 503         | Service Unavailable   | The server is not ready to handle the request.               |
| 504         | Gateway Timeout       | The server, while acting as a gateway or proxy, did not get a response in time from the upstream server. |

## Error Handling in API Requests

Handling errors in API requests involves checking the status code of the response and responding accordingly. The `requests` library provides a straightforward way to do this.

#### Example: Basic Error Handling

Here is a basic example of making an API request and handling different types of errors:

```python
import requests

url = 'https://api.example.com/data'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
    
    # Process the JSON response if the request was successful
    data = response.json()
    print(data)

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # e.g. 404 Not Found
except requests.exceptions.ConnectionError as conn_err:
    print(f'Connection error occurred: {conn_err}')
except requests.exceptions.Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')
except requests.exceptions.RequestException as req_err:
    print(f'An error occurred: {req_err}')
```

### Detailed Error Handling

For more detailed error handling, you can check specific status codes and respond accordingly. This can involve retrying the request, logging errors, or taking other appropriate actions based on the type of error.

#### Example: Detailed Error Handling

```python
import requests

url = 'https://api.example.com/data'

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    elif response.status_code == 400:
        print('Bad Request: The server could not understand the request.')
    elif response.status_code == 401:
        print('Unauthorized: Access is denied due to invalid credentials.')
    elif response.status_code == 403:
        print('Forbidden: The server understood the request, but it refuses to authorize it.')
    elif response.status_code == 404:
        print('Not Found: The requested resource could not be found.')
    elif response.status_code == 500:
        print('Internal Server Error: The server encountered an error and could not complete the request.')
    else:
        print(f'Unexpected status code: {response.status_code}')

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except requests.exceptions.ConnectionError as conn_err:
    print(f'Connection error occurred: {conn_err}')
except requests.exceptions.Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')
except requests.exceptions.RequestException as req_err:
    print(f'An error occurred: {req_err}')
```

### Retry Logic

In some cases, especially for transient errors (like network issues or server overload), it might be useful to implement retry logic.

#### Example: Implementing Retry Logic

```python
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

url = 'https://api.example.com/data'

session = requests.Session()
retry = Retry(
    total=5,  # Retry up to 5 times
    backoff_factor=1,  # Wait 1, 2, 4, 8, 16 seconds between retries
    status_forcelist=[500, 502, 503, 504]  # Retry on these status codes
)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

try:
    response = session.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except requests.exceptions.ConnectionError as conn_err:
    print(f'Connection error occurred: {conn_err}')
except requests.exceptions.Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')
except requests.exceptions.RequestException as req_err:
    print(f'An error occurred: {req_err}')
```

Proper error handling and understanding HTTP status codes are essential when working with APIs. It ensures that your application can gracefully handle errors and provides a better user experience. By checking the response status code, handling different types of exceptions, and implementing retry logic, you can make your API interactions more robust and reliable.