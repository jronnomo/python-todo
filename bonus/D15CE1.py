import csv

with open("../files/weather.csv") as file:
    data = list(csv.reader(file))

city = input("What city are you looking up?: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])
