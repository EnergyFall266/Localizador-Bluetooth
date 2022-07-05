import pandas as pd



df = pd.read_csv('erros_coord.csv')

df=df.sort_values(by=['CoordX','CoordY'])

df.to_csv('erroCoordOrd.csv',index=False)
