import pandas as pd
df=pd.read_csv("cleaned_city_day_no_outliers.csv")
from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
# from sklearn.linear_model import LinearRegression
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.svm import SVR
from sklearn.metrics import accuracy_score,mean_squared_error, r2_score
import joblib

X = df[['PM2.5', 'PM10', 'NOx', 'SO2', 'CO', 'O3', 'NH3']]
y = df['AQI']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# random forest

rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
print("\nRandom Forest Regressor:")
print(f"Mean Squared Error: {mse_rf}")
print(f"R-squared: {r2_rf}")


# Save the model to a .joblib file
joblib.dump(rf_model, 'random_forest_aqi_model.joblib')
print("Model saved as random_forest_aqi_model.joblib!")

