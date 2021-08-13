import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address',
              'City', 'State', 'Area Code', 'Income']

# only drop addresses
df.drop(columns='Address', inplace=True)

# get the row by a new identifier -- index -- area code
df = df.set_index('Area Code')
print(df.loc[8074])

# get row by index with iloc - by index
print(df.iloc[0])

# get everyones first name; by the index of 8074
print(df.loc[8074:, 'First'])

# split data with first names only - each word in the colmumn will get a dedicated column
print(df.First.str.split(expand=True))

# replace NaN value with empty string

df = df.replace(np.nan, 'No Answer', regex=True)
print(df)
to_excel = df.to_excel('modified-clean.xlsx')
