import pandas as pd



df = pd.read_csv('results41.csv')

df=df.sort_values(by=['mse'])

df.to_csv('resultsOrd41.csv',index=False)
