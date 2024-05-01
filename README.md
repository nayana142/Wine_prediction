# Wine Quality Prediction 

![image](https://github.com/nayana142/Wine_prediction/assets/120770261/0f7ad535-f55c-4e6b-9287-bc691961a9a8)

## Introduction
 Welcome to the Wine Quality Prediction application powered by Streamlit! This application utilizes machine learning techniques
 to predict the quality of wine based on various features. Users can input the characteristics of a wine sample, and the application
 will provide a prediction of its quality.

## Dataset
The prediction model is trained on a dataset containing the following features:

    Fixed Acidity
    Volatile Acidity
    Citric Acid
    Residual Sugar
    Chlorides
    Free Sulfur Dioxide
    Total Sulfur Dioxide
    Density
    pH
    Sulphates
    Alcohol
The target variable is 'Quality', which represents the quality rating of the wine.

## Installation
To run this Streamlit application locally, follow these steps:

      1.Clone this repository to your local machine.
      2.Navigate to the project directory.
## Install the required dependencies by running:
Copy code

    pip install -r requirements.txt
## Usage
After installing the dependencies, launch the Streamlit application by executing the following command:
arduino

    streamlit run app.py
This will start a local server, and the application will open in your default web browser.

## Features
     * Input Form: Users can fill out a form providing details such as fixed acidity, volatile acidity, citric acid, etc., of the wine sample.
     * Prediction: The application utilizes a predictive model to estimate the quality rating of the wine based on the provided information.
     * Visualization: Visual representations such as graphs or charts may be provided to illustrate the relationship between input features and wine quality.
     * Technologies Used
     * Streamlit: Streamlit is used as the main framework for building the interactive web application.
     * Python: The backend logic and predictive modeling are implemented using Python.
     * Machine Learning: Predictive modeling techniques are employed to predict wine quality based on the input features.
