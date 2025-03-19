import pandas as pd

df = pd.read_csv(filepath_or_buffer= 'data/survey_results_public.csv', index_col= 'ResponseId')

# print('Original DataFrame')
# print(df)

# This is how we sort data according to specific columns
df.sort_values(by= ['Country', 'ConvertedCompYearly'], ascending= [True, False], inplace= True)
print('\n')
print('DataFrame sorted by countries:')
print(df['Country'].head(50))

# This is how we get sorted data according to columns.
print('\n')
print(df[['Country', 'ConvertedCompYearly']].head(50))

# 
print('\n')
# print(df[['Country', 'ConvertedCompYearly']].head(50))

# This is how we get the largest values of column(s) from the DataFrame
largest_salaries = df['ConvertedCompYearly'].nlargest(n= 10)
print('\n')
print(largest_salaries)

# This is how we get the complete sorted rows from the DataFrame
print('\n')
print(df.nlargest(n= 10, columns= 'ConvertedCompYearly'))