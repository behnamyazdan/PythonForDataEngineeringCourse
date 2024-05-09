## Python Basics Assignment

The purpose of these assignments is to review all the fundamental concepts you've learned thus far. Some tasks may pose a challenge for beginners, but don't worry—you can ask questions in the course group, and I'll respond to you as soon as possible.

Remember:

- Start simple and gradually add complexity.
- Focus on understanding the core concepts and don't be afraid to experiment.

**Note for Intermediate and Advanced Participants:** Please approach this project only through the concepts discussed in this section. Avoid adding any features that go beyond the scope of the topics covered in this section.

**Good luck, and happy coding!**

---



### 1- To-Do List Application

**Objective:**

The goal of this project is to develop a simple to-do list app in Python. This project will help you improve your understanding of Python fundamentals such as data types,data structure, control flow, functions, and error handling.

**Requirements**:

1. **Add Tasks:** Users should be able to add tasks to their todo list.
2. **View Tasks:** Users should be able to view all the tasks in their todo list.
3. **Mark Tasks as Done:** Users should be able to mark tasks as done once they are completed.
4. **Delete Tasks:** Users should be able to delete tasks from the todo list.
5. **(optional) Save and Load Tasks:** Implement functionality to save the todo list to a file and load it back when the app is reopened. this step is optional.

**Expectations**:

- Utilize basic data types such as lists and strings to store tasks.
- Choose the right data structure to use.
- Implement control flow with if statements and loops to handle user interactions.
- Define functions to modularize the code and improve readability.
- Use error handling with try-except blocks to manage unexpected inputs or file operations.
- Ensure the app is user-friendly and intuitive to use.
- Break down the project into smaller tasks and tackle them one at a time.
- Test your app thoroughly to ensure it works as expected in different scenarios.



### 2- Movie Recommendation System

**Objective:**

Get ready to create your own movie recommender! In this project, you'll build a basic Python program that suggests movies based on a user's preferred genre. This project is a great way to practice essential Python skills like working with data, taking user input, and using control flow statements.

**Requirements:**

Your mission is to code a simple movie recommendation system. The program will:

1. **Store movie** : save information (title, genre, year) in a data structure.
2. **View Tasks:** Users should be able to view all the movies, groped and sorted in their gene.
3. **Interact with Users:**  Ask the user for their favorite genre.
4. **Search and Recommend movies:** Search through the movie data and recommend movies that match the user's preferred genre.

**Expectations:**

- Create a Python program that fulfills the objective.
- Use clear variable names and comments to explain your code.
- Test your program with different user inputs to ensure it works correctly.

**Challenge (Optional):**

- Enhance your program by allowing users to choose multiple genres for broader recommendations.



### 3- Fill-in-the-Blank Text(String Manipulation Focus)

**Objective:**

This assignment challenges you to showcase your string manipulation skills in Python by building a Fill-in-the-Blank text generator. In this project users provide different words (nouns, verbs, adjectives, etc.), and the program incorporates them into a predefined text template, creating a humorous or silly outcome.

- Create a Python program that generates a text.
- The program should:
  - Prompt the user for various words (e.g., noun, verb, adjective, adverb).
  - Store these words in variables.
  - Utilize string formatting techniques (f-strings) to insert the user's words into a pre-written story template.
  - Display the completed story for the user's entertainment.

**Requirements:**

- String Manipulation techniques (slicing, concatenation, f-strings)
- User input using `input()` function
- Basic understanding of variables and data types

**Expectations:**

- Create a well-structured and commented program.
- Design a funny or engaging story template.
- Ensure proper string manipulation to integrate user-provided words seamlessly.
- Test your program with different word choices to verify it works correctly.

**Challenge (Optional):**

- Enhance your program with additional features:
  - Allow users to choose from different story templates.
  - Categorize word prompts (e.g., noun types, specific adjectives).
  - Implement basic error handling for invalid user input (e.g., entering numbers instead of words).

**Help:**

1. **Text Template:**

   - create a text template with placeholders for various words. for example:
     ```
     Yesterday, I woke up feeling very [adjective].  
     I decided to make myself a delicious breakfast of [noun] and [noun].  
     While I was eating, a [noun] flew right by my window!  
     I chased it outside as fast as my [body part] could go,  
     but it disappeared into the [place].  
     The rest of the day was pretty uneventful, but it was definitely an [adjective] morning!
     ```

2. **User Input:**

   - Employ `input()` to prompt the user for different word categories (e.g., "Enter an adjective: ").
   - Store each user-provided word in a separate variable (use a data structure).

3. **String Manipulation:**

   - Utilize string manipulation techniques like slicing and concatenation to incorporate user words into the story template.
   - Employ f-strings (formatted string literals) within the template to embed user words seamlessly.

4. **Output:**

   - Use `print()` statements to display the completed text for the user to enjoy.