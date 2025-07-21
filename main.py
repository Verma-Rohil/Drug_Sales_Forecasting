import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
from pmdarima.arima import ARIMA

# Page configuration
st.set_page_config(page_title="ARIMA Forecasting UI", layout="centered")

# Title
st.title("📈 ARIMA Time Series Forecasting App")

# Load saved ARIMA model
@st.cache_resource
def load_model():
    return joblib.load('arima_model.pkl')

model = load_model()

# Sidebar input
st.sidebar.header("📅 Forecast Settings")
n_periods = st.sidebar.slider("Select number of periods to forecast:", 1, 60, 12)

# Upload dataset
st.sidebar.header("📂 Upload Time Series CSV/TXT")
uploaded_file = st.sidebar.file_uploader("Upload your time series file (with date index)", type=['csv', 'txt'])

if uploaded_file:
    try:
        # Load uploaded data
        data = pd.read_csv(uploaded_file, index_col=0, parse_dates=True)

        # Ensure the index is datetime
        if not pd.api.types.is_datetime64_any_dtype(data.index):
            data.index = pd.to_datetime(data.index)

        # Forecast
        forecast, confint = model.predict(n_periods=n_periods, return_conf_int=True)
        last_index = data.index[-1]
        forecast_index = pd.date_range(start=last_index + pd.offsets.MonthBegin(1), periods=n_periods, freq='MS')

        forecast_series = pd.Series(forecast, index=forecast_index)
        lower_series = pd.Series(confint[:, 0], index=forecast_index)
        upper_series = pd.Series(confint[:, 1], index=forecast_index)

        # Plot with Plotly
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=data.index, y=data.iloc[:, 0], mode='lines', name='Historical', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=forecast_index, y=forecast_series, mode='lines', name='Forecast', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=forecast_index, y=upper_series, mode='lines', name='Upper Bound', line=dict(width=0), showlegend=False))
        fig.add_trace(go.Scatter(x=forecast_index, y=lower_series, mode='lines', name='Lower Bound', fill='tonexty',
                                 fillcolor='rgba(128,128,128,0.2)', line=dict(width=0), showlegend=False))

        fig.update_layout(
            title="Forecast with ARIMA Model",
            xaxis_title="Date",
            yaxis_title="Value",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Show forecasted values
        st.subheader("📊 Forecasted Values")
        st.dataframe(forecast_series.rename("Forecast"))

    except Exception as e:
        st.error(f"⚠️ Failed to load or forecast: {e}")

else:
    st.info("📄 Please upload a dataset with a datetime index column.")
