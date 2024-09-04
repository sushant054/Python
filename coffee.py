#Basic Data Inspection 
# a. Load the dataset and display the first 10 rows.
# b. How many rows and columns are present in the dataset?
# c. What are the data types of each column?

# Handling Missing Data 
# a. Identify the columns with missing data and their respective counts.
# b. For columns with more than 20% missing values, suggest a method to handle them and implement it.

# Summary Statistics 
# a. Generate summary statistics (mean, median, mode, etc.) for numerical columns (such as expertise, coffee_a_bitterness, and coffee_a_acidity).
# b. How does the bitterness preference (coffee_a_bitterness) vary across different age groups? Provide a brief analysis.


import pandas as pd
file_path = "coffee_survey.csv"  # Ensure this path is correct for your local setup
data = pd.read_csv(file_path)
#display the first 10 rows
print("First 10 rows of the dataset:")
print(data.head(10))
print("\n")
# no. of rows and columns
print(f"Number of rows and columns: {data.shape}")
print("\n")
# Data types of each column
print("Data types of each column:")
print(data.dtypes)
print("\n")
# Identify columns with missing data and their counts
missing_data = data.isnull().sum()
print("Columns with missing data and their counts:")
print(missing_data[missing_data > 0])
print("\n")
# Calculate the percentage of missing data for each column
missing_percentage = (missing_data / len(data)) * 100

# Identify columns with more than 20% missing data
columns_to_handle = missing_percentage[missing_percentage > 20].index
print("Columns with more than 20% missing data:")
print(columns_to_handle)
print("\n")

# Example of handling missing data: Drop columns with more than 20% missing values
data_cleaned = data.drop(columns=columns_to_handle)
print("Dataset after dropping columns with more than 20% missing values:")
print(data_cleaned.head(10))
print("\n")

# Summary...
# Generate summary statistics for numerical columns
print("Summary statistics for numerical columns:")
print(data.describe())
print("\n")

# Analysis of Bitterness Preference Across Age Groups
# Ensure 'coffee_a_bitterness' and 'age' columns are present
if 'coffee_a_bitterness' in data.columns and 'age' in data.columns:
    # Group by age and get mean bitterness preference
    bitterness_by_age = data.groupby('age')['coffee_a_bitterness'].mean()
    print("Bitterness preference by age group:")
    print(bitterness_by_age)
else:
    print("Columns 'coffee_a_bitterness' or 'age' not found in the dataset.")
