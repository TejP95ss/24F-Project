import streamlit as st
import requests

st.title("Update LinkedIn Profile URL")

user_id = st.text_input("Enter User ID", placeholder="E.g., 1")

linkedin_url = st.text_input(
    "Enter New LinkedIn Profile URL",
    placeholder="E.g., https://www.linkedin.com/in/your-profile"
)

if st.button("Update LinkedIn URL"):
    if not user_id or not linkedin_url:
        st.warning("Both User ID and LinkedIn URL are required!")
    else:
        url = f"http://web-api:4000/user/{user_id}/linkedin"
        payload = {"linkedin_url": linkedin_url}

        try:
            response = requests.put(url, json=payload)
            if response.status_code == 200:
                st.success("LinkedIn URL updated successfully!")
            elif response.status_code == 404:
                st.error("User ID not found!")
            elif response.status_code == 400:
                st.error("Invalid input! Please check the LinkedIn URL.")
            else:
                st.error(f"Failed to update. HTTP Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {str(e)}")
