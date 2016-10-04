'''
Unit2 Lesson5: Multivariate Analysis Overview
Tutorial from http://nbviewer.jupyter.org/urls/s3.amazonaws.com/datarobotblog/notebooks/multiple_regression_in_python.ipynb#appendix
'''

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

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
income_linspace = np.linspace(df.logincome.min(), df.logincome.max(), 100)
est = smf.ols(formula="mdvis ~ logincome + hlthp", data=df).fit()
# print(model.summary())

# fig = plt.figure("Number of visits depending on income and health status")
# plt.subplot(2,2,1)
# plt.scatter(df.logincome, df.mdvis, alpha=0.3)
# plt.xlabel('Log income')
# plt.ylabel('Number of visits')
# plt.plot(income_linspace, est.params[0] + est.params[1] * income_linspace + est.params[2] * 0, 'r')
# plt.plot(income_linspace, est.params[0] + est.params[1] * income_linspace + est.params[2] * 1, 'g')

est = smf.ols(formula="mdvis ~ hlthp * logincome", data=df).fit()
# print(est.summary())

# plt.subplot(2,2,2)
# plt.scatter(df.logincome, df.mdvis, alpha=0.3)
# plt.xlabel('Log income')
# plt.ylabel('Number of visits')
# plt.plot(income_linspace, est.params[0] + est.params[1] * 0 + est.params[2] * income_linspace + \
# est.params[3]* 0 * income_linspace, 'r')
# plt.plot(income_linspace, est.params[0] + est.params[1] * 1 + est.params[2] * income_linspace + \
# est.params[3]* 1 * income_linspace, 'g')
# plt.show()

# load the boston housing dataset - median house values in the Boston area
df = pd.read_csv('http://vincentarelbundock.github.io/Rdatasets/csv/MASS/Boston.csv')
# print(df.info())

# plot lstat (% lower status of the population) against median value
# lstat = "proportion of the adults without some high school education and proportion of male workes classified as laborers"
plt.figure(figsize=(6 * 1.618, 6))
plt.scatter(df.lstat, df.medv, s=10, alpha=0.3)
plt.xlabel('lstat')
plt.ylabel('medv')

x = pd.DataFrame({'lstat': np.linspace(df.lstat.min(), df.lstat.max(), 100)})

poly_1 = smf.ols(formula='medv ~ 1 + lstat', data=df).fit()
# print(poly_1.summary())
plt.plot(x.lstat, poly_1.predict(x), 'b-', label='Poly n=1 $R^2$=%.2f' % poly_1.rsquared, alpha=0.9)

poly_2 = smf.ols(formula='medv ~ 1 + lstat + I(lstat**2.0)', data=df).fit()
plt.plot(x.lstat, poly_2.predict(x), 'g-', label='Poly n=2 $R^2$=%.2f' % poly_2.rsquared, alpha=0.9)

poly_3 = smf.ols(formula='medv ~ 1 + lstat + I(lstat**2.0) + I(lstat**3.0)', data=df).fit()
plt.plot(x.lstat, poly_3.predict(x), '-r', label='Poly n=3 $R^2$=%.2f' % poly_3.rsquared, alpha=0.9)

plt.legend()
plt.show()