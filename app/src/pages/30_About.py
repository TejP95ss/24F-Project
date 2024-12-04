import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    This is a demo app for a Northeastern Co-op Review platform called Rate My Co-op

    The goal of this project is to provide a review service for students searching for co-ops and for those would like to share their past experiences

    
    We have provided 4 personas for use:

    Gavin, a system administrator, who can perform various management tasks to keep the platform running smoothly 

    Jennifer, a data analyst who can modify and view site statistics to monitor student and co-op trends 

    John, a first time co-op seeker who is using the platform to help him determine which companies he wants to apply to 

    Natasha, a former co-op student who can use the platform to submit and modify reviews on her experience and help future users 

    
    Feel free to act as one of the 4 personas provided to test out any of the features!
    """
        )
