# Time Series Analysis

This repository contains scripts and resources for analyzing time series data, including forecasting models such as Auto ARIMA, SARIMA, and VAR. The project utilizes a dataset to forecast various environmental parameters and compares them against defined thresholds.

## Table of Contents
- [Overview](#overview)
- [Files](#files)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project aims to forecast environmental parameters like pH, EC, TDS, etc., using time series models. Seasonal data comparisons are made against thresholds specified in `Threshold Values.txt`.

## Files
- **autoArima.py**: Script for forecasting using the Auto ARIMA model.
- **Sarima.py**: Implements SARIMA for seasonal data forecasting.
- **VAR.py**: Conducts multivariate analysis using the VAR model.
- **Dataset.xlsx**: Contains the time series data with environmental parameters.
- **Threshold Values.txt**: Lists thresholds for different parameters across various seasons.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Time-Series-Analysis.git
