import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# Navigation menu for Jennifer's pages
page_options = [
    "Co-op Trends and Summary",
    "Skills Insights",
    "Review Management",
    "Company Satisfaction Analysis",
    "Student Participation Analysis"
]
selected_page = st.sidebar.selectbox("Select a Page", page_options)

# Page 1: Co-op Trends and Summary
if selected_page == "Co-op Trends and Summary":
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