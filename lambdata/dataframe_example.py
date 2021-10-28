import pandas as pd

# Classes have variables, and functions
# when we talk about variables that are associated with objects/classes we call them "attributes"
# wehn we talk about functions that are associated with objects/classes we call them "methods"

# df = pd.DataFrame({'a': [1,2,3], 'b':[4,5,6]})

# dataframe attributes
# attributes have no parentheses
# print(df.shape)
# print(df.index)
# print(df.dtypes)

# dataframe methods
# mehotds *do* have parentheses
# print(df.isnull())
# print(df.head())
# print(df.value_counts())
# print(df.describe())


df = pd.DataFrame()

print(df)