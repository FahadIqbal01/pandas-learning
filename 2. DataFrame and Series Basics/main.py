import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}

# Create DataFrame from the dictionary 'people'
df = pd.DataFrame(people)
print("DataFrame:")
print(df)

# This way we access the column of the DataFrame
print('\n')
print(df['email'])

# This shows that it is Panda Series
print('\n')
print(type(df['email']))

# This is how we show multiple columns.
print('\n')
print(df[['email', 'last']])

# This is how we show all columns.
print('\n')
print(df.columns)

# This is how we get rows of the DataFrame
print('\n')
print("Get Row with iloc indexer:")
print(df.iloc[0])

# This is how we get multiple rows of the DataFrame
print('\n')
print("Get Multiple Rows:")
print(df.iloc[[0, 2]])

# This is how we get rows and columns of the DataFrame with Pandas "iloc" indexer
print('\n')
print("Get Multiple Rows with Columns:")
print(df.iloc[[0, 1, 2], 2])

# This is how we get rows of the DataFrame using 'loc' indexer
print('\n')
print('Get Row with loc indexer:')
print(df.loc[0])

# This is how we get multiple rows of the DataFrame
print('\n')
print('Get Multiple Rows:')
print(df.loc[[0, 1]])

# This is how we get multiple rows with columns of the DataFrame
print('\n')
print('Get Multiple Rows with Columns:')
print(df.loc[[0, 1], 'email'])

print('\n')
print(df.loc[[0, 2], ['email', 'last']])