### Basic import 
```
import pandas as pd
from openpyxl.workbook import workbook
import numpy as np
```

#### Pareto Principle / 80-20 problem

- read file -  Importing data from each of these data sources is provided by function with the prefix read_*
- header=None - be able to modify columns
- delimiter='\' - work off tab spacing
- .columns = ['this', 'is', 'a' ] - list of headers for columns that are defined
- inplace=True -- this flag only confirms that dataframe applies only to the current instance
- index=None ---> ???
- expand=True

### Viewing the DataFrame
```
<!-- check viewing_data.py -->
# get data by columns
print(df.columns)

# show data from one column
print(df['last'])

# assign details to variable - get 3 columns from the data frame
my_values = df[['first', 'last', 'Area Code']]

# save variable to excel document - index=None ---> ???
saved_values = my_values.to_excel('name_area-cod.xlsx', index=None)

# read a tab delimited file
pd.read_csv('output.txt', delimiter='\t')

# get the first five rows of data
print(df['id'][0:5])

# replace Nan values with '0' in the df
df = df.replace(np.nan, '0', regex=True)

```

### Manipulating the data frame
```

<!-- Check filtered_data.py -->

# create new column based on data
taxes = df['Tax %'] = df['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)

# generate new column with 1. existing data & 2. new data
df['Annual Tax'] = df['Income'] * df['Tax %']

# remove unwanted columns
df.drop(columns=to_drop, inplace=True)

# create new column and add a value to the row
df.loc[df['Income'] < 75000, 'Testing Column'] = True

# update value in new column when value is < 75000
df.loc[df['Income'] < 75000, 'Income < 75000'] = True
```

### Get values from data
```
<!-- Check filtered_data.py -->

Show the average
df.groupby(['Income < 75000']).mean()

Sort the data
df.sort_values('Income')
```

### cleaning data basics

```
# split data with first names only - each word in the colmumn will get a dedicated column
print(df.First.str.split(expand=True))

# replace NaN value with empty string
df = df.replace(np.nan, 'No Answer', regex=True)
```

### find data with a custom index
```
# get the row by a new identifier -- index -- area code
df = df.set_index('Area Code')
print(df.loc[8074])

# get row by index with iloc - by index
print(df.iloc[0])
```

### examples
```
# Give students with a grade > 90 a 4.0 or put nothing:
df['grade'] = df['points'].apply(lambda x: 4.0 if 90 <= x <= 100 else '')


```