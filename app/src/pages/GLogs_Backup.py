import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
SideBarLinks()

# Title of the Page
st.title("Restore Backup Log")

# Input box for version 
id = st.text_input("Input Application ID to restore that application:")

# Button to restore backup
if st.button('Restore Backup',
             type = 'primary',
             use_container_width=True):
    response = requests.put(f"http://web-api:4000//logs_backup/{id}")
    if response.status_code == 200:
        st.success("Backup Restored Successfully!")
    else:
        st.error(f"Failed to restore backup. HTTP Status: {response.status_code}")