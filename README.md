# Time Series Analysis and Prediction for Water Quality Index

This repository is dedicated to a time series analysis project that focuses on predicting and assessing water quality over time using various environmental parameters. The project implements advanced time series forecasting models such as VAR, Auto ARIMA, and SARIMA, aiming to predict the **Canadian Council of Ministers of the Environment (CCME) Water Quality Index (WQI)** across different seasons. This project not only evaluates seasonal trends in water quality but also provides a clear and actionable metric for understanding environmental health.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Models](#models)
- [Water Quality Index Calculation](#water-quality-index-calculation)
- [Performance Metric](#performance-metric)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributors](#contributors)

---

## Project Overview

This project aims to develop a seasonal water quality prediction framework using time series models that analyze key environmental parameters. By forecasting these parameters and calculating the **CCME WQI** for each season, this analysis allows us to monitor and understand how water quality varies across seasons over multiple years. The models are trained on multi-year historical data, enabling them to capture both short-term and long-term trends, particularly focusing on seasonal variations that impact water potability.

The seasonal analysis covers:
- **Pre-Monsoon (March - May)**
- **Monsoon (June - September)**
- **Post-Monsoon (October - November)**
- **Winter (December - February)**

---

## Dataset

The dataset (`Dataset.xlsx`) provides comprehensive information on water quality parameters over multiple years, including details on physicochemical properties essential for assessing water safety. Each row represents a seasonal record of water quality, while the columns detail individual measurements.

### Key Parameters:
1. **pH**: Indicates the acidity or alkalinity of water.
2. **Electrical Conductivity (EC)**: Reflects the ion concentration, measuring water’s ability to conduct electricity.
3. **Total Alkalinity (TA)**: Shows water’s capacity to buffer against pH changes.
4. **Chlorides (Cl)**: Indicates the concentration of chloride ions, often affecting taste and corrosion.
5. **Total Dissolved Solids (TDS)**: The total concentration of dissolved substances in water.
6. **Total Suspended Solids (TSS)**: Measures undissolved particles in water, affecting turbidity.
7. **Dissolved Oxygen (DO)**: Essential for aquatic life, indicates water quality.
8. **Biochemical Oxygen Demand (BOD)**: Shows the amount of organic pollution present.
9. **Chemical Oxygen Demand (COD)**: Measures the total pollutants, both organic and inorganic.
10. **Turbidity (Turb)**: Reflects water clarity, influenced by suspended solids and organic matter.

#### Thresholds:
Thresholds for each parameter are defined in `Threshold Values.txt`, aligning with water quality standards used in environmental assessment. These thresholds help calculate the WQI and determine if water meets potability standards.

---

## Features

### Data Preprocessing
1. **Missing Values**: Missing values are filled using mean imputation, ensuring a complete dataset for time series modeling.
2. **Standardization**: Features are standardized to improve model performance, making all variables comparable on a common scale.
3. **Seasonal Encoding**: Seasonal categories are created to differentiate trends in water quality based on seasonal patterns (Pre-Monsoon, Monsoon, Post-Monsoon, Winter).

### Feature Engineering
1. **Rolling Averages**: Moving averages for each parameter help smooth data and emphasize long-term trends.
2. **Lagged Variables**: Previous values of key parameters are included as additional features, allowing models to understand temporal dependencies.
3. **Seasonal and Temporal Lags**: Features capturing the seasonal effect over previous periods are added to enrich model training data.

---

## Models

The project implements several time series models, each tailored for capturing different aspects of temporal data. Scripts are provided for each model, allowing focused and individual analysis.

### 1. Vector Auto-Regressive (VAR)
   - **Objective**: Captures interdependencies among multiple environmental variables.
   - **Suitability**: Best suited for datasets where variables are mutually influencing each other. For example, DO and BOD have inverse relationships that VAR can capture.
   - **Script**: `VAR.py`

### 2. Auto ARIMA
   - **Objective**: Automatically identifies the optimal ARIMA configuration by testing different p, d, and q parameters.
   - **Suitability**: Handles trend and seasonality effectively, fitting well with data showing repetitive seasonal patterns.
   - **Script**: `AutoArima.py`

### 3. Seasonal AutoRegressive Integrated Moving Average (SARIMA)
   - **Objective**: Extends ARIMA by including seasonal terms to capture periodic fluctuations.
   - **Suitability**: Ideal for data with clear seasonal patterns, making it suitable for forecasting water quality across seasons.
   - **Script**: `Sarima.py`

Each model is designed to capture unique characteristics of time series data, providing a comprehensive analysis of water quality trends over time.

---

## Water Quality Index Calculation

The **CCME Water Quality Index (WQI)** provides a single score to summarize water quality based on specific thresholds for each parameter. This consolidated index offers an intuitive metric to interpret water quality, facilitating a straightforward comparison across seasons and years.

### Calculation Process:
The WQI is calculated by:
1. **Parameter Threshold Comparison**: Each parameter’s value is compared against the threshold in `Threshold Values.txt`.
2. **Scoring**: Scores are assigned based on the number of parameters meeting potability standards, with penalties for each parameter that fails to meet its threshold.
3. **Aggregation**: The scores are averaged and normalized to produce a WQI score ranging from 0 to 100.

### Parameter Thresholds:

| Parameter         | Threshold            |
|-------------------|----------------------|
| pH                | 6.5 - 8.5            |
| EC                | ≤1200 μS/cm          |
| TA                | ≤150 mg/L            |
| Cl                | 150 - 650 mg/L       |
| TDS               | ≤2100 mg/L           |
| TSS               | ≤150 mg/L            |
| DO                | ≥5 mg/L              |
| BOD               | ≤6 mg/L              |
| COD               | ≤200 mg/L            |
| Turbidity         | ≤10 NTU              |

The calculated WQI scores are used to monitor changes in water quality over different seasons, providing insights into the safety of water resources.

---

## Performance Metric

### Accuracy:
The accuracy metric is used to assess how well each model predicts seasonal water quality values. Accuracy is computed based on the proportion of correct predictions, giving a straightforward indication of each model’s effectiveness in forecasting.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AzimNahin/Time-Series-Prediction.git
2. Navigate to the project directory:
   ```bash
   cd Time-Series-Prediction
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt

---

## Usage

### Steps for Analysis
1. **Run Time Series Models**:
   - Execute individual model scripts for predictions:
     - **Auto ARIMA**: Run `autoArima.py` to forecast parameters using Auto ARIMA.
     - **SARIMA**: Execute `Sarima.py` for SARIMA-based seasonal forecasting.
     - **VAR**: Use `VAR.py` to analyze inter-variable dependencies.

2. **Compute WQI**:
   - Run `calculate_wqi.py` to calculate the WQI based on predicted values from each model, applying thresholds defined in `Threshold Values.txt`.

3. **Visualize Results**:
   - Seasonal WQI scores and trends are visualized, showing variations over time:
     - **Auto ARIMA**: Results in `CCMEWQI_AutoArima.png`
     - **SARIMA**: Results in `CCMEWQI_Sarima.png`
     - **VAR**: Results in `CCMEWQI_VAR.png`

4. **Comprehensive Analysis**:
   - Use `Main.ipynb` for an end-to-end analysis, including data preprocessing, model training, WQI calculation, and visualization.

---

## Results

### Key Findings
- **Auto ARIMA**: Efficient in capturing trends with minimal seasonal adjustments, yielding smooth WQI predictions.
- **SARIMA**: Provides strong seasonal forecasting, accurately representing fluctuations across different time periods.
- **VAR**: Captures the relationships among multiple parameters, reflecting interactions between water quality indicators.

### Visual Summary
- **Auto ARIMA Results**: `CCMEWQI_AutoArima.png`
- **SARIMA Results**: `CCMEWQI_Sarima.png`
- **VAR Results**: `CCMEWQI_VAR.png`

These visualizations provide a temporal overview of water quality, illustrating how it fluctuates within and across seasons.

### Observations
- **Seasonal Peaks and Troughs**: Each model captures seasonal peaks and troughs in water quality, highlighting potential stress periods on water resources.
- **Inter-Parameter Dependencies**: VAR demonstrates the effect of interactions, such as the inverse relationship between BOD and DO, furthering our understanding of water quality dynamics.

---

## Contributors
- [Azim Nahin](https://github.com/AzimNahin)
- [Sadman1702042](https://github.com/Sadman1702042)
  
---

