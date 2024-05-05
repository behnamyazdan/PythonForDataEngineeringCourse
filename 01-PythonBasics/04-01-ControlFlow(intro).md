# Control flow (if statements, loops)
Control flow statements, such as if statements and loops, are fundamental concepts in programming that allow you to control the flow of execution in your code based on certain conditions or iterate over sequences of data. Let's explore these concepts with an abstract real-world example:

---
### Control Flow: If Statements

If statements allow you to execute certain code blocks conditionally based on whether a specified condition evaluates to true or false.

Example:
```python
# Real-world scenario: Checking weather conditions before going outside
weather = "sunny"

if weather == "sunny":
    print("It's a beautiful day! Let's go for a walk.")
else:
    print("It's not sunny outside. Let's stay indoors.")
```

Explanation:
- In this example, the program checks the `weather` variable to determine if it's "sunny" or not.
- If the weather is "sunny", the program prints a message encouraging going for a walk.
- If the weather is not "sunny", the program prints a message suggesting staying indoors.

---
## Control Flow: Loops

Loops allow you to execute a block of code repeatedly, either for a specified number of times or until a certain condition is met.

Example:
```python
# Real-world scenario: Making multiple iterations through a to-do list
to_do_list = ["Read", "Exercise", "Study"]

# Using a for loop to iterate over each item in the to-do list
for task in to_do_list:
    print("I need to:", task)
```

Explanation:
- In this example, the program iterates over each item in the `to_do_list` using a for loop.
- For each iteration, the program prints a message indicating the task that needs to be done.

**Abstract Real-world Scenario: Planning a Trip**

Consider the following abstract real-world scenario: You are planning a trip, and you need to check various conditions and perform different actions based on those conditions.

```python
# Real-world scenario: Planning a trip based on weather and budget
weather = "sunny"
budget = 1000

if weather == "sunny":
    print("It's a beautiful day! Let's go for a hike.")
    budget -= 200  # Deduct hiking expenses from the budget
else:
    print("It's not sunny outside. Let's visit a museum.")
    budget -= 50   # Deduct museum entrance fee from the budget

# Using a while loop to plan additional activities until the budget runs out
activities = ["Visit beach", "Go shopping", "Have dinner"]
while budget > 0 and activities:
    activity = activities.pop(0)  # Get the next activity from the list
    print("Let's:", activity)
    if activity == "Visit beach":
        budget -= 100  # Deduct beach expenses from the budget
    elif activity == "Go shopping":
        budget -= 150  # Deduct shopping expenses from the budget
    elif activity == "Have dinner":
        budget -= 50   # Deduct dinner expenses from the budget

print("Remaining budget:", budget)
```

Explanation:
- In this example, the program plans a trip based on the weather and the available budget.
- It uses if statements to decide between hiking and visiting a museum based on the weather.
- It uses a while loop to plan additional activities (e.g., visiting the beach, shopping, having dinner) until the budget runs out.
- The program deducts expenses for each activity from the budget and prints the remaining budget at the end.

---

### Lists in Python:

In Python, a list is a versatile **data structure** used to store a collection of items. Lists are ordered, mutable (modifiable), and can contain elements of different data types. Lists are defined using square brackets `[ ]` and individual elements are separated by commas. Lists offer various methods for adding, removing, and manipulating elements.

For example:
```python
my_list = [1, 2, 3, "apple", "banana", True]
```

**In the next section, we'll delve deeper into lists, exploring their properties, methods, and common operations. We'll learn how to create and manipulate lists effectively to store and organize data in Python programs.**