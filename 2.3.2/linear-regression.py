

import pandas as pd

#import data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#modify columns
loansData['Interest.Rate'].map(lambda x : float(x.replace("%", "")))
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x : int(x.split("-")[0]))

#create the scatter matrix
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))