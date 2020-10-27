import csv

with open('data.csv') as csvfile:
    lines = csv.reader(csvfile)

print(lines)