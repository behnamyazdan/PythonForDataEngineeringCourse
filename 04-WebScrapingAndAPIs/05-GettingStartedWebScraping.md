# Getting Started with Web Scraping Using Python



## Introduction to Web Scraping

Web scraping involves extracting data from websites. This can be useful for various purposes such as data analysis, research, and automation. The process typically involves fetching web pages and extracting specific pieces of information from them.

## Setting Up Your Environment

Before you start web scraping, you need to set up your Python environment with the necessary libraries.

1. **Install Python:**
   - Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. **Install Required Libraries:**
   - Use `pip` to install the libraries needed for web scraping.
     ```sh
     pip install requests
     pip install beautifulsoup4
     ```

## Using Requests to Fetch Web Pages

The `requests` library is a simple and elegant HTTP library for Python. It allows you to send HTTP requests and handle responses.

1. **Making a GET Request:**
   ```python
   import requests
   
   url = 'https://jobinja.ir/'
   response = requests.get(url)
   
   if response.status_code == 200:
       print('Page fetched successfully!')
       print(response.content)  # Print the raw HTML content
   else:
       print('Failed to fetch the page.')
   ```

2. **Handling Response Content:**
   - The `response.content` attribute contains the raw bytes of the page content.
   - The `response.text` attribute contains the content as a string.

## Parsing HTML with BeautifulSoup

BeautifulSoup is a library that makes it easy to scrape information from web pages. It creates a parse tree for parsed pages that can be used to extract data.

1. **Creating a BeautifulSoup Object:**
   ```python
   from bs4 import BeautifulSoup
   
   html_content = response.content
   soup = BeautifulSoup(html_content, 'html.parser')
   ```

2. **Finding Elements:**
   - **Finding by Tag Name:**
     ```python
     title_tag = soup.find('title')
     print(title_tag.text)
     ```
   - **Finding by Class Name:**
     ```python
     div = soup.find('p', class_='intro')
     print(div.text)
     ```

3. **Finding Multiple Elements:**
   - **Finding All Paragraphs:**
     ```python
     paragraphs = soup.find_all('p')
     for p in paragraphs:
         print(p.text)
     ```
