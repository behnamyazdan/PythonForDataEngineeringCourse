# Dealing with Pagination and Infinite Scrolling

When dealing with websites that use pagination or infinite scrolling, you can use the `requests` library to fetch the HTML of each page and `BeautifulSoup` to parse and extract the data.

## Handling Pagination

Pagination involves navigating through multiple pages to extract data. Typically, each page will have a unique URL or a parameter in the query string that changes for each page.

#### Example: Handling Pagination

Suppose we want to scrape data from a website that lists items across multiple pages, with each page accessible via a URL like `https://example.com/items?page=1`, `https://example.com/items?page=2`, and so on.

Here's a step-by-step approach:

1. **Fetch HTML for Each Page:**
2. **Parse and Extract Data:**
3. **Repeat for All Pages:** 

```python
import requests
from bs4 import BeautifulSoup

# Define the base URL
base_url = 'https://example.com/items?page='

# Function to fetch and parse a page
def fetch_page(page_number):
    url = f"{base_url}{page_number}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve page {page_number}")
        return None

# Function to extract data from a page
def extract_data(soup):
    items = []
    # Assuming items are contained within <div class="item">
    item_elements = soup.find_all('div', class_='item')
    
    for item in item_elements:
        # Extract relevant data
        title = item.find('h2').text
        description = item.find('p').text
        items.append({'title': title, 'description': description})
    
    return items

# Fetch and parse data from multiple pages
all_items = []
page_number = 1

while True:
    soup = fetch_page(page_number)
    if soup:
        items = extract_data(soup)
        if items:
            all_items.extend(items)
            page_number += 1
        else:
            # No more items found, break the loop
            break
    else:
        # Failed to retrieve page, break the loop
        break

# Print the extracted data
for item in all_items:
    print(item)
```

In this example:
- We define the `base_url` with a placeholder for the page number.
- The `fetch_page` function constructs the URL for each page, sends a GET request using `requests`, and parses the response with `BeautifulSoup`.
- The `extract_data` function extracts data from each page. In this case, it looks for `div` elements with the class `item`, and extracts the `title` and `description`.
- We use a `while` loop to fetch and parse each page until no more items are found or a request fails.

## Handling Infinite Scrolling

Infinite scrolling dynamically loads more content as the user scrolls down the page. This often involves sending AJAX requests to the server to fetch more data.

To handle infinite scrolling, you need to:
1. **Identify the AJAX Request:**
   Use browser developer tools to find the network request that loads additional content.
2. **Replicate the AJAX Request:**
   Use the `requests` library to replicate the AJAX request and fetch the additional content.

#### Example: Handling Infinite Scrolling

Suppose we identify that the website sends AJAX requests to `https://example.com/api/items?page=1` to load more items.

```python
import requests

# Define the base URL for the AJAX request
base_url = 'https://example.com/api/items?page='

# Function to fetch JSON data from an AJAX request
def fetch_ajax_page(page_number):
    url = f"{base_url}{page_number}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve page {page_number}")
        return None

# Function to extract data from JSON response
def extract_ajax_data(json_data):
    items = []
    for item in json_data['items']:
        # Extract relevant data
        title = item['title']
        description = item['description']
        items.append({'title': title, 'description': description})
    
    return items

# Fetch and parse data from multiple AJAX requests
all_items = []
page_number = 1

while True:
    json_data = fetch_ajax_page(page_number)
    if json_data:
        items = extract_ajax_data(json_data)
        if items:
            all_items.extend(items)
            page_number += 1
        else:
            # No more items found, break the loop
            break
    else:
        # Failed to retrieve page, break the loop
        break

# Print the extracted data
for item in all_items:
    print(item)
```

In this example:
- We identify the AJAX request URL and create the `base_url`.
- The `fetch_ajax_page` function sends a GET request to the AJAX URL, retrieves the JSON response, and checks for success.
- The `extract_ajax_data` function extracts data from the JSON response.
- We use a `while` loop to fetch and parse data from each AJAX request until no more items are found or a request fails.
