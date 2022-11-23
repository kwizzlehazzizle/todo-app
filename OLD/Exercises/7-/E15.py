"""import glob
myfiles = glob.glob("files/*.txt")
print(myfiles)
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())"""

"""import csv

with open("weather.csv",'r') as file:
    data = list(csv.reader(file))
#print(data)
for element in data:
    #print(element)
    location = element[0]
    temperature = element[1]
    print(location,temperature)

city = input("Enter a city: ")
for row in data[1:]:
    if row[0] == city:
        print(row[1])"""
"""
import shutil

shutil.make_archive("output", "zip", "Files")"""

import webbrowser

user_term = input("Enter a search term: ").replace(" ","+")

webbrowser.open("https://www.google.com/search?q="+user_term)









