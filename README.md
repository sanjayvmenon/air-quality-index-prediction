# Air Quality Index (AQI) Prediction

## Project Overview
This project predicts the Air Quality Index (AQI) based on pollutant values. It includes a variety of algorithms and models that help analyze and predict the AQI. The model was trained using a dataset containing pollutant values, and the goal is to use it to classify the AQI as one of the following categories:
- Good
- Satisfactory
- Moderate
- Poor
- Very Poor
- Severe

## Project Structure
This repository is divided into multiple branches, each representing different stages of the project:

### Main Branch:
- Contains the original dataset (before any modifications).
  
### caqip1 Branch:
- Contains the cleaned dataset (with unnecessary columns removed).
- Includes the code to preprocess the data.

### caqip2 Branch:
- Contains the outlier-removed dataset.
- Includes the outlier removal code.

### caqip3 Branch:
- Contains the code for model training.
- A joblib file will be created once the code is run
  
### caqip4 Branch:
- Contains the Flask web application that allows users to input pollutant values directly and get AQI classification predictions.
- This branch includes the code for the Flask API and related files.

## Installation Instructions

### Clone the Repository:
Clone this repository to your local machine using:
```bash
git clone https://github.com/your-username/air_quality_index_prediction.git
