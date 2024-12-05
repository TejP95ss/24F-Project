import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Get Information About a Coop', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/John_Coop_Info.py')

if st.button('Add and Remove Skills', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/John_Edit_Skills.py')

if st.button('Edit Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/John_Update_Linkedin.py')

if st.button('See All Students Open To Connect', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/John_Open_To_Connect.py')