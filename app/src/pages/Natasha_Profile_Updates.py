import streamlit as st
import requests

st.title("Create and Update Profile")
option = st.radio("What would you like to do?", ["Create Profile", "Change Connect Preferences"])

# Create Profile
if option == "Create Profile":
    st.header("Create Profile")
    username = st.text_input("Username: ")
    profileType = st. # option to put either Seeker or Reviewer
    openToConnect = st. # Option to put yes or no

    if st.button("Create Profile"):
        if position_id and student_id and review_text:
            data = {
                "username": username,
                "profileType": profileType,
                "openToConnect": openToConnect
            }
            response = requests.post(f"http://web-api:4000/students/{id}", json=data)
            if response.status_code == 201:
                st.success("Profile created successfully!")
            else:
                st.error(f"Failed to create profile. HTTP Status: {response.status_code}")
        else:
            st.warning("Please fill all fields!")

# Update Profile
elif option == "Change Connect Preferences":
    st.header("Change Your Connection Preferences")
    openToConnect = st. # Option to put yes or no

    if st.button("Update Profile"):
        if openToConnect:
            data = {
                "openToConnect": openToConnect
            }
            response = requests.put(f"http://web-api:4000/user/{id}", json=data)
            if response.status_code == 200:
                st.success("Preferences updated successfully!")
            else:
                st.error(f"Failed to update preferences. HTTP Status: {response.status_code}")
        else:
            st.warning("Please fill all fields!")