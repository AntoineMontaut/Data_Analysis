'''
Chi-square calculation example
'''

import pandas as pd
from scipy import stats
import collections
import matplotlib.pyplot as plt
import numpy as np

loans_data = pd.read_csv("loansData.csv")
loans_data.dropna()
# print(loans_data)

x = "Open.CREDIT.Lines" #in the dataset I'm working with it seems that columns are misplaced
x_name = x.replace(".", " ")
freq = collections.Counter(loans_data[x])

print("\nNote: using the small dataset it seems like the values for Open.CREDIT.Lines are under the column Revolving.CREDIT.Balance.\
\nNote2: I corrected the dataset in my directory so I am using the right column name at this point.")

def all_plots(data, name):
    '''Get the three plots on one figure for a specified column'''
    #create figure and add subplots
    fig = plt.figure(name)
    #box plot
    ax1 = fig.add_subplot(221)
    ax1.boxplot(data)
    ax1.set_ylabel(name.replace(".", " "))
    #QQ plot
    plt.subplot(2,2,2)
    stats.probplot(data, dist='norm', plot=plt)
    #histogram
    freq = collections.Counter(data)
    ax3 = fig.add_subplot(223)
    ax3.bar(freq.keys(), freq.values(), width=1)
    ax3.set_xlabel(name.replace(".", " "))

#get basic plots for the selected column
all_plots(loans_data[x], x_name)
plt.show()

#get histogram for the selected column
# fig = plt.figure(x_name)
# plt.bar(freq.keys(), freq.values(), width=1)

#lets assume expeted values are normally distributed with same mean and std
avg = loans_data[x].mean()
std = loans_data[x].std()
mod = int(stats.mode(loans_data[x])[0])
print("\nFor {0}, the mean is {1}, and standard deviation is {2}, and the mode is {3}.".format(x_name, round(avg,1), round(std,1), mod))
expected_values = list(np.random.normal(loc=avg, scale=std, size=len(loans_data[x])))
for index in xrange(len(expected_values)):
    expected_values[index] = round(expected_values[index], 0)

#based on values from data get frequency from our synthetic dataset
expected_freq = {}
for k in freq.keys():
    expected_freq[k] = expected_values.count(k)

#get chi and p
chi, p = stats.chisquare(freq.values()) #by default assumes equal frequency for all values
# chi, p = stats.chisquare(freq.values(), expected_freq.values())
print("Chi-square:\nFor {0}, chi = {1}, and p = {2}.".format(x_name, chi, p))

plt.show()