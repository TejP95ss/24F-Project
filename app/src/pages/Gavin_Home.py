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

if st.button('Access Student Data', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/GStudent_Data.py')
  
if st.button('Manage Databases',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/GDatabases.py')

if st.button('Hire a new data analyst',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/GAnalyst_Management.py')