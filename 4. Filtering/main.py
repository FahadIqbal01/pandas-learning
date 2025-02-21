import pandas as pd

people = {
    'first' : ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@email.com', 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(data= people)

print('DataFrame:\n', df)

# This is the way of filtering of the DataFrame
filt = df['last'] == 'Doe'
print('\n')
print('Filter Series\n', df[filt])

# This is how we use "loc" to filter the DataFrame
filt = df['last'] == 'Doe'
print('\n')
print('Filtering with loc:\n', df.loc[filt])

# This is how we use AND operator for filtering the DataFrame
filt = (df['last'] == 'Doe') & (df['first'] == 'John')
print('\n')
print('Filtering with AND operator:')
print(df.loc[filt, 'email'])

# This is how we use OR operator for filtering the DataFrame
filt = (df['last'] == 'Doe') | (df['first'] == 'John')
print('\n')
print('Filtering with OR operator:')
print(df.loc[filt, 'email'])

# This is how we get the results except the filter.
filt = (df['last'] == 'Schafer') | (df['first'] == 'John')
print('\n')
print('Filter all the negate data:')
print(df.loc[~filt, 'email'])