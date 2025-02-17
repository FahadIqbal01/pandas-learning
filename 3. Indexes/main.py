import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}

df = pd.DataFrame(data= people)
print("DataFrame:")
print(df)

# This is how we set the index of the DataFrame
df.set_index(keys= 'email')
print('\n')
print("DataFrame:")
print(df)

# But above method doesn't change the index of the DataFrame
df.set_index(keys= 'email', inplace= True)
print('\n')
print('DataFrame with specified index:')
print(df)

# This shows the index column of the DataFrame
print('\n')
print(df.index)

print('\n')
print(df.loc['CoreyMSchafer@gmail.com', 'last'])

# This is how we reset the index of the DataFrame
df.reset_index(inplace= True)
print('\n')
print("Reset Index of DataFrame")
print(df)