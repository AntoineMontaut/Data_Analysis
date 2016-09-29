'''
Unit2 lesson2: Visualizing Lending Club Data
'''

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

loans_data = pd.read_csv("loansData.csv")
# print(loans_data)

save_yn = "init"
while save_yn.lower() not in ["y", "n"]:
    save_yn = raw_input("\nDo you want to save the figure? [y/n]\n->")
    if save_yn.lower() not in ["y", "n"]:
        print("Please enter 'y' or 'n'")
if save_yn.lower() == "y":
    fig_name = raw_input("\nPlease enter the name of the figure to be saved:\n->")
    fig_name = fig_name + ".png"

#remove rows with null values
loans_data.dropna()

def get_plots():
    #Box Plot
    plt.figure()
    plt.subplot(2,2,1)
    loans_data.boxplot(column="Amount.Funded.By.Investors")
    plt.subplot(2,2,2)
    loans_data.boxplot(column="Amount.Requested")
    #QQ Plot
    plt.subplot(2,2,3)
    stats.probplot(loans_data["Amount.Funded.By.Investors"], dist="norm", plot=plt)
    plt.subplot(2,2,4)
    stats.probplot(loans_data["Amount.Requested"], dist="norm", plot=plt)

    # Hist
    fig = plt.figure("histograms")
    f1 = fig.add_subplot(121)
    f1.hist(loans_data["Amount.Funded.By.Investors"])
    # loans_data.hist(column="Amount.Funded.By.Investors")
    f2 = fig.add_subplot(122)
    f2.hist(loans_data["Amount.Requested"])
    # loans_data.hist(column="Amount.Requested")

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
    ax3 = fig.add_subplot(223)
    ax3.hist(data, histtype='bar')
    ax3.set_xlabel(name.replace(".", " "))
    
# all_plots(loans_data["Amount.Funded.By.Investors"], "Amount Funded by Investors")
# all_plots(loans_data["Amount.Requested"], "Amount.Requested")

def plots_2_datasets(data1, data2, name, name1, name2):
    '''Get the three plots on one figure for 2 dataset'''
    #create figure and add subplots
    fig = plt.figure(name, figsize=(25, 11))
    
    #data1
    #box plot
    ax1 = fig.add_subplot(231)
    ax1.boxplot(data1)
    ax1.set_ylabel(name1.replace(".", " "))
    #histogram
    ax2 = fig.add_subplot(232)
    ax2.hist(data1, histtype='bar')
    #QQ plot
    plt.subplot(2,3,3)
    stats.probplot(data1, dist='norm', plot=plt)
    
    #data2
    #box plot
    ax2 = fig.add_subplot(234)
    ax2.boxplot(data2)
    ax2.set_ylabel(name2.replace(".", " "))
    #histogram
    ax5 = fig.add_subplot(235)
    ax5.hist(data2, histtype='bar')
    #QQ plot
    plt.subplot(2,3,6)
    stats.probplot(data2, dist='norm', plot=plt)

plots_2_datasets(loans_data["Amount.Funded.By.Investors"], loans_data["Amount.Requested"], \
"Loans Data", "Amount.Funded.By.Investors", "Amount.Requested")
    
if save_yn == "y":
    plt.savefig(fig_name)
plt.show()