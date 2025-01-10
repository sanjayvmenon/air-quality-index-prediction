import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("cleaned_city_day.csv")
# # print(df.head())
# Outlier removal
# Array of pollutant columns
pollutants = ['PM2.5', 'PM10', 'NOx', 'SO2', 'CO', 'O3', 'NH3']

for pollutant in pollutants:
    Q1 = df[pollutant].quantile(0.25)  # First quartile (25th percentile)
    Q3 = df[pollutant].quantile(0.75)  # Third quartile (75th percentile)
    IQR = Q3 - Q1  # Interquartile Range
    lower_bound = Q1 - 1.5 * IQR  # Lower limit
    upper_bound = Q3 + 1.5 * IQR  # Upper limit
    
    cleaned_data = df[(df[pollutant] >= lower_bound) & (df[pollutant] <= upper_bound)]

# Print the updated DataFrame after removing outliers
print(cleaned_data.head())
cleaned_data.to_csv("cleaned_city_day_no_outliers.csv", index=False)