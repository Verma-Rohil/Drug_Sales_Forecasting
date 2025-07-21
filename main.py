import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from pmdarima.arima import ARIMA

# Set Streamlit page config
st.set_page_config(page_title="ARIMA Forecasting UI", layout="centered")

# Title
st.title("📈 ARIMA Time Series Forecasting App")

# Load saved ARIMA model
@st.cache_resource
def load_model():
    return joblib.load('arima_model.pkl')

model = load_model()

# Forecast input
st.sidebar.header("📅 Forecast Settings")
n_periods = st.sidebar.slider("Select number of periods to forecast:", 1, 60, 12)

# Optional: Load training data if needed for plotting
@st.cache_data
def load_data():
    # This is just a dummy line — replace with your actual training data
    # e.g., pd.read_csv("drug_sales.csv", parse_dates=True, index_col="Month")
    return pd.read_csv("dataset.txt", index_col=0, parse_dates=True)

try:
    data = load_data()

    # Forecast
    forecast, confint = model.predict(n_periods=n_periods, return_conf_int=True)
    last_index = data.index[-1]
    forecast_index = pd.date_range(start=last_index + pd.offsets.MonthBegin(1), periods=n_periods, freq='MS')

    forecast_series = pd.Series(forecast, index=forecast_index)
    lower_series = pd.Series(confint[:, 0], index=forecast_index)
    upper_series = pd.Series(confint[:, 1], index=forecast_index)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data, label="Historical", color='blue')
    ax.plot(forecast_series, label="Forecast", color='darkgreen')
    ax.fill_between(forecast_index, lower_series, upper_series, color='gray', alpha=0.3)
    ax.set_title("ARIMA Forecast")
    ax.legend()

    # Show plot
    st.pyplot(fig)

    # Show forecasted values
    st.subheader("Forecasted Values")
    st.dataframe(forecast_series.rename("Forecast"))

except Exception as e:
    st.error(f"⚠️ Error loading data or forecasting: {e}")
