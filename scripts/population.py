import pandas as pd
import random, csv, sys, itertools
# data = pd.read_csv("population_per_state.csv", encoding="utf-8")

raw = []
with open('population_per_state.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        raw.append(row)

math = {}

for row in raw[1:]:
    year1 = int(row[1])
    year5 = int(row[5])

    math[row[0]] = str((year5 / year1)**(1/60))

attribute = []
attribute.insert(0, "Population per state per month in a given year")

year = 2013
month = 1
for i in range(60):
    date = str(month)+str('/')+str(year)
    attribute.append(date)
    month += 1
    if month >= 13:
        month = 1
        year += 1

results = [attribute]

for row in raw[1:]:
    pop_per_month = []
    pop_per_month.append(row[0])
    pop_month = int(row[1])
    pop_per_month.append(pop_month)
    for j in range(59):
        pop_month = round(int(pop_month) * float(math[row[0]]))
        pop_per_month.append(pop_month)
    results.append(pop_per_month)

with open('population_per_state_v2.csv','w') as file:
    wr = csv.writer(file, dialect='excel')
    wr.writerows(results)
    print("csv file added")
