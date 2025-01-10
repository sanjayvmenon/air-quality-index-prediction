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
```
## Install Dependencies

### Create a Virtual Environment

### Activate the Virtual Environment

### Install Required Libraries

- pandas
- scikit-learn
- flask
- joblib
- matplotlib (if using for visualizations)
- numpy (if using for numerical operations)

## Running the Model

Run the model.py code which will create a joblib file 

## Running the Flask Application

- To use the Web Application run the app.py file
- Visit http://127.0.0.1:5000/ in your browser to input pollutant values and get the AQI prediction.

## Notes

- The joblib file is not included in the repository to keep the repository size manageable. You can regenerate it by running the training script.
- You can refer to the respective branches for different stages of the project.
