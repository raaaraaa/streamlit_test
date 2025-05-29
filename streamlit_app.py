import streamlit as st
import requests
import pandas as pd

st.title("🌍 Currency and Weather Dashboard")

# --- Custom Message Input ---
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', widgetuser_input)

# --- Currency Exchange Section ---
currency_options = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SGD", "INR", "MYR"]
selected_currency = st.selectbox('Select base currency:', currency_options)

if st.button("Get Exchange Rates"):
    response = requests.get(f'https://api.vatcomply.com/rates?base={selected_currency}')
    if response.status_code == 200:
        data = response.json()
        st.write(f'Exchange rates for {selected_currency}:')
        st.json(data)
    else:
        st.error(f"API call failed with status code: {response.status_code}")

# --- Weather Section ---
st.header("🌤 Weather Forecast by Country")

# Country -> City + Coordinates
country_coords = {
    "Philippines": {"city": "Manila", "lat": 14.6, "lon": 120.98},
    "United States": {"city": "New York", "lat": 40.71, "lon": -74.01},
    "Japan": {"city": "Tokyo", "lat": 35.68, "lon": 139.69},
    "United Kingdom": {"city": "London", "lat": 51.51, "lon": -0.13},
    "Australia": {"city": "Sydney", "lat": -33.87, "lon": 151.21},
    "India": {"city": "New Delhi", "lat": 28.61, "lon": 77.21},
    "Canada": {"city": "Toronto", "lat": 43.65, "lon": -79.38},
    "China": {"city": "Beijing", "lat": 39.91, "lon": 116.40},
    "Germany": {"city": "Berlin", "lat": 52.52, "lon": 13.40},
    "Brazil": {"city": "São Paulo", "lat": -23.55, "lon": -46.63},
    "Malaysia": {"city": "Kuala Lumpur", "lat": 3.14, "lon": 101.69},  # ✅ Added Malaysia
}

# Country Dropdown
selected_country = st.selectbox("Select a country:", list(country_coords.keys()))
selected_location = country_coords[selected_country]

# Show selected city and coordinates
st.write(f"City: {selected_location['city']}")
st.write(f"Coordinates: {selected_location['lat']}, {selected_location['lon']}")

# Weather API Call
weather_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={selected_location['lat']}&longitude={selected_location['lon']}"
    f"&hourly=temperature_2m,wind_speed_10m,relative_humidity_2m"
    f"&current_weather=true"
)

weather_response = requests.get(weather_url)

if weather_response.status_code == 200:
    weather_data = weather_response.json()

    # Current weather
    current = weather_data.get("current_weather", {})
    st.subheader("Current Weather")
    st.write(f"Temperature: {current.get('temperature')}°C")
    st.write(f"Windspeed: {current.get('windspeed')} km/h")

    # Hourly data
    hourly = weather_data["hourly"]
    df_weather = pd.DataFrame({
        "Time": pd.to_datetime(hourly["time"]),
        "Temperature (°C)": hourly["temperature_2m"],
        "Wind Speed (km/h)": hourly["wind_speed_10m"],
        "Humidity (%)": hourly["relative_humidity_2m"]
    })

    st.subheader("Hourly Weather Trends")
    st.line_chart(df_weather.set_index("Time"))
else:
    st.error("Failed to fetch weather data.")
