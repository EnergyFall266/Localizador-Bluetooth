import pandas as pd
from sqlalchemy import false


df = pd.read_csv('coleta.csv')

df=df.sort_values(by=['CoordX', 'CoordY','Address'])

df.to_csv('ordenado.csv',index=False)
