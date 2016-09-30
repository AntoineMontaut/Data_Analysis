'''
Unit2 Lesson3: Linear Regression and Correlation
'''

import pandas as pd
import plots
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

ds_loans = pd.read_csv("loansData.csv")
# print(ds_loans.head(5))
print(ds_loans.info())
ds_loans.dropna()

fico = "FICO.Score"
fico_name = fico.replace(".", " ")
int_rate = "Interest.Rate"
int_rate_name = int_rate.replace(".", " ")
length = "Loan.Length"
length_name = length.replace(".", " ")
amt_req = "Amount.Requested"
amt_req_name = amt_req.replace(".", " ")
income = "Monthly.Income"
income_name = income.replace(".", " ")

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

base_data_plots()

def scatter_matrix_plot():
    # spm = pd.scatter_matrix(ds_loans, figsize=(10,10), diagonal='hist', alpha=0.05)
    spm_reduced = pd.scatter_matrix(ds_loans[[fico, int_rate, length, amt_req, income]], figsize=(10,10), diagonal='hist', alpha=0.05)
    plt.show()
    
scatter_matrix_plot()

#y=interest rate, x1=FICO score, x2=Loan amount
#transpose to have data in a vertical vector form
y = np.matrix(ds_loans[int_rate]).transpose()
x1 = np.matrix(ds_loans[fico]).transpose()
x2 = np.matrix(ds_loans[amt_req]).transpose()
#create a single matrix from x1 and x2
x = np.column_stack([x1, x2])
#add a constant to x to have the full equation: y = a1*x1 + a2*x2 + b
X = sm.add_constant(x)

#create the linear model and fit
model = sm.OLS(y, X).fit() #OLS: Ordinary Least Square
print("\n")
print(model.summary())