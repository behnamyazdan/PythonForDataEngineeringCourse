# Parsing HTML with BeautifulSoup

BeautifulSoup is a popular Python library for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is essential for web scraping.

## Installation

To use BeautifulSoup, you need to install it along with a parser, such as `lxml` or `html.parser`.

```bash
pip install beautifulsoup4 lxml
```

## Basic Syntax and Methods of BeautifulSoup

To start parsing HTML with BeautifulSoup, you first need to import the library and load your HTML content. Here is a basic example:

```python
from bs4 import BeautifulSoup

# Example HTML content
html_content = """
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <h1>Welcome to the Example Page</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Visit Example.com</a>
  </body>
</html>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'lxml')

# Print the parsed HTML
print(soup.prettify())
```

**Output:**
```html
<html>
 <head>
  <title>
   Example Page
  </title>
 </head>
 <body>
  <h1>
   Welcome to the Example Page
  </h1>
  <p>
   This is a paragraph.
  </p>
  <a href="https://example.com">
   Visit Example.com
  </a>
 </body>
</html>
```

## Basic Methods of BeautifulSoup

BeautifulSoup provides several methods to navigate and search the parse tree. Here are some of the most common methods:

1. **Finding Tags:**

- `find()`: Finds the first occurrence of a tag.
- `find_all()`: Finds all occurrences of a tag.

**Example:**

```python
# Find the first <h1> tag
h1_tag = soup.find('h1')
print(h1_tag.text)  # Output: Welcome to the Example Page

# Find all <p> tags
p_tags = soup.find_all('p')
for p in p_tags:
    print(p.text)  # Output: This is a paragraph.
```

2. **Accessing Attributes:**

You can access the attributes of a tag using dictionary-like syntax.

**Example:**

```python
# Find the first <a> tag and get its href attribute
a_tag = soup.find('a')
print(a_tag['href'])  # Output: https://example.com
```

3. **Navigating the Parse Tree:**

- `parent`: Navigates to the parent of a tag.
- `children`: Iterates over a tag’s children.
- `descendants`: Iterates over all descendants of a tag.
- `next_sibling` and `previous_sibling`: Navigate between siblings.

**Example:**

```python
# Navigate to the parent of the <h1> tag
print(h1_tag.parent.name)  # Output: body

# Iterate over children of the <body> tag
for child in soup.body.children:
    print(child.name)

# Output:
# h1
# p
# a

# Get the next sibling of the <h1> tag
print(h1_tag.next_sibling.name)  # Output: p
```

## Extracting Data from HTML: Tags, Attributes, and Text

#### Extracting Text

To extract text from a tag, use the `.text` or `.get_text()` method.

**Example:**

```python
# Extract text from the <h1> tag
print(h1_tag.get_text())  # Output: Welcome to the Example Page
```

#### Extracting Attributes

Attributes of tags can be accessed like dictionary keys.

**Example:**

```python
# Extract the href attribute of the <a> tag
print(a_tag['href'])  # Output: https://example.com
```

#### Extracting Multiple Tags

Use `find_all()` to extract multiple tags.

**Example:**

```python
# Extract all paragraph texts
for p in soup.find_all('p'):
    print(p.get_text())  # Output: This is a paragraph.
```

### Example

Let's create a practical example where we parse a more complex HTML document and extract specific data.

**Example HTML Content:**

```html
<html>
  <head>
    <title>Sample Web Page</title>
  </head>
  <body>
    <div id="main">
      <h1>Article Title</h1>
      <p class="author">By John Doe</p>
      <p class="date">Published on June 8, 2024</p>
      <div class="content">
        <p>This is the first paragraph of the article.</p>
        <p>This is the second paragraph of the article.</p>
      </div>
      <a href="https://example.com/contact">Contact Us</a>
    </div>
  </body>
</html>
```

**Objective:** Extract the article title, author name, publication date, and the content paragraphs.

**Code:**

```python
from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
<html>
  <head>
    <title>Sample Web Page</title>
  </head>
  <body>
    <div id="main">
      <h1>Article Title</h1>
      <p class="author">By John Doe</p>
      <p class="date">Published on June 8, 2024</p>
      <div class="content">
        <p>This is the first paragraph of the article.</p>
        <p>This is the second paragraph of the article.</p>
      </div>
      <a href="https://example.com/contact">Contact Us</a>
    </div>
  </body>
</html>
"""

# Parse the HTML content
soup = BeautifulSoup(html_content, 'lxml')

# Extract the article title
title = soup.find('h1').get_text()
print(f"Title: {title}")

# Extract the author name
author = soup.find('p', class_='author').get_text()
print(f"Author: {author}")

# Extract the publication date
date = soup.find('p', class_='date').get_text()
print(f"Date: {date}")

# Extract the content paragraphs
content_div = soup.find('div', class_='content')
content_paragraphs = content_div.find_all('p')
for i, paragraph in enumerate(content_paragraphs, start=1):
    print(f"Paragraph {i}: {paragraph.get_text()}")

# Extract the contact link
contact_link = soup.find('a')['href']
print(f"Contact Link: {contact_link}")
```

**Output:**

```
Title: Article Title
Author: By John Doe
Date: Published on June 8, 2024
Paragraph 1: This is the first paragraph of the article.
Paragraph 2: This is the second paragraph of the article.
Contact Link: https://example.com/contact
```

### Summary

BeautifulSoup is a powerful and easy-to-use library for parsing HTML and XML documents in Python. It provides methods to navigate, search, and modify the parse tree, making it an essential tool for web scraping. Understanding how to extract data from HTML tags, attributes, and text allows you to gather information efficiently from web pages.