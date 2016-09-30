'''
Unit2 Lesson3: Linear Regression and Correlation
'''

import pandas as pd
import plots
import matplotlib.pyplot as plt

ds_loans = pd.read_csv("loansData.csv")
# print(ds_loans.head(5))
# print(ds_loans.info())
ds_loans.dropna()

fico = "FICO.Score"
fico_name = fico.replace(".", " ")
int_rate = "Interest.Rate"
int_rate_name = int_rate.replace(".", " ")
length = "Loan.Length"
length_name = length.replace(".", " ")

ds_loans[fico] = ds_loans["FICO.Range"].map(lambda x: int(str(x).rstrip().split("-")[0]))
ds_loans[int_rate] = ds_loans[int_rate].map(lambda x: float(str(x).rstrip()[:-1])/100)
ds_loans[length] = ds_loans[length].map(lambda x: int(str(x).rstrip().split(" ")[0]))

# for col in [fico, int_rate, length]:
    # print(ds_loans[col][:5])
def base_data_plots():
    # plots.all_plots(ds_loans[fico], "Fico Scores", "no unit")
    # plots.all_plots(ds_loans[int_rate], "Interest Rates", "%")
    # plots.all_plots(ds_loans[length], "Loan Length", "months")
    fig = plt.figure("Base data")
    ax1 = fig.add_subplot(221)
    ax1.hist(ds_loans[fico])
    ax1.set_title("FICO scores")
    ax2 = fig.add_subplot(222)
    ax2.hist(ds_loans[int_rate])
    ax2.set_title("Interest Rate")
    ax3 = fig.add_subplot(223)
    ax3.hist(ds_loans[length])
    ax3.set_title("Loan Length (months)")
    plt.show()

# base_data_plots()

def scatter_matrix_plot():
    spm = pd.scatter_matrix(ds_loans, figsize=(10,10), diagonal='hist')
    plt.show()
    
scatter_matrix_plot()