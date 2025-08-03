import csv
import pandas

# Open csv file without Pandas
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print("Write out temperature from csv file without using Pandas:")
    print(temperatures)

# Open csv file with Pandas
data = pandas.read_csv("weather_data.csv")
print("\nWrite out temperature from csv file with using Pandas:")
print(data["temp"], "\n")


# Basic data structures in pandas
"""Pandas provides two types of classes for handling data:
1. DataFrame: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.
2. Series: a one-dimensional labeled array holding data of any type such as integers, strings, Python objects etc."""

print(f"1. Data in pandas is of the DataFrame type, which is equivalent to one sheet of an Excel document: {type(data)}")
print(f"2. Data in one column of a DataFrame has a Series object type: {type(data["temp"])}\n")


# Conversion in Pandas
print("Convert DataFrame to Dictionary:")
data_dict = data.to_dict()
print(data_dict, "\n")

print("Convert Series to List:")
temp_list = data["temp"].to_list()
print(temp_list, "\n")


# Calculating the average and maximum value

# The usual method:
average = sum(temp_list) / len(temp_list)
print(f"Average temperature is: {average}")

# Using Pandas Library methods:
print(f"Average temperature is: {data["temp"].mean()} [Pandas Library]")
print(f"Max temperature is {data["temp"].max()}\n")


# Get Data in Columns
print(f"Data in column condition:\n{data["condition"]}\n")
# or
# print(data.condition)

# Get Data in Row
print(f"Data from the row day equals Monday:\n{data[data["day"] == "Monday"]}\n")
# or
# print(data[data.day == "Monday"])

# Row with the highest temp
print(f"Row with the highest temp:\n{data[data.temp == data.temp.max()]}\n")


# Convert Monday temp from Celsius to Fahrenheit
monday = data[data.day == "Monday"]
print(f"Monday temp in Celsius: {monday.temp}\n")
monday_temp_F = monday.temp * 1.8 + 32
print(f"Monday temp in Fahrenheit: {monday_temp_F}\n")


# Create DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data_frame = pandas.DataFrame(data_dict)
print(f"New DataFrame created in Pandas from dictionary:\n{new_data_frame}\n")
new_data_frame.to_csv("students_and_scores.csv")



#Squirrell count challenge

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250225.csv")

# Extracting the color values of all squirrels and writing them to a list
squirrel_color = squirrel_data["Primary Fur Color"].to_list()

squirrel_dict = {
    "Color": [],
    "Count": [],
}

# Adding all colors and their quantities to the dictionary
for color in ("Gray", "Cinnamon", "Black"):
    squirrel_dict["Color"].append(color)
    squirrel_dict["Count"].append(squirrel_color.count(color))

# Convert squirrel_dict to pandas and create new csv file with this data
pandas_squirrel_dict = pandas.DataFrame(squirrel_dict)
print(f"Number of each color of squirrels in New York's Central Park:\n{pandas_squirrel_dict}")
pandas_squirrel_dict.to_csv("squirrel_count.csv")
