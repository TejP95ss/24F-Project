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
if st.button("View Co-op Trends and Summary", type="primary", use_container_width=True):
    st.switch_page("Jennifer_Coop_Trends")

if st.button("Explore Skills Insights", type="primary", use_container_width=True):
    st.switch_page("Jennifer_Skills_Insights")

if st.button("Manage Tasks", type="primary", use_container_width=True):
    st.switch_page("Jennifer_Task_Management")
