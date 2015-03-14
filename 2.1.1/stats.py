
#Requirnment
#Write a script called "stats.py" that prints the:
# mean, 
# median, 
# mode, 
# range, 
# variance, 
# and standard deviation 
#for the Alcohol and Tobacco dataset with full text 
#(ex. "The range for the Alcohol and Tobacco dataset is ...").
#Push the code to Github and enter the link below.

#Required Libraries
import pandas as pd
import scipy.stats as stats


data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.split('\n')
data = [i.split(', ') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)


for vice in ['Alcohol', 'Tobacco']:
	df[vice] = df[vice].astype(float)
	
	print 'The mean of the ' + vice + ' dataset is ' + str(df[vice].mean())
	print 'The median of the ' + vice + ' dataset is ' + str(df[vice].median())
	print 'The mode of the ' + vice + ' dataset is ' + str(stats.mode(df[vice])[0][0])
	print 'The range of the ' + vice + ' dataset is ' + str(max(df[vice]) - min(df[vice]))
	print 'The variance of the ' + vice + ' dataset is ' + str(df[vice].var())
	print 'The standard deviation of the ' + vice + ' dataset is ' + str(df[vice].std())


