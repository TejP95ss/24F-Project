import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
SideBarLinks()

# Title of the Page
st.title("Student User Data")


# Info for Current Student Users

# pulls the data
current_users = requests.get(f"http://web-api:4000/current_users").json()

# Display the details in a readable format
st.subheader("Number of current student users")
st.dataframe(current_users)


# Info for a count of the total number of Co-ops

# pulls the data
coop_count = requests.get(f"http://web-api:4000//student/coop_count").json()

# Display the details in a readable format
st.subheader("Student Co-op counts")
st.dataframe(coop_count)


# Info for students ready to connect on Linkedin

# pulls the data
linkedin_connect = requests.get(f"http://web-api:4000/id").json()

# Display the details in a readable format
st.subheader("IDs for students ready to connect")
st.dataframe(linkedin_connect)