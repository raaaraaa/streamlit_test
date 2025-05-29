import streamlit as st 
import requests

# Set the app title 
st.title('Blupp Blupp anyeong raraaa !!') 

# Add a welcome message 
st.write('Welcome to my Streamlit app!') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

# Display the customized message 
st.write('Customized Message:', widgetuser_input)

# List of common currencies for dropdown
currency_options = [
    "USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SGD", "INR"
]

# Dropdown to select base currency
selected_currency = st.selectbox('Select base currency:', currency_options)

# API call with selected base currency
response = requests.get(f'https://api.vatcomply.com/rates?base={selected_currency}')

if response.status_code == 200:
    data = response.json()
    st.write(f'Exchange rates for {selected_currency}:')
    st.json(data)  # nicely formatted JSON output
else:
    st.error(f"API call failed with status code: {response.status_code}")



