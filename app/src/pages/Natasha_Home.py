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

# Navigation buttons for Natasha's functionalities
if st.button('Create and Update Profile', 
             type='primary',
             use_container_width=True):
    st.switch_page('_____')

if st.button('Edit Your Reviews', 
             type='primary',
             use_container_width=True):
    st.switch_page('__')

if st.button('Explore Student Database', 
             type='primary',
             use_container_width=True):
    st.switch_page('___')

if st.button('View Reviews', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Jennifer_Skills_Insights.py')




