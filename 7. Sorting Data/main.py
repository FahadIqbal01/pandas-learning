import pandas as pd

people = {
    'first' : ['Corey', 'Jane', 'John', 'Adam'],
    'last' : ['Schafer', 'Doe', 'Doe', 'Doe'],
    'email' : ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com', 'AdamDoe@gmail.com']
}

df = pd.DataFrame(data= people)

print("Original DataFrame")
print(df)

# This is how we sort data by column name
sorted1 = df.sort_values(by= 'last', ascending= False)
print('\n')
print(sorted1)

# This is how we sort data by different column names
sorted1 = df.sort_values(by= ['last', 'first'], ascending= False)
print('\n')
print(sorted1)

# This is how we sort different columns data by specifying 'ascending' values
sorted1 = df.sort_values(by= ['last', 'first'], ascending= [False, True])
print('\n')
print(sorted1)

# This is how we sort index or reset the sorted DataFrame.
sorted1 = sorted1.sort_index()
print('\n')
print(sorted1)

# This is how we sort values of a column/Series object.
sorted1 = df['last'].sort_values()
print('\n')
print(sorted1)