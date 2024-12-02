import streamlit as st
import requests

st.title("Manage User Skills")

option = st.radio("What would you like to do?", ["Add Skill", "Remove Skill"])

# Add Skill to User Profile
if option == "Add Skill":
    st.header("Add Skill to User Profile")
    user_id = st.text_input("User ID")
    skill_id = st.text_input("Skill ID")

    if st.button("Add Skill"):
        if user_id and skill_id:
            data = {
                "skill_id": skill_id
            }
            response = requests.post(f"http://web-api:4000/user/{user_id}/skills", json=data)
            if response.status_code == 201:
                st.success("Skill added to user's profile successfully!")
            else:
                st.error(f"Failed to add skill. HTTP Status: {response.status_code}")
        else:
            st.warning("Please provide both User ID and Skill ID!")

# Remove Skill from User Profile
elif option == "Remove Skill":
    st.header("Remove Skill from User Profile")
    user_id = st.text_input("User ID", key="remove_user_id")
    skill_id = st.text_input("Skill ID", key="remove_skill_id")

    if st.button("Remove Skill"):
        if user_id and skill_id:
            data = {
                "skill_id": skill_id
            }
            response = requests.delete(f"http://web-api:4000/user/{user_id}/skills", json=data)
            if response.status_code == 200:
                st.success("Skill removed from user's profile successfully!")
            else:
                st.error(f"Failed to remove skill. HTTP Status: {response.status_code}")
        else:
            st.warning("Please provide both User ID and Skill ID!")
