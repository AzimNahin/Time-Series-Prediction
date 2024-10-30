# Time Series Prediction and Calculate CCME-WQI

This repository contains scripts and resources for analyzing time series data, including forecasting models such as Auto ARIMA, SARIMA, and VAR. The project utilizes a dataset to forecast various environmental parameters and compares them against defined thresholds for seasonal evaluation. Seasonal CCME-WQI has also been calculated.

## Table of Contents
- [Overview](#overview)
- [Files](#files)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributors](#contributors)

## Overview
This project aims to forecast environmental parameters such as pH, EC, TDS, etc., using time series models. Data is analyzed for seasonal variations (e.g., Pre-monsoon, Monsoon) and compared against specified thresholds found in `Threshold Values.txt`.

## Files
- **Main.ipynb**: Applies models like Prophet, ARIMA, SARIMAX, and VAR to forecast trends, evaluates model performance using metrics like MAE, MSE, and RMSE, and visualizes the actual versus predicted values.
- **autoArima.py**: Script for forecasting using the Auto ARIMA model.
- **Sarima.py**: Implements SARIMA for seasonal data forecasting.
- **VAR.py**: Conducts multivariate analysis using the VAR model.
- **Dataset.xlsx**: Contains the time series data with environmental parameters.
- **Threshold Values.txt**: Lists thresholds for different parameters across various seasons.
- **requirements.txt**: Lists all required Python libraries for the project.
- **README.md**: Provides an overview and instructions for the project.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AzimNahin/Time-Series-Analysis.git
2. Navigate to the project directory:
   ```bash
   cd Time-Series-Analysis
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt

## Usage
1. Load the dataset using one of the provided scripts (e.g., `autoArima.py`, `Sarima.py`, or `VAR.py`).
2. Run the selected script to perform time series forecasting.
3. Evaluate the model results by comparing forecasts with seasonal threshold values found in `Threshold Values.txt`.

## Technologies
- **Python**: Core programming language for analysis and forecasting.
- **Libraries**: 
  - `pandas` for data manipulation and analysis.
  - `numpy` for numerical operations.
  - `matplotlib` and `seaborn` for data visualization.
  - `statsmodels` for statistical modeling and forecasting.
  - `pmdarima` for Auto ARIMA model.
  - `openpyxl` for handling Excel files.

## Contributors
- [Azim Nahin](https://github.com/AzimNahin)
- [Sadman1702042](https://github.com/Sadman1702042)
