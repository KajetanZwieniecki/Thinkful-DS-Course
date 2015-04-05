
'''
Load the Lending Club Statistics.

Use income (annual_inc) to model interest rates (int_rate).

Add home ownership (home_ownership) to the model.

Does that affect the significance of the coefficients in the original model? 
+ Try to add the interaction of home ownership and incomes as a term. How does this impact the new model?
'''


import pandas as pd
import statsmodels.api as sm
import numpy as np

#import and clean data
loansData = pd.read_csv('loansData_aggregate.csv', na_values = 'nan')

#remove NA's
loansData.dropna(subset=['int_rate'], inplace = True) 
#loansData = loansData[loansData['int_rate'].map(lambda x: str(x) != 'nan')]
loansData.dropna(subset=['annual_inc'], inplace = True) 
#loansData = loansData[loansData['annual_inc'].map(lambda x: str(x) != 'nan')]
loansData.dropna(subset=['home_ownership'], inplace = True) 
#loansData = loansData[loansData['home_ownership'].map(lambda x: str(x) != 'nan')]

#get interest rate column that will serve as our dependent variable
loansData['int_rate'] = loansData['int_rate'].map(lambda x : float(x.replace("%", "")))

int_rate = loansData['int_rate']
annual_inc =  loansData['annual_inc']

'''
The First linear regression
'''

# The dependent variable
y = np.matrix(int_rate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(annual_inc).transpose()

x = np.column_stack([x1])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

#print results
print 'First model (income on rate)'
print 'Coefficients: ', f.params[1]
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

#interestingly the result is postive, likely because the size of the loan asked for. 
#lets test this:
# Need a second independent variable in loan amount
loan_amnt = loansData['loan_amnt']
x2 = np.matrix(loan_amnt).transpose()

x = np.column_stack([x1, x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

#print results
print 'Second model (income and amount on rate)'
print 'Coefficients: ', f.params[1:3]
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

'''
The multivariate regression
'''
loansData = loansData.join(pd.get_dummies(loansData['home_ownership']))

housecategory = ['ANY', 'MORTGAGE']

home_ownership_c1 = loansData['ANY']
home_ownership_c2 = loansData['MORTGAGE'] 
home_ownership_c3 = loansData['NONE']
home_ownership_c4 = loansData['OTHER']
home_ownership_c5 = loansData['OWN']

np.matrix(loansData[housecategory[0]]).transpose() 

x3 = np.matrix(home_ownership_c1).transpose() 
x4 = np.matrix(home_ownership_c2).transpose() 
x5 = np.matrix(home_ownership_c3).transpose() 
x6 = np.matrix(home_ownership_c4).transpose() 
x7 = np.matrix(home_ownership_c5).transpose() 

x = np.column_stack([x1, x3, x4, x5, x6, x7])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print 'Second model (income and home ownership on rate)'
print 'Coefficients: ', f.params[1:7]
print 'Coefficient order: income, Any, Mortgage, None, Other, Own'
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

'''
Third model: interaction of income and owenrship
'''
home_ownership_c6 = loansData['ANY'] * loansData['annual_inc']
home_ownership_c7 = loansData['MORTGAGE'] * loansData['annual_inc'] 
home_ownership_c8 = loansData['NONE'] * loansData['annual_inc']
home_ownership_c9 = loansData['OTHER'] * loansData['annual_inc']
home_ownership_c10 = loansData['OWN'] * loansData['annual_inc']

x8 = np.matrix(home_ownership_c6).transpose() 
x9 = np.matrix(home_ownership_c7).transpose() 
x10= np.matrix(home_ownership_c8).transpose() 
x11 = np.matrix(home_ownership_c9).transpose() 
x12 = np.matrix(home_ownership_c10).transpose() 


x = np.column_stack([x1, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print 'Third model (income and home ownership and cross product on rate)'
print 'Coefficients: ', f.params[1:12]
print 'Coefficient order: income, Any, Mortgage, None, Other, Own, Any*inc, Mortgage*inc, None*inc, Other*inc, Own*inc'
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

