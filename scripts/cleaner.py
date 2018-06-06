# Jelle Bosscher - 10776583
# Script to clean the gun violence data
import csv


raw = []

with open('../data/stage3.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        raw.append(row)

empty_cells_per_column = [0]*29

j = 0
for attribute in raw[0]:
    empty_cells_per_column[j] = [attribute, 0]
    j+=1

for i in range(0,len(raw[0])):
    for row in raw[1:]:
        if row[i] is '':
            empty_cells_per_column[i][1] +=1

for row in empty_cells_per_column:
    print("Class: {:<30s} - Missing Values: {:<20d}".format(row[0],row[1]))

print("The whole data set has {} rows".format(len(raw)))
