# Branching and Merging for Feature Development (Scenario Step 5)

In this section, we will introduce the concept of branches and how they facilitate independent development in a project. Branching is a powerful feature of Git that allows multiple developers to work on different parts of a project simultaneously without interfering with each other's work. This is particularly useful in data engineering projects, such as our ETL pipeline, where different team members might be working on various stages of the pipeline or integrating new data sources.

#### Introduction to Branches

**What is a Branch?**

A branch in Git is essentially a separate line of development. By default, Git starts with a branch named `master` (or `main` in newer versions). Creating a new branch allows you to diverge from the main line of development and work on changes independently. This means you can develop features, fix bugs, or experiment with new ideas without affecting the stable version of your project.

**Benefits of Branching:**

- **Isolation of Work**: Each branch can encapsulate changes independently, making it easier to manage and test different features or fixes.
- **Parallel Development**: Multiple team members can work on different branches simultaneously, enhancing productivity and reducing bottlenecks.
- **Experimentation**: Branches provide a safe space to try out new ideas or perform risky changes without impacting the main project.

#### Creating and Using Branches

1. **Creating a New Branch**:
   - To create a new branch, use the `git branch` command followed by the branch name:
     ```sh
     git branch <branch-name>
     ```
     This command creates a new branch called `feature-branch` but does not switch to it.

2. **Switching to a Branch**:
   - To switch to the newly created branch, use the `git checkout` command:
     ```sh
     git checkout <branch-name>
     ```
     Alternatively, you can create and switch to a new branch in one command using:
     ```sh
     git checkout -b <branch-name>
     ```
     This command both creates the branch and switches to it.

3. **Making Changes**:
   - Once you are on the new branch, any changes you make (such as modifying files, adding new code, or making commits) will only affect this branch. This allows you to work on a specific feature or fix without disturbing the main codebase.

4. **Committing Changes**:
   - After making changes, stage and commit them as usual:
     ```sh
     git add .
     git commit -m "Implemented feature X"
     ```

#### Merging Branches

Once you have completed the work on your feature branch and tested it, you can merge these changes back into the main branch (typically `master` or `main`). Merging incorporates the changes from one branch into another.

1. **Switch to the Main Branch**:
   - First, switch back to the main branch:
     ```sh
     git checkout main
     ```
   
2. **Merge the Feature Branch**:
   - Use the `git merge` command to merge the feature branch into the main branch:
     ```sh
     git merge <branch-name>
     ```
     This command integrates the changes from `feature-branch` into the current branch (in this case, `master`).

3. **Resolving Conflicts**:
   - Sometimes, conflicts can arise if the same parts of files were modified in both branches. Git will highlight these conflicts, and you will need to resolve them manually before completing the merge.
   - After resolving conflicts, mark them as resolved by adding the resolved files:
     ```sh
     git add <file>
     ```
     Then commit the merge:
     ```sh
     git commit
     ```

#### Example Scenario: Adding a New Data Source

Imagine we need to integrate a new data source into our ETL pipeline. Here’s how we could use branching and merging:

1. **Create a Branch for the New Data Source**:
   ```sh
   git checkout -b add-new-data-source
   ```

2. **Develop the Integration**:
   - Write the code to extract data from the new source, transform it, and load it into the database.

3. **Commit the Changes**:
   ```sh
   git add .
   git commit -m "Added integration for new data source"
   ```

4. **Merge the Changes into the Main Branch**:
   - Switch to the main branch:
     ```sh
     git checkout main
     ```
   - Merge the feature branch:
     ```sh
     git merge add-new-data-source
     ```

### Creating a New Branch for a Specific Data Source Integration

This hands-on exercise will demonstrate how to isolate changes in a dedicated branch, allowing for focused development and easier collaboration.

#### Step-by-Step Guide

1. **Navigate to Your Local Repository**:
   - Open your terminal or command prompt.
   - Navigate to the directory of your local repository. For example:
     ```sh
     cd path/to/etl-pipeline
     ```

2. **Create a New Branch**:
   - To create a new branch specifically for adding a new data transformation, use the `git branch` command followed by the branch name. Here, we’ll name the branch `feature/data-transformation`:
     ```sh
     git branch feature/data-transformation
     ```
   - This command creates a new branch called `feature/data-transformation`.

3. **Switch to the New Branch**:
   - After creating the branch, switch to it using the `git checkout` command:
     ```sh
     git checkout feature/data-transformation
     ```
   - You can also create and switch to the new branch in one step with:
     ```sh
     git checkout -b feature/data-transformation
     ```

4. **Verify the Branch Switch**:
   - To confirm that you have successfully switched to the new branch, use the `git branch` command to list all branches. The current branch will be highlighted with an asterisk (*):
     ```sh
     git branch
     ```
   - The output should look something like this:
     ```
     * feature/data-transformation
       master
     ```

5. **Make Changes on the New Branch**:
   - Now that you are on the `feature/data-transformation` branch, any changes you make will be isolated to this branch.
   - Create or modify your Python script for the new data transformation. For example, create a new file named `data_transformation.py` and add your transformation code using libraries like Pandas:
     ```python
     import pandas as pd
     
     def transform_data(df):
         # Example transformation: adding a new column
         df['new_column'] = df['existing_column'] * 2
         return df
     
     # Load data
     data = pd.read_csv('data.csv')
     
     # Transform data
     transformed_data = transform_data(data)
     
     # Save transformed data
     transformed_data.to_csv('transformed_data.csv', index=False)
     ```

6. **Stage and Commit Your Changes**:
   - Stage the changes you’ve made using the `git add` command:
     ```sh
     git add data_transformation.py
     ```
   - Commit the changes with a descriptive message:
     ```sh
     git commit -m "Added new data transformation script for feature/data-transformation"
     ```

#### Explanation of the Commands

- **Creating a Branch** (`git branch feature/data-transformation`):
  - This command creates a new branch named `feature/data-transformation`. A branch is essentially a pointer to a commit, allowing you to work on a separate line of development.
  
- **Switching to a Branch** (`git checkout feature/data-transformation`):
  - This command switches your working directory to the specified branch. All subsequent changes and commits will be made on this branch.
  - The combined command `git checkout -b feature/data-transformation` both creates and switches to the new branch in one step.

- **Staging Changes** (`git add data_transformation.py`):
  - The `git add` command stages the specified files, preparing them to be included in the next commit. Staging is a crucial step that allows you to review changes before committing them.

- **Committing Changes** (`git commit -m "Added new data transformation script for feature/data-transformation"`):
  - The `git commit` command records the changes to the repository. The `-m` flag allows you to add a commit message inline, describing what changes were made and why.

### Summary

By creating a new branch and making changes within it, you can work on specific features or fixes in isolation, ensuring that the main project remains stable. This approach is essential for collaborative projects, as it allows multiple team members to work on different tasks simultaneously without interfering with each other’s work. Following this step-by-step guide, you have learned how to create and switch to a new branch, make changes, and commit those changes, all within the context of developing a new data transformation for your ETL pipeline.