import pandas as pd
from openpyxl.workbook import workbook

df = pd.read_csv('Names.csv', header=None)

# access data
df.columns = ['first', 'last', 'address',
              'city', 'State', 'Area Code', 'unknown']

# get data by columns
print(df.columns)

# show data from one column
print(df['last'])

# show data from first three rows
print(df['city'][0:3])

# print column / row only
print(df.iloc[2])

# show full data frame
print(df)

# pick specific value by index - state CO
print(df.iloc[5, 4])

# assign details to variable - get 3 columns from the data frame
my_values = df[['first', 'last', 'Area Code']]
# print??
print(my_values)
# save variable to excel document - index=None ---> ???
saved_values = my_values.to_excel('name_area-cod.xlsx', index=None)
