import streamlit as st
import requests

# Set the app title
st.title('Blupp Blupp anyeong raraaa !!')

# Add a welcome message
st.write('Welcome to my Streamlit app!')

# Text input for a custom message
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', widgetuser_input)

# Dropdown to select base currency
currency_options = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SGD", "INR"]
selected_currency = st.selectbox('Select base currency:', currency_options)

# Button to trigger API call
if st.button("Get Exchange Rates"):
    response = requests.get(f'https://api.vatcomply.com/rates?base={selected_currency}')
    
    if response.status_code == 200:
        data = response.json()
        st.write(f'Exchange rates for {selected_currency}:')
        st.json(data)
    else:
        st.error(f"API call failed with status code: {response.status_code}")
