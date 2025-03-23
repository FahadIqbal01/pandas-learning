import pandas as pd

df = pd.read_csv(filepath_or_buffer= 'data/survey_results_public.csv', index_col= 'ResponseId')

# print('Original DataFrame')
# print(df)

filt = (df['Country'] == 'India')
india_df = df.loc[filt]
# print('\n')
# print('India DataFrame')
# print(india_df.head())

# Export data to CSV file.
# india_df.to_csv(path_or_buf= 'data/modified.csv')

# Export data to TSV file.
# india_df.to_csv(path_or_buf= 'data/modified.tsv', sep= '\t')

# Export data to Excel (xlsx) file.
# india_df.to_excel('data/modified.xlsx')

# df = pd.read_excel('data/modified.xlsx', index_col= 'ResponseId')
# print('\n')
# print('Read data from Excel file.')
# print(df.head())

# Export datat to JSON file.
# india_df.to_json(path_or_buf= 'data/modified.json', orient= 'records', lines= True)

df = pd.read_json(path_or_buf= 'data/modified.json', orient= 'records', lines= True)
print('\n')
print('Read data from JSON file.')
print(df.head())