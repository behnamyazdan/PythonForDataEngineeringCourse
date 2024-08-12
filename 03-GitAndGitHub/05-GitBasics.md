# Git Basics

In this part, we will focus on basic Git operations that are essential for managing your code. We will start by creating some initial scripts for our ETL pipeline and then learn how to track changes using Git.

#### Script Development (Scenario Step 2)

To make this hands-on and practical, we'll start by developing Python scripts that are part of our ETL pipeline. This will involve writing scripts for data extraction, transformation, and loading.

1. **Creating Initial Python Scripts**:
   - **Data Extraction**:
     - Create a script named `extract.py` that reads data from a source, such as a CSV file or an API.
     ```python
     import pandas as pd
     
     def extract_data(file_path):
         return pd.read_csv(file_path)
     
     if __name__ == "__main__":
         data = extract_data('data/weather_data.csv')
         print(data.head())
     ```

   - **Data Transformation**:
     - Create a script named `transform.py` that cleans and transforms the extracted data.
     ```python
     import pandas as pd
     
     def transform_data(data):
         data['temperature_celsius'] = (data['temperature_fahrenheit'] - 32) * 5.0/9.0
         return data
     
     if __name__ == "__main__":
         data = pd.read_csv('data/weather_data.csv')
         transformed_data = transform_data(data)
         print(transformed_data.head())
     ```

   - **Data Loading**:
     - Create a script named `load.py` that loads the transformed data into a database.
     ```python
     import pandas as pd
     from sqlalchemy import create_engine
     
     def load_data(data, db_connection_string):
         engine = create_engine(db_connection_string)
         data.to_sql('weather', con=engine, if_exists='replace', index=False)
     
     if __name__ == "__main__":
         data = pd.read_csv('data/transformed_weather_data.csv')
         load_data(data, 'sqlite:///weather_data.db')
     ```

#### Understanding the Working Directory and Staging Area

Next, we will introduce key Git concepts: the working directory and the staging area.

1. **Working Directory**:
   - The working directory is the current state of your project files. It includes all the files in your project folder, whether they are tracked by Git or not.
   - Any changes you make to your files occur in the working directory. These changes are initially untracked by Git until you explicitly tell Git to track them.

2. **Staging Area (Index)**:
   - The staging area, also known as the index, is a space where you can prepare your changes before committing them to the repository.
   - Think of the staging area as a holding area for changes that you want to include in your next commit. This allows you to control exactly which changes are included in a commit.

#### Adding and Committing Changes

Now, let's add our newly created scripts to the staging area and commit them to the repository.

1. **Adding Changes to the Staging Area**:
   - Use the `git add` command to add files to the staging area.
     ```sh
     git add extract.py transform.py load.py
     ```
   - This command tells Git to start tracking these files and prepares them for committing.

2. **Committing Changes**:
   - Use the `git commit` command to save the changes from the staging area to the repository.
     ```sh
     git commit -m "Initial commit with extract, transform, and load scripts"
     ```
   - The `-m` flag allows you to include a commit message, which should describe the changes you are committing.

#### Viewing the Git History

Finally, let's view the commit history to see the changes we've made.

1. **Viewing Commit History**:
   - Use the `git log` command to see a log of all the commits made to the repository.
     ```sh
     git logs
     ```
   - This command shows a list of commits, including their commit hashes, author information, date, and commit messages. This history is crucial for tracking the development of your project over time.

### Summary

By the end of this session, you will have:
- Created initial scripts for data extraction, transformation, and loading.
- Understood the concepts of the working directory and the staging area.
- Learned how to add changes to the staging area and commit them to the repository.
- Viewed the commit history to track changes.

These foundational Git skills are essential for managing the code in your ETL pipeline project effectively.