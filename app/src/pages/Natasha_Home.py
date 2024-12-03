import logging
logger = logging.getLogger(__name__)

import streamlit as st # type: ignore
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
    st.switch_page('pages/Natasha_Profile_Updates.py')

if st.button('Edit Your Reviews', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Natasha_Edit_Reviews.py')

if st.button('Explore Student Database', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Natasha_Explore_Students.py')

if st.button('View Reviews', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Natasha_View_Reviews.py')




