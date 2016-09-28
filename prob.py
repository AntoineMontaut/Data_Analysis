'''
Unit2 lesson2: Probability Distributions and Densities
'''

import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#Frequency
test_list = [1, 4, 5, 6, 9, 9, 9]

cnt = collections.Counter(test_list)

print(cnt)

cnt_sum = sum(cnt.values())

print("\nIn {0}:".format(test_list))
for k, v in cnt.iteritems():
    print("The frequency of {0} is {1}.".format(k, round(float(v)/cnt_sum, 2)))


def plot_types():
    test_list = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
    plt.figure("Box Plot and Histogram")
    plt.subplot(2,2,1)
    plt.title("Box Plot")
    plt.boxplot(test_list)
    plt.subplot(2,2,2)
    plt.title("Histogram")
    plt.hist(test_list, histtype='bar')

    plt.subplot(2,2,3)
    plt.title("QQ Plot - Random")
    test_data_1 = np.random.normal(size=1000)
    graph1 = stats.probplot(test_data_1, dist="norm", plot=plt)
    plt.subplot(2,2,4)
    plt.title("QQ Plot - uniform")
    test_data_2 = np.random.uniform(size=1000)
    graph2 = stats.probplot(test_data_2, dist="norm", plot=plt)
    plt.show()
    
# plot_types()

def base_plots(data, figure_name):
    plt.figure(figure_name)
    plt.subplot(2,2,1)
    plt.title("Box Plot")
    plt.boxplot(data)
    plt.subplot(2,2,2)
    plt.title("Histogram")
    plt.hist(data, histtype='bar')

    plt.subplot(2,2,3)
    plt.title("QQ Plot - Random")
    graph1 = stats.probplot(data, dist="norm", plot=plt)
    # plt.subplot(2,2,4)
    # plt.title("QQ Plot - uniform")
    # graph2 = stats.probplot(data, dist="norm", plot=plt)
    plt.show()
    
test_list = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
base_plots(test_list, "Test List")