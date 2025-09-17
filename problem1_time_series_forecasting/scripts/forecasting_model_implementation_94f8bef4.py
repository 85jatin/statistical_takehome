```python
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
from openpyxl import load_workbook

# Function to load data from an Excel file
def load_data(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
        return None

# Function to preprocess the data
def preprocess_data(data):
    try:
        data['week'] = pd.to_datetime(data['week'], format='%Y-%m-%d')
        data = data.set_index('week')
        data = data.asfreq('W-MON')
        data = data.fillna(method='ffill')
        return data
    except ValueError:
        print("Error: Ensure the 'week' column is in a recognizable date format.")
        return None

# Function to split the data into training and testing sets
def train_test_split(data, test_size=0.2):
    n = len(data)
    train_data = data.iloc[:int(n * (1 - test_size))]
    test_data = data.iloc[int(n * (1 - test_size)):]
    return train_data, test_data

# Function to train the SARIMAX model
def train_model(train_data):
    model = SARIMAX(train_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 52))
    model_fit = model.fit(disp=False)
    return model_fit

# Function to forecast future values
def forecast(model, steps):
    forecasted_values = model.forecast(steps=steps)
    return forecasted_values

# Function to calculate Mean Absolute Percentage Error (MAPE)
def calculate_mape(actual, predicted):
    epsilon = 1e-10
    return mean_absolute_percentage_error(actual, predicted + epsilon)

# Main execution logic
def main():
    # Load and preprocess data
    data = load_data('TimeSeries.xlsx')
    if data is not None:
        data = preprocess_data(data)
    
    # Split data into training and testing sets
    train_data, test_data = train_test_split(data)
    
    # Train the model
    model = train_model(train_data)
    
    # Validate the model
    test_forecast = forecast(model, len(test_data))
    mape = calculate_mape(test_data, test_forecast)
    print(f"MAPE: {mape * 100:.2f}%")
    
    # Ensure MAPE is less than 10%
    if mape < 0.10:
        # Forecast the next 10 weeks
        future_forecast = forecast(model, 10)
        print("Forecast for the next 10 weeks:")
        print(future_forecast)
        
        # Plot the results
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data, label='Historical')
        plt.plot(test_data.index, test_forecast, label='Test Forecast', color='orange')
        plt.plot(pd.date_range(data.index[-1], periods=11, freq='W-MON')[1:], future_forecast, label='Future Forecast', color='green')
        plt.legend()
        plt.show()
    else:
        print("MAPE is greater than 10%. Model needs re-evaluation.")

if __name__ == "__main__":
    main()
```
