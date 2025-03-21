import pandas as pd

na_vals = ['NA', 'Missing']
df = pd.read_csv(filepath_or_buffer= 'data/survey_results_public.csv', index_col= 'ResponseId', na_values= na_vals)

# print('Original DataFrame')
# print(df)

# 
print('\n')
print(df['YearsCode'].head(10))

# 
# df['YearsCode'] = df['YearsCode'].astype(float
# print(df['YearsCode'].mean())

# 
print('\n')
print('This is how we get unique values of the columns.')
print(df['YearsCode'].unique())

# 
df['YearsCode'] = df['YearsCode'].replace(to_replace= ['More than 50 years', 'Less than 1 year'], value= ['51', '0'])
df['YearsCode'] = df['YearsCode'].astype(float)
print('\n')
print('We replace strings with some values so that we can find mean, median etc,.')
print(df['YearsCode'].unique())

# 
print('\n')
print('Average years of coding experience')
print(df['YearsCode'].mean())
print(df['YearsCode'].median())