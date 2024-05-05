# Control flow concepts in Python:

---
### Example 1: Conditional Statement

```python
# Example 1: Conditional Statement
# Check if a number is positive, negative, or zero

num = int(input("Enter a number: "))  # Take user input

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

**Explanation:**
- This program prompts the user to enter a number using the `input()` method and converts the input to an integer using `int()`.
- The `if`, `elif`, and `else` statements are used to check whether the number is positive, negative, or zero, respectively.
- Depending on the value of the input number, the corresponding message is printed.

---

### Example 2: Looping with a Condition

```python
# Example 2: Looping with a Condition
# Print all even numbers between 1 and 20 using a while loop

num = 1  # Initialize num to start from 1

while num <= 20:  # Loop until num reaches 20
    if num % 2 == 0:  # Check if num is even
        print(num)
    num += 1  # Increment num for the next iteration
```

**Explanation:**
- In this example, we use a `while` loop to iterate over numbers from 1 to 20.
- Within the loop, we use an `if` statement to check if the current number (`num`) is even by checking if the remainder of dividing `num` by 2 is zero (`num % 2 == 0`).
- If the condition is true, we print the current number.
- Finally, we increment `num` by 1 to move to the next number.

---

### Example 3: Nested Loops

```python
# Example 3: Nested Loops
# Print a pattern of stars in a right-angled triangle

rows = 5  # Define the number of rows in the triangle

for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(i):  # Inner loop for each row
        print("*", end=" ")  # Print stars without newline
    print()  # Move to the next line for the next row
```

**Explanation:**
- This example demonstrates the usage of nested loops to print a right-angled triangle pattern of stars.
- The outer loop (`for i in range(1, rows + 1)`) iterates over the rows of the triangle, from 1 to the specified number of rows (`rows`).
- Inside the outer loop, the inner loop (`for j in range(i)`) iterates over each row, printing the required number of stars (`*`) based on the current row number (`i`).
- After printing the stars for each row, the `print()` statement with no arguments is used to move to the next line, creating a newline for the next row of stars.

---
### Example 4: Using `break` in a Loop

```python
# Example 4: Using `break` in a Loop
# Find the smallest factor of a given number

num = int(input("Enter a number: "))  # Take user input

for i in range(2, num + 1):  # Iterate from 2 to the given number
    if num % i == 0:  # Check if i is a factor of the given number
        print("Smallest factor of", num, "is", i)
        break  # Exit the loop after finding the smallest factor
```

**Explanation:**
- This example finds the smallest factor of a given number entered by the user.
- The `for` loop iterates from 2 to the given number (`num`) using the `range()` function.
- Inside the loop, the `if` statement checks if the current number (`i`) is a factor of the given number (`num`) by checking if the remainder of dividing `num` by `i` is zero (`num % i == 0`).
- If a factor is found, the program prints the smallest factor and then exits the loop using the `break` statement, as we only need to find the smallest factor.

---

### Example 5: Using `continue` in a Loop

```python
# Example 5: Using `continue` in a Loop
# Print all numbers from 1 to 10 except multiples of 3

for i in range(1, 11):  # Iterate over numbers from 1 to 10
    if i % 3 == 0:  # Check if the current number is a multiple of 3
        continue  # Skip the rest of the loop for multiples of 3
    print(i)  # Print the current number if it's not a multiple of 3
```

**Explanation:**
- This example prints all numbers from 1 to 10 except multiples of 3.
- The `for` loop iterates over numbers from 1 to 10 using the `range()` function.
- Inside the loop, the `if` statement checks if the current number (`i`) is a multiple of 3 by checking if the remainder of dividing `i` by 3 is zero (`i % 3 == 0`).
- If the current number is a multiple of 3, the `continue` statement is executed, causing the loop to skip the rest of the code block for that iteration and move to the next iteration.
- If the current number is not a multiple of 3, it is printed using the `print()` statement.

---

### Example 6: Using `else` with Loops

```python
# Example 6: Using `else` with Loops
# Check if a number is prime

num = int(input("Enter a number: "))  # Take user input
is_prime = True  # Assume the number is prime initially

if num <= 1:  # Check if the number is less than or equal to 1
    is_prime = False  # Numbers less than or equal to 1 are not prime
else:
    for i in range(2, int(num ** 0.5) + 1):  # Iterate from 2 to square root of the number
        if num % i == 0:  # Check if the number is divisible by any number in this range
            is_prime = False  # If divisible, the number is not prime
            break  # Exit the loop if a divisor is found
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
```

**Explanation:**
- This example checks if a given number entered by the user is prime.
- We initially assume the number is prime (`is_prime = True`).
- If the number is less than or equal to 1, it's not prime (`is_prime = False`).
- Otherwise, we iterate from 2 to the square root of the number and check if the number is divisible by any number in this range.
- If the number is divisible by any number in this range, it's not prime, and we set `is_prime` to `False`.
- The `else` block is executed if the loop completes without finding any divisors, indicating that the number is prime.

---
### Example 7: Using `pass` Statement

```python
# Example 7: Using `pass` Statement
# Print numbers from 1 to 5 and skip number 3 without any action

for i in range(1, 6):  # Iterate over numbers from 1 to 5
    if i == 3:  # Check if the current number is 3
        pass  # Skip number 3 without any action
    else:
        print(i)  # Print the current number if it's not 3
```

**Explanation:**
- This example prints numbers from 1 to 5 but skips number 3 without performing any action.
- Inside the `for` loop, the `if` statement checks if the current number (`i`) is 3.
- If the current number is 3, the `pass` statement is executed, which means no action is taken for that iteration, and the loop moves to the next iteration.
- If the current number is not 3, it is printed using the `print()` statement.

---
### Example 8: Using `enumerate()` with Loops (without data structures)

```python
# Example 8: Using `enumerate()` with Loops (without data structures)
# Print the index and value of each element in a sequence

fruits = "apple", "banana", "cherry", "date"  # Define a sequence of fruits

index = 0  # Initialize index to 0

for fruit in fruits:  # Iterate over the sequence of fruits
    print("Index:", index, " - Fruit:", fruit)  # Print the index and value
    index += 1  # Increment index for the next iteration
```

**Explanation:**
- This example represents a sequence of fruits.
- We initialize the `index` variable to 0 before starting the loop.
- The `for` loop iterates over each element in the sequence `fruits`.
- Inside the loop, we print the current index (`index`) and value (`fruit`) of each element.
- After printing, we increment the `index` variable to prepare it for the next iteration.

---

### Example 9: Using `while` Loop to Generate Fibonacci Sequence

```python
# Example 9: Using `while` Loop to Generate Fibonacci Sequence
# Generate the Fibonacci sequence up to a specified limit

limit = 20  # Define the limit for the Fibonacci sequence
prev, curr = 0, 1  # Initialize the first two Fibonacci numbers

while prev <= limit:  # Continue until the previous Fibonacci number exceeds the limit
    print(prev, end=" ")  # Print the current Fibonacci number
    prev, curr = curr, prev + curr  # Update the Fibonacci numbers for the next iteration
```

**Explanation:**
- This example demonstrates how to use a `while` loop to generate the Fibonacci sequence up to a specified limit.
- We define a variable `limit` to specify the upper limit for the sequence.
- We initialize two variables `prev` and `curr` to represent the first two Fibonacci numbers (0 and 1).
- The `while` loop continues until the value of `prev` (the previous Fibonacci number) exceeds the specified `limit`.
- Inside the loop, we print the current Fibonacci number (`prev`) using `print()` with the `end` parameter set to space to print numbers horizontally.
- We then update the values of `prev` and `curr` to generate the next Fibonacci number in the sequence.

---
### Example 10: Using `if` Statement to Check Leap Year

```python
# Example 10: Using `if` Statement to Check Leap Year
# Check if a given year is a leap year

year = 2024  # Define the year to be checked

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Check leap year conditions
    print(year, "is a leap year.")  # Print message if the year is a leap year
else:
    print(year, "is not a leap year.")  # Print message if the year is not a leap year
```

**Explanation:**
- This example demonstrates how to use an `if` statement to check if a given year is a leap year.
- We define a variable `year` representing the year to be checked.
- The `if` statement checks two conditions to determine if the year is a leap year:
  - The year must be divisible by 4 but not divisible by 100 (unless it is also divisible by 400).
- If the conditions are met, the program prints a message indicating that the year is a leap year. Otherwise, it prints a message indicating that the year is not a leap year.

---

### Example 11: Putt all together (Text-Based Game) 

**Overview:**
- The game is a text-based adventure where the player navigates through a series of rooms in search of a treasure chest.
- Along the way, the player may encounter locked doors, traps, and hidden items.
- The goal is to reach the final room, find the treasure chest, and win the game.

**Explanation:**

1. **Initialization:**
   - The game starts by welcoming the player and initializing the player's position to the first room (room 1).
   - An empty inventory is also initialized to store items found during exploration.

2. **Game Loop:**
   - The game runs in a loop (`while True`) until the player wins, encounters a trap, or quits.
   - Each iteration of the loop represents the player's actions in a single room.

3. **Room Navigation:**
   - The player is presented with options to navigate north (`N`) or south (`S`) in each room.
   - In the first room, the player encounters a locked door to the north and must find a key to unlock it.

4. **Special Events:**
   - Special events occur in each room, such as encountering traps or finding items.
   - Traps have a chance of appearing in rooms other than the first and last, adding an element of risk to exploration.
   - Items such as keys, potions, or coins can be found while searching the room.

5. **Inventory System:**
   - The player's inventory keeps track of items found during exploration.
   - Items found in rooms are added to the inventory for later use.

6. **Game Outcome:**
   - If the player reaches the final room, they find the treasure chest and win the game.
   - If the player encounters a trap, the game ends in defeat.
   - The player can choose to quit the game at any time.

**Purpose:**
- The game provides an interactive and engaging experience for players who enjoy exploration and decision-making.
- It demonstrates various programming concepts such as loops, conditional statements, user input handling, randomization, and inventory management.

**Conclusion:**
- The Enhanced Text-Based Adventure Game with Inventory System offers an entertaining gameplay experience with room navigation, special events, and inventory management mechanics.
- Players can enjoy the challenge of navigating through rooms, avoiding traps, and collecting items on their quest to find the treasure chest and win the game.



```python
import random

# Constants
ROOMS = 5  # Number of rooms in the game

# Main program
print("Welcome to the Text-Based Adventure Game!")

# Initialize player's position and inventory
player_position = 1
inventory = []

# Game loop
while True:
    print("\nYou are in room", player_position)

    # Check for special events in each room
    if player_position == 1:
        print("You see a locked door to the north.")
        direction = input("Which direction will you go? (N/S): ").upper()
        if direction == 'N':
            print("The door is locked! Find the key to unlock it.")
        elif direction == 'S':
            player_position += 1
        else:
            print("Invalid direction! Please enter 'N' or 'S'.")

    elif player_position == ROOMS:
        print("You found the treasure chest! You win!")
        break

    else:
        # Random chance of encountering an obstacle
        obstacle_chance = random.randint(1, 5)
        if obstacle_chance == 1:
            print("Oh no! You encountered a trap!")
            print("Game Over!")
            break

        direction = input("Which direction will you go? (N/S): ").upper()
        if direction == 'N':
            player_position -= 1
        elif direction == 'S':
            player_position += 1
        else:
            print("Invalid direction! Please enter 'N' or 'S'.")

        # Nested loop for searching the room
        search_attempts = 3
        for _ in range(search_attempts):
            print("Searching the room...")
            found_item = random.choice(['key', 'potion', 'coin', None])
            if found_item:
                print("You found a", found_item + "!")
                inventory.append(found_item)
                break
            else:
                print("Nothing found.")

print("Thank you for playing the Text-Based Adventure Game!")
```

#### Example Explanation:

```python
import random

# Constants
ROOMS = 5  # Number of rooms in the game

# Main program
print("Welcome to the Text-Based Adventure Game!")

# Initialize player's position and inventory
player_position = 1
inventory = []
```

**Explanation:**
- The program begins with importing the `random` module for generating random numbers.
- A constant `ROOMS` is defined to represent the number of rooms in the game.
- The main program starts with a welcome message and initializes the player's starting position (`player_position`) to 1 and an empty inventory (`inventory`).

```python
# Game loop
while True:
    print("\nYou are in room", player_position)

    # Check for special events in each room
    if player_position == 1:
        print("You see a locked door to the north.")
        direction = input("Which direction will you go? (N/S): ").upper()
        if direction == 'N':
            print("The door is locked! Find the key to unlock it.")
        elif direction == 'S':
            player_position += 1
        else:
            print("Invalid direction! Please enter 'N' or 'S'.")
```

**Explanation:**
- The game loop continues indefinitely (`while True`) until the player wins or encounters a trap.
- In each iteration of the loop, the player's current room is displayed.
- Special events are checked for each room. In room 1, the player encounters a locked door to the north. The player can choose to go south (`S`) to move to the next room.

```python
    elif player_position == ROOMS:
        print("You found the treasure chest! You win!")
        break
```

**Explanation:**
- If the player reaches the last room (`ROOMS`), they find the treasure chest and win the game. The loop is terminated using `break`.

```python
    else:
        # Random chance of encountering an obstacle
        obstacle_chance = random.randint(1, 5)
        if obstacle_chance == 1:
            print("Oh no! You encountered a trap!")
            print("Game Over!")
            break

        direction = input("Which direction will you go? (N/S): ").upper()
        if direction == 'N':
            player_position -= 1
        elif direction == 'S':
            player_position += 1
        else:
            print("Invalid direction! Please enter 'N' or 'S'.")
```

**Explanation:**
- For rooms other than the first and last, there's a chance of encountering a trap (1 in 5). If the player encounters a trap, the game ends.
- The player is prompted to choose a direction (`N` or `S`) to move to the previous or next room based on their input.

```python
        # Nested loop for searching the room
        search_attempts = 3
        for _ in range(search_attempts):
            print("Searching the room...")
            found_item = random.choice(['key', 'potion', 'coin', None])
            if found_item:
                print("You found a", found_item + "!")
                inventory.append(found_item)
                break
            else:
                print("Nothing found.")
```

**Explanation:**
- A nested loop is used to simulate searching the room multiple times (`search_attempts`) before finding an item.
- In each attempt, a random item (or None) is generated. If an item is found, it's added to the player's inventory (`inventory`) and the loop breaks.

```python
print("Thank you for playing the Text-Based Adventure Game!")
```

**Explanation:**
- Once the game loop is exited (either by winning, encountering a trap, or quitting), a thank-you message is displayed, and the program terminates.

This text-based adventure game includes room navigation, special events, inventory management, and randomization, providing an engaging gameplay experience.