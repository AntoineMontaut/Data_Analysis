'''
Unit2 lesson1: overview of statistics
'''

import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
#data = data.split("\n")
data = [line.split(",") for line in data]

cols = data[0]
ds = pd.DataFrame(data[1::], columns=cols)

#change column content to another type
for col in cols[1:]:
    ds[col] = ds[col].astype(float)

# print(ds)

lst = [1, 1, 2, 3, 4, 1]
print stats.mode(lst)

# get mean, median, and mode
for col in cols[1:]:
    print("{0}:\nMean: {1}, median: {2}, mode: {3}".format(\
    col, round(ds[col].mean(),2), ds[col].median(), float(stats.mode(ds[col])[0])))
    print("Range: {1}, st. dev.: {2}, variance: {3}".format(\
    col, ds[col].max()-ds[col].min(), round(ds[col].std(),2), round(ds[col].var(),2)))
    print("\n")