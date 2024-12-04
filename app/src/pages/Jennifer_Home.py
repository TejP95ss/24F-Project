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

# Action buttons for Jennifer's features
if st.button('View Trends Overview', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Jennifer_Trends_Overview.py')

if st.button('Manage Trends', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Jennifer_Manage_Trends.py')

if st.button('View Reports', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Jennifer_View_Reports.py')
