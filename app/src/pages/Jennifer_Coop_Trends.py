import streamlit as st
import requests

st.title("Co-op Trends and Summary")
st.write("Analyze trends and summary data for co-op positions.")

# Input for position ID
position_id = st.text_input("Enter Position ID:", "1")

if st.button("Get Co-op Summary"):
    url = f"http://127.0.0.1:5000/trends/{position_id}"
    response = requests.get(url)
    if response.status_code == 200:
        summary_data = response.json()
        st.write("### Co-op Summary:")
        st.write(summary_data)
    else:
        st.error("Failed to fetch co-op summary data.")
