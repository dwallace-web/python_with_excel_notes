import pandas as pd
from openpyxl.workbook import workbook

# create data frame variables for files

df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None)
df_txt = pd.read_csv('data.txt', delimiter='\t')

# print(df_csv)

df_csv.columns = ['first', 'last', 'address',
                  'city', 'State', 'Area Code', 'unknown']

print(df_csv)
df_csv.to_excel('modified.xlsx')
