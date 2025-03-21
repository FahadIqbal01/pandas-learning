import pandas as pd
import numpy as np

people = {
    'first' : ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last' : ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email' : ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age' : ['33', '55', '63', '36', None, None, 'Missing']
}

df = pd.DataFrame(data= people)

df.replace(to_replace= ['NA', 'Missing'], value= np.nan, inplace= True)

print('Original DataFrame')
print(df)

# This is how we drop missing values (axis = 'index' and how = 'any' -> default parameters)
print('\n')
print('Drop missing values from the DataFrame')
print(df.dropna())

# 
print('\n')
print('Drop all rows having all values missing')
print(df.dropna(axis='index', how= 'all'))

# 
print('\n')
print('Drop all columns having any missing values')
print(df.dropna(axis= 'columns', how= 'any'))

# 
print('\n')
print('Drop all columns having all missing values')
print(df.dropna(axis= 'columns', how= 'all'))

# 
print('\n')
print('Drop rows if "email" column has any missing values')
print(df.dropna(axis= 'index', how='any', subset= ['email']))

# 
print('\n')
print('Drop rows if "email" and "last" columns have all missing values')
print(df.dropna(axis= 'index', how= 'all', subset= ['last', 'email']))

# 
print('\n')
print('Mapping missing values in the DataFrame')
print(df.isna())

# 
print('\n')
print('Fill all the missing values with a string. Useful for numeric data.')
print(df.fillna('MISSING'))

# 
# print('\n')
# print('This is how we determine the type of columns of the DataFrame.')
# print(df.dtypes)

# 
print('\n')
print('This is how we change type of column. It is due to we can not perform specific operation on it.')
df['age'] = df['age'].astype(float)
print(df['age'].mean())