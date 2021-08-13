import pandas as pd
from pandas import concat

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address',
              'City', 'State', 'Area Code', 'Income']

# show rows by column values
print(df.loc[df['City'] == 'Riverside'])

# rows income >50000
print(df.loc[df['Income'] >= 50000])

# rows income >80000
print(df.loc[df['Income'] >= 80000])

# create column - tax_bracket
taxes = df['Tax %'] = df['Income'].apply(
    lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)

# show new variable by itself
print(taxes)

# show new table
print(df)

df['Annual Tax'] = df['Income'] * df['Tax %']
print(df)

# remove columns
to_drop = ['Area Code', 'First', 'Address']
df.drop(columns=to_drop, inplace=True)
print(df)

# create column with fake values
df['Income < 75000'] = False
# row has value less than 75000
df.loc[df['Income'] < 75000, 'Income < 75000'] = True
print(df)

# group by - show the averages of unique values in a column. Exampl shows the averages of the income, tax % and taxes owed
print(df.groupby(['Income < 75000']).mean())

# sort by - order data set
print(df.sort_values('Income'))
