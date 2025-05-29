import streamlit as st
import requests
import pandas as pd

# Title and welcome
st.title('Blupp Blupp anyeong raraaa !!')
st.write('Welcome to my Streamlit app!')

# Text input
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', widgetuser_input)

# Dropdown to select base currency
currency_options = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SGD", "INR"]
selected_currency = st.selectbox('Select base currency:', currency_options)

# Currency API call
if st.button("Get Exchange Rates"):
    response = requests.get(f'https://api.vatcomply.com/rates?base={selected_currency}')
    
    if response.status_code == 200:
        data = response.json()
        st.write(f'Exchange rates for {selected_currency}:')
        st.json(data)
    else:
        st.error(f"API call failed with status code: {response.status_code}")

# --- Simulated Weather Data ---
weather_data = {
    "current": {
        "time": "2022-01-01T15:00",
        "temperature_2m": 2.4,
        "wind_speed_10m": 11.9,
    },
    "hourly": {
        "time": [
            "2022-07-01T00:00", "2022-07-01T01:00", "2022-07-01T02:00",
            "2022-07-01T03:00", "2022-07-01T04:00", "2022-07-01T05:00"
        ],
        "wind_speed_10m": [3.16, 3.02, 3.3, 3.14, 3.2, 2.95],
        "temperature_2m": [13.7, 13.3, 12.8, 12.3, 11.8, 11.2],
        "relative_humidity_2m": [82, 83, 86, 85, 88, 88],
    }
}

st.subheader("🌤 Current Weather")
st.write(f"Time: {weather_data['current']['time']}")
st.write(f"Temperature: {weather_data['current']['temperature_2m']}°C")
st.write(f"Wind Speed: {weather_data['current']['wind_speed_10m']} km/h")

# Convert hourly data to DataFrame
hourly = weather_data["hourly"]
df_weather = pd.DataFrame({
    "Time": pd.to_datetime(hourly["time"]),
    "Temperature (°C)": hourly["temperature_2m"],
    "Wind Speed (km/h)": hourly["wind_speed_10m"],
    "Humidity (%)": hourly["relative_humidity_2m"]
})

# Display line chart
st.subheader("📊 Hourly Weather Trends")
st.line_chart(df_weather.set_index("Time"))
