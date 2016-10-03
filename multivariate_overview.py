'''
Unit2 Lesson5: Multivariate Analysis Overview
Tutorial from http://nbviewer.jupyter.org/urls/s3.amazonaws.com/datarobotblog/notebooks/multiple_regression_in_python.ipynb#appendix
'''

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

'''Linear regression with multiple regressors'''
df_adv = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
# print(df_adv.info())
# print(df_adv.head())

X = df_adv[["TV", "Radio"]]
Y = df_adv["Sales"]
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
# print(model.summary())

#other way to get the model using a formula
model = smf.ols(formula="Sales ~ TV + Radio", data=df_adv).fit()
# print(model.summary())


'''how to handle categorical data'''
df = pd.read_csv("http://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data", index_col=0)
X = df.copy() #famhist is whether family has history of coronary artery disease or not
y = X.pop("chd") #chd = chronic heart disease
# print(X.head())
# print(y.groupby(X.famhist).mean())

df["famhist_ord"] = pd.Categorical(df["famhist"]).labels
model = smf.ols(formula="chd ~ famhist_ord", data=df).fit()
#OR
model = smf.ols(formula="chd ~ C(famhist)", data=df).fit()
# print(model.summary())

''' '''
df = pd.read_csv('randhie.csv')
# print(df.info())
df["logincome"] = np.log1p(df.income)
# print(df[['mdvis', 'logincome', 'hlthp']].tail())