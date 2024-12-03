import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
SideBarLinks()

# Title of the Page
st.title("Individual Student Co-op Count")

# pulls the data
results = requests.get(f"http://web-api:4000//student/coop_count")

# Display the details in a readable format
st.subheader("Student Co-op Counts")
st.dataframe(results)