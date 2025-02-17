import pandas as pd

# This is how we set the index column of the DataFrame when importing data from the file(s).
df = pd.read_csv(filepath_or_buffer= 'data/survey_results_public.csv', index_col= 'ResponseId')
schema_df = pd.read_csv(filepath_or_buffer= 'data/survey_results_schema.csv', index_col= 'qname')

# pd.set_option('display.max_columns', 10000)
pd.set_option('display.max_rows', 10000)

print('DataFrame:')
print(df.head())


# print('\n')
# print("Schema DataFrame:")
# print(schema_df)

# This is how get the full text if the text is collapsed by specifying the second argument
print('\n')
print(schema_df.loc['CodingActivities', 'question'])

# This is how we sort the DataFrame alphabetically
print('\n')
print("Sorted DataFrame:")
schema_df.sort_index(inplace= True)
print(schema_df)