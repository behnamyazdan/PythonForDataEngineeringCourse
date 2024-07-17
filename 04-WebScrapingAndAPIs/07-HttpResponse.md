# HTTP Response

An HTTP response is what a server sends back to the client after receiving and processing an HTTP request. Like HTTP requests, HTTP responses have a structured format that includes three main components: the status line, headers, and an optional body. Let's delve into each part.

#### 1. Status Line
The status line is the first line of an HTTP response and contains three parts:
- **HTTP Version**
- **Status Code**
- **Reason Phrase**

**Example:**
```http
HTTP/1.1 200 OK
```

- **HTTP Version:** This indicates the HTTP protocol version used by the server (e.g., `HTTP/1.1`, `HTTP/2`).
- **Status Code:** This is a three-digit code that indicates the result of the server's attempt to understand and satisfy the client's request. Status codes are categorized as follows:
  - `1xx` Informational: Request received, continuing process.
  - `2xx` Success: The action was successfully received, understood, and accepted.
  - `3xx` Redirection: Further action needs to be taken to complete the request.
  - `4xx` Client Error: The request contains bad syntax or cannot be fulfilled.
  - `5xx` Server Error: The server failed to fulfill a valid request.

- **Reason Phrase:** This is a short textual description of the status code.

**Example Status Codes:**
- `200 OK`: The request was successful.
- `404 Not Found`: The server cannot find the requested resource.
- `500 Internal Server Error`: The server encountered an unexpected condition.

#### 2. Headers
Headers in an HTTP response provide additional information about the response. They consist of key-value pairs and appear after the status line, each on a new line.

**Example:**
```http
Content-Type: text/html; charset=UTF-8
Content-Length: 138
Connection: keep-alive
```

**Common Headers:**
- **Content-Type:** Indicates the media type of the response body.
  ```http
  Content-Type: application/json
  ```

- **Content-Length:** The length of the response body in bytes.
  ```http
  Content-Length: 348
  ```

- **Connection:** Controls whether the network connection stays open after the current transaction.
  ```http
  Connection: close
  ```

- **Server:** Contains information about the server software handling the request.
  ```http
  Server: Apache/2.4.1 (Unix)
  ```

- **Set-Cookie:** Used to send cookies from the server to the client.
  ```http
  Set-Cookie: sessionId=abc123; Path=/; HttpOnly
  ```

- **Date:** The date and time at which the response was generated.
  ```http
  Date: Sat, 08 Jun 2024 12:35:00 GMT
  ```

- **Cache-Control:** Directives for caching mechanisms in both requests and responses.
  ```http
  Cache-Control: no-cache, no-store, must-revalidate
  ```

#### 3. Body
The body of an HTTP response is optional and contains the data requested by the client. The type and content of the body depend on the resource being requested and the headers provided.

**Example:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Example Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

If the `Content-Type` header is `application/json`, the body might look like:
```json
{
  "message": "Hello, World!"
}
```

### Example: Understanding an HTTP Response

Consider a practical example using Python's `requests` library to make a GET request and analyze the response components.

```python
import requests

# Define the URL
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Make the GET request
response = requests.get(url)

# Print the status line
print(f"Status Line: {response.status_code} {response.reason}")

# Print the response headers
print("Response Headers:")
for k, v in response.headers.items():
    print(f"{k}: {v}")

# Print the response body
print("Response Body:")
print(response.text)
```

**Output:**
```
Status Line: 200 OK
Response Headers:
Date: Sat, 08 Jun 2024 12:35:00 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 292
Connection: keep-alive
Server: cloudflare
Vary: Origin, Accept-Encoding

Response Body:
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit repellat nisi...",
}
```

In this example:
- **Status Line:** The status line indicates a successful `200 OK` response.
- **Response Headers:** These include `Date`, `Content-Type`, `Content-Length`, `Connection`, `Server`, and `Vary`.
- **Response Body:** Contains the JSON data for a specific post.

### Summary

An HTTP response is composed of three main parts:
- **Status Line:** Contains the HTTP version, status code, and reason phrase.
- **Headers:** Provide metadata about the response, such as content type, length, and caching policies.
- **Body:** Contains the actual data requested by the client, which can be HTML, JSON, XML, or other media types.

Understanding the anatomy of an HTTP response is crucial for web scraping and web development, as it helps in handling server responses effectively and ensuring robust communication between clients and servers.

---

## Optional Reading Topic:

### HTTP status codes

This table provides a comprehensive overview of HTTP status codes, their categories, descriptions, and practical examples. This knowledge is essential for understanding the various responses you might encounter while performing web scraping and how to handle them effectively.

| **Status Code**       | **Category**                    | **Description**                                              | **Example**                                                  |
| --------------------- | ------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **1xx Informational** |                                 |                                                              |                                                              |
| 100                   | Continue                        | The initial part of a request has been received and the client should continue. | The client sends a request to the server with `Expect: 100-continue` header and receives 100 Continue in response before sending the body. |
| 101                   | Switching Protocols             | The server is switching protocols as requested by the client. | A client asks the server to switch protocols from HTTP/1.1 to HTTP/2.0 using the `Upgrade` header. |
| 102                   | Processing                      | The server has received and is processing the request, but no response is available yet. | A WebDAV request that takes a long time to process returns 102 Processing to prevent the client from timing out. |
| 103                   | Early Hints                     | Used to return some response headers before final HTTP message. | A server sends headers early to hint about content type and other info before final response is ready. |
| **2xx Success**       |                                 |                                                              |                                                              |
| 200                   | OK                              | The request was successful, and the server returned the requested resource. | A client requests a webpage and receives the full HTML content with status code 200 OK. |
| 201                   | Created                         | The request was successful, and a new resource was created.  | A client submits a form to create a new user account and receives 201 Created upon success. |
| 202                   | Accepted                        | The request has been accepted for processing, but the processing is not complete. | A client uploads a file, and the server returns 202 Accepted indicating the file will be processed later. |
| 203                   | Non-Authoritative Information   | The request was successful, but the returned information may be from another source. | A proxy server returns 203 Non-Authoritative Information indicating the data might not be from the original server. |
| 204                   | No Content                      | The request was successful, but there is no content to send in the response. | A client performs a DELETE operation on a resource and receives 204 No Content, indicating successful deletion without a body in the response. |
| 205                   | Reset Content                   | The request was successful, but the client should reset the view. | After a successful form submission, a client receives 205 Reset Content indicating the form should be cleared. |
| 206                   | Partial Content                 | The server is delivering only part of the resource due to a range header sent by the client. | A client requests a portion of a video file using the Range header and receives 206 Partial Content with the requested bytes. |
| 207                   | Multi-Status                    | WebDAV; the message body contains multiple separate responses. | A WebDAV server returns 207 Multi-Status in response to a PROPFIND request, listing properties of multiple files. |
| 208                   | Already Reported                | WebDAV; members of a DAV binding have already been enumerated in a previous reply. | A WebDAV server indicates that the bindings have been enumerated in a previous response using 208 Already Reported. |
| 226                   | IM Used                         | The server has fulfilled a request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance. | A server returns 226 IM Used indicating that a delta encoding has been applied to the response body. |
| **3xx Redirection**   |                                 |                                                              |                                                              |
| 300                   | Multiple Choices                | The request has more than one possible response. The user or user agent can select a preferred response. | A client requests a resource that exists in multiple formats and receives 300 Multiple Choices with a list of available formats. |
| 301                   | Moved Permanently               | The requested resource has been moved to a new URL permanently. | A client requests a webpage that has been permanently moved to a new URL and receives 301 Moved Permanently with the new URL. |
| 302                   | Found                           | The requested resource is temporarily located at a different URL. | A client requests a resource that is temporarily at a different URL and receives 302 Found with the temporary URL. |
| 303                   | See Other                       | The response to the request can be found under another URL using a GET method. | After submitting data, a client is redirected to another page with a 303 See Other status and the new URL. |
| 304                   | Not Modified                    | The resource has not been modified since the last request.   | A client revalidates a cached resource with a If-Modified-Since header and receives 304 Not Modified if it hasn't changed. |
| 305                   | Use Proxy                       | The requested resource is only available through a proxy.    | Deprecated due to security concerns; clients used to receive 305 Use Proxy indicating a proxy URL. |
| 306                   | Switch Proxy                    | No longer used, but reserved for future use.                 | Was used to indicate subsequent requests should use a specified proxy. |
| 307                   | Temporary Redirect              | The requested resource resides temporarily under a different URL, but the client should use the original method for the request. | A client receives 307 Temporary Redirect indicating the resource is temporarily at a new URL and should use the same HTTP method. |
| 308                   | Permanent Redirect              | The requested resource has been permanently moved to a new URL, and future requests should use the new URL. | Similar to 301, but the request method and body must not be changed; 308 Permanent Redirect indicates the new URL. |
| **4xx Client Error**  |                                 |                                                              |                                                              |
| 400                   | Bad Request                     | The server could not understand the request due to invalid syntax. | A client sends a malformed request and receives 400 Bad Request indicating syntax error. |
| 401                   | Unauthorized                    | The client must authenticate itself to get the requested response. | A client tries to access a protected resource without valid authentication and receives 401 Unauthorized. |
| 402                   | Payment Required                | Reserved for future use. Initially intended for digital payment systems. | Not widely used; intended for future use to require payment for accessing resources. |
| 403                   | Forbidden                       | The client does not have access rights to the content.       | A client tries to access a resource without proper permissions and receives 403 Forbidden. |
| 404                   | Not Found                       | The server cannot find the requested resource.               | A client requests a non-existent webpage and receives 404 Not Found. |
| 405                   | Method Not Allowed              | The request method is known by the server but is not supported by the target resource. | A client attempts to use POST on a resource that only supports GET and receives 405 Method Not Allowed. |
| 406                   | Not Acceptable                  | The requested resource is capable of generating only content not acceptable according to the Accept headers sent in the request. | A client requests a specific content type not supported by the server and receives 406 Not Acceptable. |
| 407                   | Proxy Authentication Required   | The client must first authenticate itself with the proxy.    | A client needs to authenticate with a proxy server and receives 407 Proxy Authentication Required. |
| 408                   | Request Timeout                 | The server would like to shut down this unused connection.   | A client takes too long to send a request and the server returns 408 Request Timeout. |
| 409                   | Conflict                        | The request could not be completed due to a conflict with the current state of the resource. | A client tries to update a resource with conflicting information and receives 409 Conflict. |
| 410                   | Gone                            | The requested resource is no longer available and will not be available again. | A client requests a resource that has been permanently removed and receives 410 Gone. |
| 411                   | Length Required                 | The server refuses to accept the request without a defined Content-Length. | A client sends a request without Content-Length header and receives 411 Length Required. |
| 412                   | Precondition Failed             | One or more preconditions given in the request header fields evaluated to false when tested on the server. | A client sends conditional request headers that fail and receives 412 Precondition Failed. |
| 413                   | Payload Too Large               | The request entity is larger than limits defined by server.  | A client uploads a file that is too large and receives 413 Payload Too Large. |
| 414                   | URI Too Long                    | The URI requested by the client is longer than the server is willing to interpret. | A client sends a request with an excessively long URL and receives 414 URI Too Long. |
| 415                   | Unsupported Media Type          | The media format of the requested data is not supported by the server. | A client uploads data in an unsupported format and receives 415 Unsupported Media Type. |
| 416                   | Range Not Satisfiable           | The range specified by the Range header field in the request can't be fulfilled. | A client requests a range of bytes that are not available and receives 416 Range Not Satisfiable. |
| 417                   | Expectation Failed              | The server cannot meet the requirements of the Expect request-header field. | A client uses the `Expect: 100-continue` header but the server cannot fulfill it and returns 417 Expectation Failed. |
| 418                   | I'm a teapot                    | Defined in RFC 2324, "Hyper Text Coffee Pot Control Protocol". Not an actual error, but a playful response. | A client sends a request to brew coffee and the server humorously responds with 418 I'm a teapot. |
| 421                   | Misdirected Request             | The request was directed at a server that is not able to produce a response. | A client sends a request to the wrong server and receives 421 Misdirected Request. |
| 422                   | Unprocessable Entity            | WebDAV; the request was well-formed but unable to be followed due to semantic errors. | A client submits a well-formed WebDAV request with semantic errors and receives 422 Unprocessable Entity. |
| 423                   | Locked                          | WebDAV; the resource that is being accessed is locked.       | A client attempts to modify a locked WebDAV resource and receives 423 Locked. |
| 424                   | Failed Dependency               | WebDAV; the request failed due to failure of a previous request. | A WebDAV request fails because a previous request failed, resulting in 424 Failed Dependency. |
| 425                   | Too Early                       | The server is unwilling to risk processing a request that might be replayed. | A server returns 425 Too Early indicating a request might be processed prematurely. |
| 426                   | Upgrade Required                | The client should switch to a different protocol.            | A client needs to switch to a different protocol such as TLS/1.0 and receives 426 Upgrade Required. |
| 428                   | Precondition Required           | The server requires the request to be conditional.           | A server requires conditions to be met before processing a request, resulting in 428 Precondition Required. |
| 429                   | Too Many Requests               | The client has sent too many requests in a given amount of time. | A client exceeds the rate limit and receives 429 Too Many Requests. |
| 431                   | Request Header Fields Too Large | The server is unwilling to process the request because its header fields are too large. | A client sends a request with excessively large header fields and receives 431 Request Header Fields Too Large. |
| 451                   | Unavailable For Legal Reasons   | The server is denying access to the resource as a consequence of a legal demand. | A client requests a resource that has been legally restricted and receives 451 Unavailable For Legal Reasons. |
| **5xx Server Error**  |                                 |                                                              |                                                              |
| 500                   | Internal Server Error           | The server has encountered a situation it doesn't know how to handle. | A client sends a request that causes an unexpected condition on the server, resulting in 500 Internal Server Error. |
| 501                   | Not Implemented                 | The request method is not supported by the server and cannot be handled. | A client uses an HTTP method not supported by the server and receives 501 Not Implemented. |
| 502                   | Bad Gateway                     | The server, while acting as a gateway or proxy, received an invalid response from the upstream server. | A client receives 502 Bad Gateway when the server is acting as a proxy and gets an invalid response from another server. |
| 503                   | Service Unavailable             | The server is not ready to handle the request.               | A client receives 503 Service Unavailable when the server is temporarily overloaded or under maintenance. |
| 504                   | Gateway Timeout                 | The server is acting as a gateway and cannot get a response in time. | A client receives 504 Gateway Timeout when the server acting as a proxy does not get a timely response from another server. |
| 505                   | HTTP Version Not Supported      | The HTTP version used in the request is not supported by the server. | A client sends a request using an HTTP version not supported by the server, resulting in 505 HTTP Version Not Supported. |
| 506                   | Variant Also Negotiates         | The server has an internal configuration error.              | A server returns 506 Variant Also Negotiates indicating a misconfiguration where content negotiation itself is configured to vary. |
| 507                   | Insufficient Storage            | WebDAV; the server is unable to store the representation needed to complete the request. | A client receives 507 Insufficient Storage when the server cannot store the necessary data for a WebDAV request. |
| 508                   | Loop Detected                   | WebDAV; the server detected an infinite loop while processing a request. | A client receives 508 Loop Detected when the server identifies an infinite loop in processing a WebDAV request. |
| 510                   | Not Extended                    | Further extensions to the request are required for the server to fulfill it. | A server returns 510 Not Extended indicating additional extensions are required to process the request. |
| 511                   | Network Authentication Required | The client needs to authenticate to gain network access.     | A client receives 511 Network Authentication Required when it must authenticate to access a network, such as a captive portal. |
