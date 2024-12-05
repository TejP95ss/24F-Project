import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
SideBarLinks()

# Title of the Page
st.title("Manage Data")


# Removal of a review
st.subheader("Remove Review")

# Input box for review id
id = st.text_input("Input Review ID to remove it")

# Button to remove review
if st.button('Delete Review',
             type = 'primary',
             use_container_width=True):
    response = requests.delete(f"http://web-api:4000/review/{id}/remove")
    if response.status_code == 200:
        st.success("Review Deleted Successfully")
    else:
        st.error(f"Failed to delete review. HTTP Status: {response.status_code}")
