import pandas as pd

df = pd.read_csv(filepath_or_buffer= 'data/ETH_1h.csv')

print('Original DataFrame')
print(df)

# 
print('\n')
print('Shape of the DataFrame, rows and columns.')
print(df.shape)

# 
print('\n')
# This is how we convert column type from string to DateTime object.
df['Date'] = pd.to_datetime(arg= df['Date'], format= '%Y-%m-%d %I-%p')
print('Day name of specified date time.')
print(df.loc[0, 'Date'].day_name())

# 
# print('\n')
# print('Day names of the whole "Date" series.')
# print(df['Date'].dt.day_name())

# 
df['DayOfWeek'] = df['Date'].dt.day_name()
print('\n')
print('DayOfWeek column added in DataFrame')
print(df)

# 
print('\n')
print('Oldest Date:', df['Date'].min())
print('Latest Date:', df['Date'].max())
print('Difference bewtween dates:', df['Date'].max() - df['Date'].min())

# 
filt = (df['Date'] >= '2019') & (df['Date'] < '2020')
print('\n')
print('Filtered data with respect to years.')
print(df.loc[filt])

# 
df.set_index(keys= 'Date', inplace= True)
print('\n')
print('Set index column of Date in the DataFrame.')
print(df)

# 
# print('\n')
# print('')
# print(df.loc['2019'])

# 
print('\n')
print('Average price of ETHUSD in 2019')
print(df.loc['2019']['Close'].mean())

# 
print('\n')
print('Max High value of the day.')
print(df.loc['2020-03-12']['High'].max())

# 
print('\n')
print('Resample data with Day format code and get the max High of the day.')
highs = df['High'].resample('D').max()
print(highs)

# 
print('\n')
print('')
print(df.resample('W').agg({'Close' : 'mean', 'High' : 'max', 'Low' : 'min', 'Volume' : 'sum'}))