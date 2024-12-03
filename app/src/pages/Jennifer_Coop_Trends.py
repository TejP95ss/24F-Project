import streamlit as st
import requests

st.title("Co-op Trends and Summary")
st.write("Analyze trends and summary data for co-op positions.")

# Input for position ID
position_id = st.text_input("Enter Position ID to get trends:", "1")

if st.button("Get Co-op Summary"):
    url = f"http://127.0.0.1:5000/trends/{position_id}"
    response = requests.get(url)
    if response.status_code == 200:
        summary_data = response.json()
        st.write("### Co-op Summary:")
        st.json(summary_data)
    else:
        st.error("Failed to fetch co-op summary data. Please check the Position ID.")

# Satisfaction by industry
if st.button("Get Company Satisfaction by Industry"):
    url = "http://127.0.0.1:5000/companies/satisfaction"
    response = requests.get(url)
    if response.status_code == 200:
        satisfaction_data = response.json()
        st.write("### Company Satisfaction by Industry:")
        st.json(satisfaction_data)
    else:
        st.error("Failed to fetch satisfaction data.")
