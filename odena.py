import pandas as pd



df = pd.read_csv('results21.csv')

df=df.sort_values(by=['mse'])

df.to_csv('resultsOrd21.csv',index=False)
