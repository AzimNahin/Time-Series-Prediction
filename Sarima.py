
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

file_path = 'Dataset.xlsx'
data = pd.read_excel(file_path)
data = pd.DataFrame(data)

data['Date'] = pd.to_datetime(data['Date'])

for column in data.columns:
    #data[column] = data[column].interpolate(method='linear')
    data[column].fillna(data[column].mean(), inplace=True)
    #data[column].fillna(data[column].mode()[0], inplace=True)

#forward fill
#data = data.fillna(method='ffill')

data.set_index('Date', inplace=True)

forecast_steps = 24  # 24 months to cover 2020 and 2021

# Initialize an empty DataFrame to store predictions
sarima_predictions_full = pd.DataFrame()

# Loop over each column in the data (each feature)
for column in data.columns:

    # Fit SARIMA model (P=1, D=1, Q=1, S=12 for yearly seasonality as an example)
    model = SARIMAX(data[column], 
                    order=(1, 1, 1), 
                    seasonal_order=(1, 1, 1, 12))
    
    fitted_model = model.fit(disp=True)
    
    # Forecast future values for 24 months
    forecast = fitted_model.forecast(steps=forecast_steps)
    
    # Store the forecasted values
    sarima_predictions_full[column] = forecast

# Set the index for predictions to the 2020-2021 period
sarima_predictions_full.index = pd.date_range(start='2020-01-01', periods=forecast_steps, freq='MS')


reference_values = {
    'pH': (6.5, 8.5),
    'EC': 1200,
    'TA': 150,
    'Cl': (150, 650),
    'TDS': 2100,
    'TSS': 150,
    'DO': 5,
    'BOD': 6,
    'COD': 200,
    'Turb': 10
}


def calculate_excursion_single(value, threshold, is_upper_bound):
    
    if value == 0:
        
        # Avoid division by zero, return 0 or an appropriate value
        epsilon = 0.0001 
        return (threshold /(value + epsilon)) - 1
        
    if is_upper_bound:
        # If the value exceeds the upper bound, calculate the excursion normally
        return (value / threshold) - 1 
    else:
        # If the value is below the lower bound, calculate the excursion
        return (threshold / value) - 1



def calculate_ccme_wqi(predicted_df, reference_values,lowerBoundFeatures):

    scope_failures = 0
    frequency_failures = 0
    sum_of_excursions = 0
    total_tests = 0

    for param in reference_values:
        
        # If parameter has both lower and upper bounds (e.g., pH, Cl)
        if isinstance(reference_values[param], tuple):
            
            lower_bound, upper_bound = reference_values[param]
            
            # Scope failure check
            if predicted_df[(predicted_df[param] < lower_bound) | (predicted_df[param] > upper_bound)].shape[0] > 0:
                scope_failures += 1
            
            # Frequency failure check
            frequency_failures += predicted_df[param].apply(lambda x: x < lower_bound or x > upper_bound).sum()
            
            # Sum of excursions
            sum_of_excursions += predicted_df[param].apply(
                lambda x: calculate_excursion_single(x, upper_bound, True) if x > upper_bound 
                else calculate_excursion_single(x, lower_bound, False) if x < lower_bound 
                else 0
            ).sum()
        
        # For parameters with only upper bounds (e.g., TDS, COD)
        elif param not in lowerBoundFeatures:  # Add lower-bound parameters like 'DO' here explicitly
            upper_bound = reference_values[param]
            
            # Scope failure check
            if predicted_df[predicted_df[param] > upper_bound].shape[0] > 0:
                scope_failures += 1
            
            # Frequency failure check
            frequency_failures += predicted_df[param].apply(lambda x: x > upper_bound).sum()
            
            # Sum of excursions
            sum_of_excursions += predicted_df[param].apply(
                lambda x: calculate_excursion_single(x, upper_bound, True) if x > upper_bound else 0
            ).sum()
        
        # For parameters with only lower bounds (e.g., DO)
        elif param in lowerBoundFeatures:  # You can add other lower-bound-only parameters here
            lower_bound = reference_values[param]
            
            # Scope failure check
            if predicted_df[predicted_df[param] < lower_bound].shape[0] > 0:
                scope_failures += 1
            
            # Frequency failure check
            frequency_failures += predicted_df[param].apply(lambda x: x < lower_bound).sum()
            
            # Sum of excursions
            sum_of_excursions += predicted_df[param].apply(
                lambda x: calculate_excursion_single(x, lower_bound, False) if x < lower_bound else 0
            ).sum()

        total_tests += predicted_df[param].notnull().sum()

    # Calculate F1, F2, F3, and CCME WQI
    F1 = (scope_failures / len(reference_values)) * 100
    F2 = (frequency_failures / total_tests) * 100
    nse = sum_of_excursions / total_tests
    F3 = (nse / (0.01 * nse + 0.01))

    ccme_wqi = 100 - (np.sqrt(F1**2 + F2**2 + F3**2) / 1.732)
    
    return ccme_wqi


df = pd.concat([data,sarima_predictions_full])
df.index.name = 'Date'
df.reset_index(inplace=True)

# Convert 'Date' to datetime and extract 'Year' and 'Month'
df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df.loc[df['Date'].dt.month == 12, 'Year'] = df['Date'].dt.year + 1

df['Month'] = df['Date'].dt.month_name()

# Map months to seasons
season_order = ['Winter', 'Pre Monsoon', 'Monsoon', 'Post Monsoon']

season_mapping = {
    'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
    'March': 'Pre Monsoon', 'April': 'Pre Monsoon', 'May': 'Pre Monsoon',
    'June': 'Monsoon', 'July': 'Monsoon', 'August': 'Monsoon', 'September': 'Monsoon',
    'October': 'Post Monsoon', 'November': 'Post Monsoon'
}

# Add a 'Season' column
df['Season'] = df['Month'].map(season_mapping)
df['Season'] = pd.Categorical(df['Season'], categories=season_order, ordered=True)

lowerBoundFeatures = ['DO']

print(df.groupby(['Year', 'Season']))
ccmewqi_results = df.groupby(['Year', 'Season']).apply(lambda group: calculate_ccme_wqi(group, reference_values,lowerBoundFeatures))
ccmewqi_results = ccmewqi_results.sort_index(level=['Year', 'Season'])

#print(ccmewqi_results)


df['Time'] = df['Year'].astype(str) + " - " + df['Season'].astype(str)
plt.figure(figsize=(10, 6))
plt.plot(df['Time'].unique(), ccmewqi_results, marker='o', linestyle='-', color='b')

# Add labels and title
plt.xticks(rotation=45, ha='right')
plt.xlabel('Time (Year - Season)')
plt.ylabel('CCMEWQI')
plt.title('CCMEWQI Over Time (SARIMA Model)')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.savefig('CCMEWQI_Sarima.png')
plt.show()

