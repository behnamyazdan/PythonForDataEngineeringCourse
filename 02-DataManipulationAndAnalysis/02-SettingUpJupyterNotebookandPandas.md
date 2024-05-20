# Setting Up Jupyter Notebook and Pandas

To begin working with Jupyter Notebook and Pandas, you need to have Python installed on your system along with the necessary libraries. Follow these instructions to set up your environment.

### Step 1: Install Python

First, ensure that Python is installed on your computer. You can download and install Python from the official Python website: [python.org](https://www.python.org/downloads/). Make sure to download the latest version compatible with your operating system.

### Step 2: Install Jupyter Notebook and Pandas

You can install Jupyter Notebook and Pandas using `pip`, the Python package installer. Open your terminal or command prompt and execute the following commands:

1. **Install Jupyter Notebook:**

```bash
pip install jupyter
```

2. **Install Pandas:**

```bash
pip install pandas
```

Alternatively, you can install both Jupyter Notebook and Pandas as part of the Anaconda distribution, which includes many other useful data science libraries. You can download Anaconda from [anaconda.com](https://www.anaconda.com/products/individual).

### Step 3: Launch Jupyter Notebook

Once the installation is complete, you can launch Jupyter Notebook. Open your terminal or command prompt and type:

```bash
jupyter notebook
```

This command will start the Jupyter Notebook server and open a new tab in your default web browser. You will see the Jupyter Notebook dashboard, which displays the contents of the current directory.

also you can use `jupyter lab` by run this command:

```
jupyter lab
```

### Step 4: Create a New Notebook

In the Jupyter Notebook dashboard, follow these steps to create a new notebook:

1. Click the "New" button on the right side of the dashboard.
2. Select "Python 3" (or the version of Python you installed) from the dropdown menu.

A new notebook will open in a new tab. You can start writing and executing Python code in the cells of this notebook.

### Step 5: Import Pandas and Start Using It

Now that your Jupyter Notebook is set up, you can start using Pandas. In a new cell, type the following code to import Pandas and create a simple DataFrame:

```python
import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print(df)
```

Run the cell by pressing `Shift + Enter`. You should see the DataFrame displayed below the cell.

By following these instructions, you should be able to set up Jupyter Notebook and Pandas on your system and start working with these powerful tools for data analysis.