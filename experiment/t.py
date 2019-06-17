import pandas as pd
df=pd.DataFrame({'ID':[1,1,1,1,2,2],'time':['2012-11-12 12:23:40','2012-11-12 12:24:30','2012-11-12 12:30:40'
                         ,'2012-11-12 12:25:40','2012-11-12 12:50:40','2012-11-12 12:21:40'],
                 "number":[3,5,2,8,6,7],'q':[2,2,3,3,5,5]})
d=df[['ID','q']].groupby(['ID']).max().reset_index()
print(d)
print(df)
df['time']=pd.to_datetime(df['time'])
df=df.set_index('time').groupby("ID")['number'].resample('2T').mean().ffill().reset_index()
print(pd.merge(df,d,how = 'left',on='ID'))
