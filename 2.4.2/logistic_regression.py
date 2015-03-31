

import pandas as pd
import statsmodels.api as sm

#import and clean data
loansData = pd.read_csv('loansData_clean.csv')

#New columns: a binary on if the interest rate is over 12, and an intercept constant
loansData['interestGreaterThan12'] = loansData['Interest.Rate'].map(lambda x : x >= 12)
loansData['intercept'] = 1

ind_vars = ['intercept', 'FICO.Score', 'Amount.Requested']


logit = sm.Logit(loansData['interestGreaterThan12'], loansData[ind_vars])
result = logit.fit()
coeff = result.params

from math import exp
def p_of_x (coeff, FICO, loanAmount):
	return 1/(1 + exp(coeff['intercept'] + coeff['FICO.Score']*(FICO) + coeff['Amount.Requested']*(loanAmount)))

print 'Probability of getting loan is ' + p_of_x(coeff, 720, 10000)