import pandas as pd

# Read all data from the Excel file into a DataFrame
df = pd.read_excel('/home/mirafra/gitPull/CPractice/Python/Sample.xlsx')

# Read only the first column from the Excel file into the DataFrame
# This will overwrite the previous DataFrame 'df' with only the first column
df = pd.read_excel('/home/mirafra/gitPull/CPractice/Python/Sample.xlsx', usecols=[0])

# Read only the first row from the Excel file into the DataFrame
# This will overwrite the previous DataFrame 'df' with only the first row
df = pd.read_excel('/home/mirafra/gitPull/CPractice/Python/Sample.xlsx', nrows=1)

# Convert the DataFrame to a list of lists
# Each sublist in 'lst' represents a row in the DataFrame
lst = df.values.tolist()

# Convert the column names of the DataFrame to a list
# 'column_list' will contain the column names of the DataFrame
column_list = df.columns.tolist()

# Print the list of values read from the Excel file (either the first row or the values in the first column)
print(lst)

# Print the list of column names of the DataFrame
print(column_list)
