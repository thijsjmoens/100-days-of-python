import pandas as pd

data = pd.read_csv('weather_data.csv')

mean = data['temp'].mean()
print(mean)