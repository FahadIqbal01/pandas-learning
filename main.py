import pandas as pd

# Importing data from "csv" file
df = pd.read_csv(filepath_or_buffer= "data/survey_results_public.csv")

# shape property gives rows and columns of the dataframe
df_shape = df.shape
print("Data Frame:", df_shape, '\n')

# info() function gives full details of the dataframe
print("Data Frame Info:")
df_info = df.info()

# set_option() shows the dataframe with full columns and rows.
# pd.set_option('display.max_columns', 114)
# pd.set_option('display.max_rows', 100)

# Import schema data from "data/survey_results_schema.csv" file
schema_df = pd.read_csv(filepath_or_buffer= 'data/survey_results_schema.csv')
print("Schema DataFrame:\n", schema_df)

# head() function gives first 'n' rows. If n unspecified returns first 5 rows.
df_initial_rows = df.head(10)
print(df_initial_rows, '\n')

# tail() functions gives last 'n' rows. If n unspecified returns last 5 rows.
df_last_rows = df.tail(10)
print(df_last_rows, '\n')