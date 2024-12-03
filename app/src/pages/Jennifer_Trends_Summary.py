import streamlit as st
import requests

st.title("Co-op Trends and Summary")
st.write("Analyze trends and summary data for co-op positions.")

# Input for position ID
position_id = st.text_input("Enter a Position ID to analyze trends:", "1")

if st.button("Get Co-op Summary"):
    url = f"http://127.0.0.1:5000/trends/{position_id}"
    response = requests.get(url)
    if response.status_code == 200:
        summary_data = response.json()
        st.write("### Summary Data:")
        st.write(summary_data)
    else:
        st.error("Failed to fetch co-op summary data.")

# Fetch average ratings and review counts for positions
st.write("### Co-op Ratings by Company")
if st.button("Get Co-op Ratings"):
    url = "http://127.0.0.1:5000/positions/ratings"
    response = requests.get(url)
    if response.status_code == 200:
        ratings_data = response.json()
        st.write(ratings_data)
    else:
        st.error("Failed to fetch co-op ratings.")
