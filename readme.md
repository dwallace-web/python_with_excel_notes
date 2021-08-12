### Basic import 
import pandas as pd
from openpyxl.workbook import workbook

- read file -  Importing data from each of these data sources is provided by function with the prefix read_*

- header=None - be able to modify columns
- delimiter='\' - work off tab spacing
- .columns = ['this', 'is', 'a' ] - list of headers for columns that are defined

### Manipulating & Viewing the DataFrame
```
# get data by columns
print(df.columns)

# show data from one column
print(df['last'])

# assign details to variable - get 3 columns from the data frame
my_values = df[['first', 'last', 'Area Code']]

# save variable to excel document - index=None ---> ???
saved_values = my_values.to_excel('name_area-cod.xlsx', index=None)

```