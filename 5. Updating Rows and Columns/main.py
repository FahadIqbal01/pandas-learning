import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'],
    'last': ['Schafer', 'Doe', 'Doe'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@gmail.com', 'JohnDoe@gmail.com']
}

df = pd.DataFrame(data= people)

# This is how we get the columns of the DataFrame
# print('DataFrame Columns:')
# print(df.columns)

# This is how we change the names of the columns
# df.columns = ['first_name', 'last_name', 'email']
# print('\n')
# print('Updated Column Names:')
# print(df)

# This is how we capitalize or lower case column names.
# df.columns = [x.lower() for x in df.columns]
# print('\n')
# print('DataFrame Capitalize Columns:')
# print(df)

# This is how we rename the specific columns
# df.rename(columns= {'first_name' : 'first', 'last_name' : 'last'}, inplace= True)
# print('\n')
# print('Update Specific Columns:')
# print(df)

# This is how we update specific row in the DataFrame
# df.loc[2] = ['John', 'Smith', 'JohnSmith@gmail.com']
# print('\n')
# print('Update Specific Row:')
# print(df)

# This is how we update specific columns of a row of the DataFrame
# df.loc[2, ['last', 'email']] = ['Doe', 'JohnDoe@gmail.com']
# print('\n')
# print('Reverted DataFrame:')
# print(df)

# This is the basic way of updating multiple rows in a DataFrame
# df['email'] = df['email'].str.lower()
# print('\n')
# print(df)

# Updating rows using advanced methods

# apply() method used on Series and DataFrame objects.
# This is how we use apply() method, to get the informations of all rows.
# emailLengths = df['email'].apply(len)
# print('\n')
# print('Lengths of emails:')
# print(emailLengths)


# def update_email(email):
#     return email.upper()

# print('\n')
# print('This is how we use custom methods in apply() method.')
# df['email'] = df['email'].apply(func= update_email)
# print(df)

# print('\n')
# print('This is how we use lambda function in apply() method.')
# df['email'] = df['email'].apply(lambda x: x.lower())
# print(df)

# applymap() method applies function on each elements of the DataFrame.
print('\n')
print(df.map(len))

# This is how we lowercase every element of the DataFrame.
print('\n')
print(df.map(str.lower))

# map() substitutes each value of the Series object with another value.
print('\n')
print(df['first'].map({'Corey' : 'Chris', 'Jane' : 'Mary'}))

# 
print('\n')
print(df['first'].replace({'Corey' : 'Chris', 'Jane' : 'Mary'}))