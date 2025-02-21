import pandas as pd

df = pd.read_csv(filepath_or_buffer= 'data/survey_results_public.csv', index_col= 'ResponseId')
schema_df = pd.read_csv(filepath_or_buffer= 'data/survey_results_schema.csv', index_col= 'qname')

# pd.set_option('display.max_columns', 65536)
# pd.set_option('display.max_rows', 65536)

# print('DataFrame')
# print('\n')
# print(df)

# print('\n')
# print('Schema DataFrame:\n')
# print(schema_df)

# This is how we filter according to salary more than 70000
high_salary = df['CompTotal'] > 70000 
print('\n')
print('Highest Salary:')
print(df.loc[high_salary, ['CompTotal', 'LanguageHaveWorkedWith', 'Country']].head(50))

# This is how we get the most viewers from the DataFrame
countries = ['United States of America', 'India', 'Pakistan', 'Germany', 'Canada']
# isin() method takes the list of countries to filter out specific countries
country_filter = df['Country'].isin(countries)
print('Most viewers from the countries:')
print(df.loc[country_filter, 'Country'])

# This is how we get all the Respondents who uses Python language. (Using str methods)
filt = df['LanguageHaveWorkedWith'].str.contains(pat= 'Python', na= False)
print('\n')
print('Respondents with Python language:')
print(df.loc[filt, 'LanguageHaveWorkedWith'])