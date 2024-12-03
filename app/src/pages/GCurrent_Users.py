import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
SideBarLinks()

# Title of the Page
st.title("List of Current Student Users")

# pulls the data
results = requests.get(f"http://web-api:4000/current_users").json()

# Display the details in a readable format
st.subheader("Number of Current Student Users")
st.dataframe(results)