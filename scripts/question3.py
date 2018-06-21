# Jelle Bosscher - 10776583
# only working with lat + lng
import random, csv, sys, itertools
from geopy.geocoders import GoogleV3
import pandas as pd
import numpy as np
import re
import matplotlib
import matplotlib.pyplot as plt
import operator
import datetime
import sys

# How does the pattern between killer/victim look between various incidents
# over the years. Is it mostly family/relation or do we see more reported gang
# violence for instance?

df = pd.read_csv('../data/clean_data_v1.csv', parse_dates=['date'])


print('-'*80)
print("Done loading CSV file")
# In[2]:


# Print first 100 rows of df
#print(df.date.dt.year.head())

#print(df[1:2])
# Start of cleaing, add new feature for avg_age; is float, not required


def strip_first_class(descriptor):
    regex = re.compile('[a-zA-Z -]+')
    result = regex.findall(descriptor)
    return result[0]




df = df[['incident_id','date','participant_relationship']]




df = df.loc[df['participant_relationship'] != '0::Unknown']

x_axis_values = list(df['participant_relationship'].unique())

x_axis_values = sorted(set([strip_first_class(value) for value in x_axis_values]))


results = {}


for value in df['incident_id']:
    row = df.loc[df['incident_id'] == value]
    if 'Unknown' in str(row.participant_relationship.item()):
        continue
    else:
        year = int(row.date.dt.year)
        month = int(row.date.dt.month)
        rel = str(row.participant_relationship.item())
        rel = strip_first_class(rel)
        if year in results.keys():
            if month in results[year].keys():
                if rel in results[year][month].keys():
                    results[year][month][rel] += 1
                else:
                    results[year][month][rel] = 1
            else:
                results[year][month] = {}
                results[year][month][rel] = 1
        else:
            results[year] = {}
            results[year][month] = {}
            results[year][month][rel] = 1
    
    #fam_f = groupby_year.get_group(key).str.count('Family').sum()
    #gang_f = groupby_year.get_group(key).str.count('Gang').sum()
    #all_rel = groupby_year.get_group(key).count()
    #results[0].append(key)
    #results[1].append(fam_f/(fam_f+gang_f))
    #results[2].append(gang_f/(fam_f+gang_f))

print('-'*80)
print("Done counter relations")


total_relations = {}

for year, months in results.items():
    if year not in total_relations.keys():
        total_relations[year] = {}
    for month, relations in months.items():
        if month not in total_relations[year].keys():
            total_relations[year][month] = 0   
        for rel, value in relations.items():
            total_relations[year][month] += value

print('-'*80)
print("Done counting relations per month")
print("Now sorting relations")

#sort results dict so all relations are alphabetical
sorted_results = {}

for year, months in results.items():
    sorted_results[year] = {}
    for month, relations in months.items():
        sorted_results[year][month] = {}
        
        #sorted_relations = sorted(relations.keys(), key=lambda x:x.lower())
        
        for key in x_axis_values:
            print(key)
            if key in relations.keys():
                sorted_results[year][month][key] = relations[key]
            else:
                sorted_results[year][month][key] = 0


# add all values per relation for each month, regardless of year
month_results = {}

for year, months in sorted_results.items():
    for month, relations in months.items():
        if month not in month_results.keys():
            month_results[month] = {}
        for relation, value in relations.items():
            if relation not in month_results[month].keys():
                month_results[month][relation] = value
            else:
                month_results[month][relation] += value


# only getting the relations we care about
print(x_axis_values)
selection = []
selection.append(x_axis_values[0])
selection.append(x_axis_values[2])
selection.append(x_axis_values[4])
selection.append(x_axis_values[5])
selection.append(x_axis_values[6])
selection.append(x_axis_values[8])
selection.append(x_axis_values[11])
selection.append(x_axis_values[12])

print('-'*80)
print("Done, plotting graph")
print('-'*80)

# Per year
#plt.figure(figsize=(40,60))
#with plt.style.context('Solarize_Light2'):
#    for year in sorted_results.values():
#        for relation in selection:
#            relation_appended = []
#            for month, relations in year.items():
#                relation_appended.append(relations[relation])
#            
#            plt.plot(year.keys(), relation_appended, label=relation)
#            plt.xticks(rotation=0)


#plt.legend(loc='best')

#plt.title('Relation of killer/victim', fontsize=30)
#plt.xlabel('Months', fontsize=24)
#plt.ylabel('Amount of incidents', fontsize=24)
#plt.show()

# per month
plt.figure(figsize=(40,60))
with plt.style.context('Solarize_Light2'):
    for relation in selection:
        relation_appended = []
        for month, relations in month_results.items():
            relation_appended.append(relations[relation])
        
        plt.plot(month_results.keys(), relation_appended, label=relation)

plt.xticks(rotation=0)
plt.legend(loc='best')

plt.yticks(np.arange(0,350,20))
plt.xticks(np.arange(0,13,1))

plt.title('Relation of killer/victim', fontsize=30)
plt.xlabel('Months', fontsize=24)
plt.ylabel('Amount of incidents', fontsize=24)
plt.show()


#plt.plot(results[0],results[1], 'ro')
#p1 = plt.bar(range(len(results[1])), results[1], align='center', color='#ffcc5c')
#p2 = plt.bar(range(len(results[2])), results[2], bottom=results[1], align='center', color='#88d8b0')
#plt.xticks(range(len(results[0])),results[0])
#plt.xlabel('year')
#plt.ylabel('incidents')
#plt.ylim(ymax=1.2)

#for x,y in enumerate(results[1]):
#    plt.text(x - .15, y + 10, str(y))

#for x,y in enumerate(results[2]):
#    plt.text(x, y + 10 + results[1][x], str(y))

#plt.title('Family vs. gang related incidents')
#plt.legend((p1[0], p2[0]), ('Family', 'Gang'))
#plt.show()



# write results to new data CSV file
#with open('../data/clean_data_v3.csv','w') as result_file:
#        wr = csv.writer(result_file, dialect='excel')
#        wr.writerows(results)
#        print("Done writing data to new CSV file")

