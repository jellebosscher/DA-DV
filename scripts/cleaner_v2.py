# Jelle Bosscher - 10776583
# Script to clean the gun violence data
# only working with lat + lng
import random, csv, sys, itertools
from geopy.geocoders import GoogleV3

raw = []

#TODO remove relationship feature

with open('../data/clean_data_v1.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        raw.append(row)

# Count missing values per feature
empty_cells_per_column = [0]*27

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

#TODO fix missing lat + lng
#geolocator = Nominatim(country_bias="United States")

api_keys = ['AIzaSyCwIHCbi10jJEX-V9J2Bl-aw2-07vbt9sI','AIzaSyBQcftzxiXV48WffO-906cDgGdn0nD0pps','AIzaSyCqFbCDyGy7U2CZZ9FCM6LEV59wzEQ_UHs','AIzaSyCPVONF8HJsol32Ll_qxQ_RI3Rf1NO8-Vc']

geolocator = GoogleV3(api_key=random.choice(api_keys))
 
lat_lng_dict = {}

for row in raw:
    if (row[14] is '') or (row[16] is ''):
        try:
            location = geolocator.geocode(row[3] + ' ' + row[2])
        except (socket.timeout, geopy.exc.GeocoderTimedOut):
            print("skipping  the rest")
            break
        if location in ('', None):
            location = geolocator.geocode(row[4] + ' ' + row[3] + ' ' + row[2])
            if location in ('', None):
                continue
            else:
                lat_lng_dict[row[0]] = [location.latitude, location.longitude]
        else:
            lat_lng_dict[row[0]] = [location.latitude, location.longitude]

for x, y in lat_lng_dict.items():    
    print('{:<30f} - {:<30f}'.format(y[0],y[1]))

print('total number of new lat+long should be 7923') 
print('is actually: {}'.format(len(lat_lng_dict.keys())))



# ----------------------------------------------------------------------
# creating the results

# add new feature to the label row (the first row) of the results
# and remove several features
#-----------------------------------------------------------------------




# write results to new data CSV file
with open('../data/clean_data_v2.csv','w') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerows(results)
        print("Done writing data to new CSV file")

