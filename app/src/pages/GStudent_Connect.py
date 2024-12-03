import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
SideBarLinks()

# Title of the Page
st.title("List of Students Ready to Connect on Linkedin")

# pulls the data
results = requests.get(f"http://web-api:4000/id")

# Display the details in a readable format
st.subheader("List of IDs")
st.dataframe(results)