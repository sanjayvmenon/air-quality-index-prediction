from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved Random Forest model
model = joblib.load('random_forest_aqi_model.joblib')

# Air quality classification based on AQI
def classify_air_quality(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Satisfactory"
    elif aqi <= 200:
        return "Moderate"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get pollutant values from the form
    try:
        pm25 = float(request.form['pm25'])
        pm10 = float(request.form['pm10'])
        nox = float(request.form['nox'])
        so2 = float(request.form['so2'])
        co = float(request.form['co'])
        o3 = float(request.form['o3'])
        nh3 = float(request.form['nh3'])
    except ValueError:
        return "Please enter valid numeric values for pollutants.", 400
    
    # Prepare feature array for prediction
    features = np.array([[pm25, pm10, nox, so2, co, o3, nh3]])

    # Predict the AQI
    predicted_aqi = model.predict(features)[0]

    # Classify the air quality
    air_quality = classify_air_quality(predicted_aqi)

    return render_template('result.html', aqi=predicted_aqi, air_quality=air_quality)

if __name__ == '__main__':
    app.run(debug=True)