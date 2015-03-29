
'''
Write a script called "chi_squared.py" that 
* loads the data, 
* cleans it, 
* performs the chi-squared test, 
* and prints the result. 
Push your code to Github and enter the link below.
'''


import pandas as pd
from scipy import stats
import collections

#loads the data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# cleans it
loansData.dropna(inplace=True)

#get the variable we will perform chi squared on
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

#get the chi squared stuff
chi, p = stats.chisquare(freq.values())

#print the result
print "The chi squared value is " + str(chi) + " and the p value is " + str(p) +"."

