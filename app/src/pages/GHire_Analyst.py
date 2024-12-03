import streamlit as st
import requests

st.title('Hire a new Data Analyst')
name = st.text_input('New Hire Name: ')
email = st.text_input('New Hire Email: ')
role = st.text_input('New Hire Role: ')

if st.button('Submit Hire'):
    if name and email and role:
        data = {
            "email": email,
            "name": name,
            "role": role
        }
        response = requests.post(f'http://web-api:4000/data_analyst', json=data)
        if response.status_code == 201:
            st.success('New hire successfully added to system!')
        else:
                st.error(f"Failed to add new hire. HTTP Status: {response.status_code}")
    else:
         st.warning("Please fill all fields!")
