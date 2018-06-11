# Jelle Bosscher - 10776583
# Script to clean the gun violence data
from global_functions import csv_dict_to_py_dict
import random, csv, sys, itertools
from geopy.geocoders import GoogleV3



raw = []

with open('../data/stage3.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        raw.append(row)

# Count missing values per feature
empty_cells_per_column = [0]*29

j = 0
for attribute in raw[0]:
    empty_cells_per_column[j] = [attribute, 0]
    j+=1

for i in range(0,len(raw[0])):
    for row in raw[1:]:
        if row[i] is '':
            empty_cells_per_column[i][1] +=1
k = 1
for row in empty_cells_per_column:
    print("{:<3d} Class: {:<30s} - Missing Values: {:<20d}".format(k,row[0],row[1]))
    k+=1

print("The whole data set has {} rows".format(len(raw)))



# Start of cleaing, add new feature for avg_age; is float, not required
print('-'*80)

# calculate the average age for every entry with given ages.
avg_age_dict = {}

for row in raw[1:]:
    key = row[0]
    if row[19] is not '':
        age_dict = csv_dict_to_py_dict(row[19])
        avg_age_dict[key] = "{:.2f}".format(sum(age_dict.values())/len(age_dict))
    else:
        avg_age_dict[key] = ''

#TODO strip house numbers from adress.


# ----------------------------------------------------------------------
# creating the results

# add new feature to the label row (the first row) of the results
# and remove several features
results = [raw[0]]
del results[0][15] #location_description
del results[0][21] #participant_name
del results[0][21] #participant_relationship
results[0].insert(19, "participant_average_age")
print(results[0])

#append all rows to new results, inserting new values in every row
# and removing several values from every row
for row in raw[1:]:
    del row[15] #location_description
    del row[21] #participant_name
    del row[21] #participant_relationship
    row.insert(19,avg_age_dict[row[0]]) #insert avg_age
    results.append(row)

#-----------------------------------------------------------------------




# write results to new data CSV file
with open('../data/clean_data_v1.csv','w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerows(results)
        print("Done writing data to new CSV file")


print('-'*80)
print("Example sample:")
print("{:<30s} - {:<20s}".format(results[0][19],results[0][20]))

#for row in results[12100:12140]:
#    print("{:<30s} - {:<20s}".format(row[18],row[19]))



