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

if st.button('Get Information About a Coop', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/JCoop_Info.py')

if st.button('Edit Skills', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/JEdit_Skills.py')

if st.button('Edit Reviews', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/JEdit_Reviews.py')