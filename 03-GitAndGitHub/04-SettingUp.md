# Setting Up

Setting up Git and GitHub is the first step to start working on your ETL pipeline project collaboratively. In this section, we will ensure everyone has the necessary tools installed, configure Git, and create the initial repository for our project.

#### Prerequisites

Before we dive into using Git and GitHub, let's make sure everyone has the required tools installed:

1. **GitHub Account**:
   - Make sure each participant has a GitHub account. If anyone doesn't have one, they can sign up at [GitHub](https://github.com/).

2. **Git Installation**:
   - Ensure that Git is installed on everyone’s local machine. Git can be downloaded from [Git SCM](https://git-scm.com/downloads). 
   - Provide installation resources or assist participants with the installation process if needed.

#### Git Configuration

Once Git is installed, we need to configure it with your personal information. This configuration is necessary because Git attaches this information to every commit you make.

1. **Setting Up Username and Email**:
   - Open your terminal or command prompt.
   - Set your username and email address with the following commands:
     ```sh
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```
   - Replace `"Your Name"` and `"your.email@example.com"` with your actual name and email address.
   - These settings ensure that your commits are properly attributed to you.

#### Creating a Local Repository (Scenario Step 1)

Now that Git is configured, let's create a local repository for our ETL pipeline project. A Git repository is a storage space where your project’s files and their history are kept.

1. **Initialize a Local Git Repository**:
   
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to create your project folder.
   - Use the following command to initialize a new Git repository:
     ```sh
     git init etl-pipeline
     ```
   - This command creates a new directory named `etl-pipeline` and sets it up as a Git repository. If you prefer to initialize Git in an existing directory, navigate to that directory and run `git init`.
   
2. **Explanation of a Repository**:
   - A **repository** (or "repo" for short) is a virtual storage of your project. It allows you to save versions of your code, which you can access when needed.
   - Every time you make changes to your project, you can commit those changes to the repository, creating a history of all changes made over time.
   - This history is invaluable for tracking progress, identifying when and why changes were made, and collaborating with others.

### Recap

By the end of this setup section, you will have:
- A GitHub account.
- Git installed and configured with their personal information.
- A local Git repository initialized for the ETL pipeline project.

Now we are ready to start adding files to our repository, committing changes, and pushing them to GitHub for collaborative development.