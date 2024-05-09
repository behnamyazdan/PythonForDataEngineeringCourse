# Data Structures:

Data structures are fundamental concepts in computer science and programming that enable the organization, storage, and manipulation of data in a systematic and efficient manner. They provide a way to represent and manage collections of data elements, along with operations to **access**, **insert**, **delete**, and **modify** these elements.

In essence, data structures define the layout and relationships between data elements, allowing programmers to store and retrieve information quickly and effectively. Different data structures have distinct characteristics and are suited to specific tasks and use cases.

**Lists:**

- Lists are one of the most versatile and commonly used data structures in Python.

- They are <u>ordered collections of items</u>, allowing for easy indexing and slicing.

- Lists are mutable, meaning their elements can be modified after creation.

- Elements in a list can be of any data type, and a single list can contain a mix of different types.

- Lists are defined using square brackets `[]` and can be initialized with comma-separated values.

  **Example:**

  ```python
  my_list = [1, 2, 3, 'a', 'b', 'c']
  ```

  

**Tuples:**

- Tuples are similar to lists but are immutable, meaning their elements cannot be changed after creation.

- They are typically used to represent fixed sequences of elements, such as coordinates or database records.

- Tuples are defined using parentheses `()` and can be initialized with comma-separated values.

- Tuples support indexing and slicing operations like lists, but attempting to modify a tuple will result in an error.

  **Example:**

  ```python
  my_tuple = (1, 2, 3, 'a', 'b', 'c')
  ```

  

**Dictionaries:**

- Dictionaries are unordered collections of key-value pairs, providing fast lookup and retrieval of values based on keys.

- Keys in a dictionary must be unique and immutable, while values can be of any data type.

- Dictionaries are often used to represent mappings between unique identifiers (keys) and associated data (values).

- They are defined using curly braces `{}` and can be initialized with key-value pairs separated by colons `:` .

  **Example:**

  ```python
  my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
  ```

  

**Sets:**

- Sets are unordered collections of unique elements, allowing for efficient elimination of duplicate values.

- They are useful for performing set operations such as union, intersection, and difference.

- Sets are defined using curly braces `{}` and can be initialized with comma-separated values.

- Sets support various methods for adding, removing, and manipulating elements, making them suitable for tasks like filtering and deduplication.

  **Example:**

  ```python
  my_set = {1, 2, 3, 'a', 'b', 'c'}
  ```

### Operations on Data Structures:

- Common operations on lists include appending, inserting, removing, and slicing elements.
- Dictionaries support operations like accessing, adding, modifying, and deleting key-value pairs.
- Tuples are immutable, so operations like adding or removing elements are not possible. However, you can concatenate, slice, and unpack tuples.
- Sets support operations like adding, removing, and checking for membership. They also support set operations like union, intersection, and difference.

**1. Operations on Lists:**
```python
# Define a list
my_list = [1, 2, 3, 4, 5]

# Append an element
my_list.append(6)

# Insert an element at a specific index
my_list.insert(2, 10)

# Remove an element
my_list.remove(3)

# Access an element using indexing
print(my_list[0])  # Output: 1

# Slice the list
print(my_list[1:4])  # Output: [2, 10, 4]
```

**2. Operations on Dictionaries:**
```python
# Define a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Access a value using a key
print(my_dict['name'])  # Output: John

# Add a new key-value pair
my_dict['gender'] = 'Male'

# Modify a value
my_dict['age'] = 35

# Remove a key-value pair
del my_dict['city']

print(my_dict)  # Output: {'name': 'John', 'age': 35, 'gender': 'Male'}
```

**3. Operations on Tuples:**
```python
# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Concatenate two tuples
new_tuple = my_tuple + (6, 7)

# Access an element using indexing
print(my_tuple[0])  # Output: 1

# Slice the tuple
print(my_tuple[1:4])  # Output: (2, 3, 4)
```

**4. Operations on Sets:**
```python
# Define a set
my_set = {1, 2, 3, 4, 5}

# Add an element
my_set.add(6)

# Remove an element
my_set.remove(3)

# Check for membership
print(2 in my_set)  # Output: True

# Union of two sets
other_set = {4, 5, 6, 7}
union_set = my_set.union(other_set)

print(union_set)  # Output: {1, 2, 4, 5, 6, 7}
```

### Choosing the Right Data Structure:

- Lists are suitable for storing collections of items when the order matters, and elements may need to be modified.
- Dictionaries are ideal for representing mappings between unique identifiers (keys) and associated data (values).
- Tuples are preferred for fixed sequences of elements that should not change.
- Sets are useful for eliminating duplicate values and performing set operations efficiently.

Understanding these fundamental data structures is essential for effective Python programming. They provide versatile tools for organizing and manipulating data in a wide range of applications, from simple scripts to complex software systems.

---

## Optional reading topics

---

### Mutable vs Immutable

Understanding the concept of mutable and immutable data types is crucial for Python programmers. Let's break down these concepts with simple explanations and examples:

**Mutable:**

A mutable object is one whose value can be changed after it is created. This means you can modify the object's content without changing its identity. Common mutable data types in Python include lists, dictionaries, and sets.

**Example of Mutable Data Type (List):**
```python
# Define a list
my_list = [1, 2, 3, 4]

# Modify the list by appending a new element
my_list.append(5)

# The list has changed
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

In this example, we start with a list `[1, 2, 3, 4]`, and we modify it by appending the number `5` to the end. The list's content changes, but its identity as a list remains the same.

**Immutable:**

An immutable object is one whose value cannot be changed after it is created. Once an immutable object is created, its content cannot be modified. Common immutable data types in Python include integers, floats, strings, tuples, and frozensets.

**Example of Immutable Data Type (String):**
```python
# Define a string
my_string = "Hello From Python for Data engineering"

# Attempt to modify the string (which is not possible)
# This will raise an error
# my_string[0] = 'h'  # Uncommenting this line will raise a TypeError
```

In this example, we define a string `"Hello From Python for Data engineering"`. Strings in Python are immutable, so attempting to modify a character within the string (e.g., changing the first character to lowercase `'h'`) will result in a `TypeError`.

**Key Differences:**

- Mutable objects can be modified after creation, while immutable objects cannot.
- Mutable objects include lists, dictionaries, and sets, while immutable objects include integers, floats, strings, tuples, and frozensets.
- Immutable objects offer advantages like thread safety and potential performance optimizations, while mutable objects provide flexibility for modifying data in place.

Understanding mutable and immutable data types is essential for writing efficient and bug-free Python code. Knowing when to use each type can help optimize performance and prevent unexpected behavior in your programs.

