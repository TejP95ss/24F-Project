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

# Navigation buttons for Jennifer's functionalities
if st.button('Analyze Co-op Trends and Summary', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Jennifer_Trends_Summary.py')

if st.button('Explore Skills Insights', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Jennifer_Skills_Insights.py')

if st.button('Manage Reviews for Co-op Positions',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Jennifer_Review_Management.py')

if st.button('Analyze Company Satisfaction Ratings',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Jennifer_Company_Satisfaction.py')

if st.button('View Student Participation in Co-ops',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Jennifer_Student_Participation.py')