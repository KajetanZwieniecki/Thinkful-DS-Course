

import numpy as np
import pandas as pd
import statsmodels.api as sm

#import and clean data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x : float(x.replace("%", "")))
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x : int(x.split("-")[0]))

loansData.to_csv('loansData_clean.csv', header=True, index=False)

print 'done'

###The below was part of the orignal script
'''
#We'll use the cleaned loansData DataFrame we've been using and extract some columns
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

#When we extract a column from a DataFrame, it's returned as a Series datatype. You want to reshape the data like this
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

#Now you want to put the two columns together to create an input matrix 
x = np.column_stack([x1,x2])

#Now we create a linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

#And output the results:
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared
'''