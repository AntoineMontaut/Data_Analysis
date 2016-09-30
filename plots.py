'''
Standard plots
'''

import matplotlib.pyplot as plt
import scipy.stats as stats

def all_plots(data, name, unit):
    '''Produce a boxplot, a histogram and a QQ plot for the given data'''
    
    fig = plt.figure(name)
    #box plot
    ax1 = fig.add_subplot(221)
    ax1.boxplot(data)
    ax1.set_ylabel(name.replace(".", " ") + " ({0})".format(unit))
    #QQ plot
    plt.subplot(2,2,2)
    stats.probplot(data, dist='norm', plot=plt)
    #histogram
    ax3 = fig.add_subplot(223)
    ax3.hist(data, histtype='bar')
    ax3.set_xlabel(name.replace(".", " ") + " ({0})".format(unit))