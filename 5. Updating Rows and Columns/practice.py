import pandas as pd

df = pd.read_csv(filepath_or_buffer= 'data/survey_results_public.csv')
schemas = pd.read_csv(filepath_or_buffer= 'data/survey_results_schema.csv')

# pd.set_option('display.max_columns', 65536)
# pd.set_option('display.max_rows', 65536)

# df.rename(columns= {'ConvertedCompYearly' : 'SalaryUSD'}, inplace= True)
# print(df['SalaryUSD'])


print(df[['EdLevel', 'CodingActivities']])