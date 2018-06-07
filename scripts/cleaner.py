# Jelle Bosscher - 10776583
# Script to clean the gun violence data
import csv, sys, itertools


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

# helper function to turn the CSV formatted dict to use in python
def csv_dict_to_py_dict(csv_string):
    if '::' in csv_string:
        py_dict = dict((key, int(value)) for key, value in (item.split('::') for item in csv_string.split('||')))
    elif ':' in csv_string:
        py_dict = dict((key, int(value)) for key, value in (item.split(':') for item in csv_string.split('|')))
    return py_dict


# calculate the average age for every entry with given ages.
dict_b = {}

for row in raw[1:]:
    key = row[0]
    if row[19] is not '':
        age_dict = csv_dict_to_py_dict(row[19])
        dict_b[key] = "{:.2f}".format(sum(age_dict.values())/len(age_dict))
    else:
        dict_b[key] = ''

#add new feature to first row
results = [raw[0]]
results[0].insert(20, "average_age")

#append all rows to new results, inserting new value in every row
for row in raw[1:]:
    row.insert(20,dict_b[row[0]])
    results.append(row)




# write results to new data CSV file
with open('../data/clean_data_v1.csv','w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerows(results)
        print("Done writing data to new CSV file")


print('-'*80)
print("Example sample:")
print("{:<30s} - {:<20s}".format(results[0][19],results[0][20]))

for row in results[12100:12140]:
    print("{:<30s} - {:<20s}".format(row[19],row[20]))



