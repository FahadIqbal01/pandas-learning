import pandas as pd

df = pd.read_csv(filepath_or_buffer= 'data/survey_results_public.csv', index_col= 'ResponseId')
schema_df = pd.read_csv(filepath_or_buffer= 'data/survey_results_schema.csv')

print(df['ConvertedCompYearly'].head(15))

# 
print('\n')
print('Average salary of a developer:')
print(df['ConvertedCompYearly'].median())

# Median of the whole DataFrame
print('\n')
print('Median of the DataFrame')
print(df.median(numeric_only= True))

# This is how we get the description of the DataFrame
print('\n')
print('Description of the DataFrame')
# print(df[['ConvertedCompYearly', 'CompTotal']].describe())
print(df.describe())

# This is how we get the count of the non-missing values of the columns.
print('\n')
print('Count of the non missing values of the column(s)')
print(df[['ConvertedCompYearly', 'CompTotal']].count())

# 
print('\n')
print('This is how we get the breakdown of values in percentage form.')
print(df['RemoteWork'].value_counts(normalize= True))

# 
# print('\n')
# print(df['Country'].value_counts())

# This is how we group data according to 'Country', and then further funnel down the data.
country_group = df.groupby(by= 'Country')
print('\n')
print(country_group['RemoteWork'].value_counts().loc['Pakistan'])

# 
print('\n')
print('Average salaries of the developers by grouping data')
print(country_group['ConvertedCompYearly'].median().loc['Pakistan'])

# This is how we applies aggregate functions(median, mean etc.,) on the grouped data.
print('\n')
print('Average and Mean salaries of the developers.')
print(country_group['ConvertedCompYearly'].agg(['median', 'mean']).loc['Pakistan'])

# This is how we get the number of respondents from each country knowing python.
print('\n')
country_respondants = df['Country'].value_counts()

country_uses_python = country_group['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum())

python_df = pd.concat([country_respondants, country_uses_python], axis= 'columns', sort= False)

python_df.rename(columns= {'count':'NumRespondents', 'LanguageHaveWorkedWith':'NumKnowsPython'}, inplace= True)

python_df['PCTKnowsPython'] = (python_df['NumKnowsPython'] / python_df['NumRespondents']) * 100

python_df.sort_values(by= 'PCTKnowsPython', ascending= False, inplace= True)

print(python_df.head(50))