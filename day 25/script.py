import pandas as pd

data = pd.read_csv('weather_data.csv')

# Average
mean = data['temp'].mean()

# Max temp
max = data['temp'].max()
print(max)