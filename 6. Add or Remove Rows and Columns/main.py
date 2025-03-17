import pandas as pd

people = {
    'first' : ['Corey', 'Jane', 'John'],
    'last' : ['Schafer', 'Doe', 'Doe'],
    'email' : ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}

df = pd.DataFrame(data= people)


# This is how we add column to a DataFrame
df['full_name'] = df['first'] + ' ' + df['last']
print('\n')
print(df)

# This is how we remove columns from the DataFrame
df.drop(columns= ['first', 'last'], inplace= True)
print('\n')
print(df)

# This is how we split a column 'full_name' into two columns 'first' and 'last' and add it into the DataFrame
df[['first', 'last']] = df['full_name'].str.split(' ', expand= True)
print('\n')
print(df)

# This is how we add single and multiple rows in the DataFrame
df.loc[len(df)] = {'first' : 'Tony'}
print('\n')
print(df)

df2 = pd.DataFrame(data= 
{
    'first' : ['Tony', 'Steve'],
    'last' : ['Starc', 'Rogers'],
    'email' : ['IronMan@avenege.com', 'Cap@avenge.com']
})

# This is how we concatenate 2 DataFrames
df3 = pd.concat(objs= [df, df2], ignore_index= True)
print('\n')
print(df3)

# This is how we remove row from the DataFrame
df3.drop(index= 5, inplace= True)
print('\n')
print(df3)

# This is how we remove rows according to some filter from the DataFrame
filt = df3['last'] == 'Doe'
df3.drop(index= df3[filt].index, inplace= True)
print('\n')
print(df3)