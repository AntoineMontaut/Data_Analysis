'''
Unit3 Lesson4: Logistic Regression
'''

import pandas as pd
import statsmodels as sm

ds_loans = pd.read_csv("loansData_clean.csv")
# print(ds_loans.head(5))
print(ds_loans.info())
ds_loans = ds_loans.dropna()

#IT_TF=0 when IR<12%, IR_TF = 1 when IR>12%
ds_loans["IR_TF"] = ds_loans["Interest.Rate"].map(lambda x: 1 if x>=.12 else 0)
# print(ds_loans[["Interest.Rate", "IR_TF"]].head(5))
# print(ds_loans[["Interest.Rate", "IR_TF"]][ds_loans["Interest.Rate"]>0.12].head(5))
# print(ds_loans[["Interest.Rate", "IR_TF"]][ds_loans["Interest.Rate"]<0.12].head(5))

#statsmodels need an intercept column in the DataFrame
ds_loans["Intercept"] = 1.0

