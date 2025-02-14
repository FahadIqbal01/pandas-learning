import pandas as pd

df = pd.read_csv(filepath_or_buffer= 'data/survey_results_public.csv')
schema_df = pd.read_csv(filepath_or_buffer= 'data/survey_results_schema.csv')

print("Original DataFrame:")
print(df)
print('\n')
print("Original Schema DataFrame:")
print(schema_df)

# Show a specific column of the DataFrame
print('\n')
print(df['CodingActivities'])

# Get first row of the DataFrame
print('\n')
print("Get First Row:")
print(df.loc[0])

# Get spcified row of the DataFrame
print('\n')
print('Get Specified Row with Column:')
print(df.loc[0, 'CodingActivities'])

# Get multiple rows with specified columns of the DataFrame
print('\n')
print('Get Multiple Rows with Specified Column:')
print(df.loc[[0, 1, 2], 'CodingActivities'])

# Get all columns labels
print('\n')
print(df.columns)

# Get rows with specified columns labels but this time with slicing technique
print('\n')
print(df.loc[[0, 1, 2], 'MainBranch' : 'CodingActivities'])