from datetime import datetime 
import pandas as pd 

#Read file
df = pd.read_csv("/Users/rodrigohofer/downloads/dataset.csv", delimiter=',')

#Primera salida con las fechas co formato ISO 
df['summary_date'] = pd.to_datetime(df['summary_date'], format='%Y.%m.%d').dt.date
df['summary_date'] = df['summary_date'].map(lambda x: x.isoformat())

print('Reporte A')
print(df)
print('---------------')
print('---------------')

#Segunda salida agrupado por campaign
df['CTR'] = df['clicks'] / df['impressions']
df['CPI'] = df['spend'] / df['installs']

df_groupby = df[["campaign_name", "impressions","clicks","installs","spend","CTR","CPI"]]
df_groupby = df_groupby.groupby(by="campaign_name").sum()


print('Reporte B y C')
print(df_groupby)
print('---------------')
print('---------------')