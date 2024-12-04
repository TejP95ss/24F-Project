##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st # type: ignore
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('Rate My Co-Op')
st.write('\n\n')
st.write('### HI! Which user would you like to log in as?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 

if st.button("Act as John, a First Time Coop Seeker", 
           type = 'primary', 
           use_container_width=True):
   st.session_state['authenticated'] = True
   st.session_state['role'] = 'coop_seeker'
   st.session_state['first_name'] = 'John'
   logger.info("Logging in as First Time Coop Seeker John")
   st.switch_page('pages/John_Home.py')


if st.button("Act as Gavin, a System Administrator",
            type = 'primary',
            use_container_width=True):
   st.session_state['authenticated'] = True
   st.session_state['role'] = 'sys_admin'
   st.session_state['first_name'] = 'Gavin'
   logger.info("Logging in as System Administrator Gavin")
   st.switch_page('pages/Gavin_Home.py')

if st.button('Act as Jennifer, a Co-Op Program Analyst', 
           type = 'primary', 
           use_container_width=True):
   st.session_state['authenticated'] = True
   st.session_state['role'] = 'data_analyst'
   st.session_state['first_name'] = 'Jennifer'
   logger.info("Logging in as Data Analyst Jennifer")
   st.switch_page('pages/Jennifer_Home.py')

if st.button('Act as Natasha, a Past Co-Op Student', 
           type = 'primary', 
           use_container_width=True):
   st.session_state['authenticated'] = True
   st.session_state['role'] = 'student'
   st.session_state['first_name'] = 'Natasha'
   st.switch_page('pages/Natasha_Home.py')