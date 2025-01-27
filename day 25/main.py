# Option 1
# f = open("weather_data.csv", "r")
# data = f.readlines()

# Option 2
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# Option 3
import csv

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    
    # Skip the header
    next(data_file)
    
    for row in data:
        # Get the temperatures
        temperature = row[1]
        
        temperature = int(temperature)
        temperatures.append(temperature)        

print(temperatures)