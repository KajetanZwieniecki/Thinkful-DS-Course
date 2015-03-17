
'''
Write a script called "prob.py" that outputs frequencies, 
as well as creates and saves a boxplot, 
a histogram, 
and a QQ-plot 
for the data in this lesson. 
Make sure your plots have names that are reasonably descriptive. 
Push your code to GitHub and enter the link below.
'''

#import the libraries we need
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

#Our data
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

plt.boxplot(x)
plt.savefig("boxplot.png")

plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("histogram.png")

plt.figure()
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("qqplot.png")

