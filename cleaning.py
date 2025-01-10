import pandas as pd
df=pd.read_csv("city_day.csv")
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

# dropping columns

df.drop(columns=["City","Date","Benzene","Toluene","Xylene","NO","NO2","AQI_Bucket"],inplace=True)
df.fillna(df.mean(),inplace=True)
# print(df.head())
# print(df.isnull().sum())
print(df.isnull().sum())
df.to_csv("cleaned_city_day.csv",index=False)
