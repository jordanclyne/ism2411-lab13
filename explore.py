#1. A Boolean filter uses a condition (True or False) to test each row in a table.
#The rows that meet the condition are returned in a new table.
#2. df["revenue"] returns a Series, whereas df[["revenue"]] returns a DataFrame.
#A Series is a single column of data, while a DataFrame is a table with rows and columns.
#3. Using pandas is more efficient than using Excel because it allows for automation.
#Things that would require manual effort in Excel can be done automatically in seconds with pandas.
#Additionally, pandas removes the need for clicking and copy-pasting.

print("---Exercise 1: Load It---")

import pandas as pd
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("---Exercise 2: Filter by Region---")
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

print("---Exercise 3: Top 5 by Revenue---")
top5 = df.sort_values('revenue', ascending=False).head(5)
print(top5)

print("---Exercise 4: Two-Condition Filter---")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head())

print("---Exercise 5: A New Column---")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

print("---Exercise 6: Unique Values---")
print(df['region'].unique())
print(df['region'].value_counts())

print("---Exercise 7: Select Columns---")
df_filtered = df[['region', 'product', 'revenue']]
print(df_filtered.shape)

print("---Exercise 8: Save---")
df.to_csv('data/explored.csv', index=False)
