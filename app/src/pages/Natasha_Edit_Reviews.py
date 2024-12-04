import streamlit as st
import requests

st.title("Edit Your Review")

option = st.radio("What would you like to do?", ["Update Review", "Delete Review"])

# Update Existing Review
if option == "Update Review":
    st.header("Update Your Review")
    review_id = st.text_input("Review ID")

    if st.button("Update Review"):
        if review_id:
            data = {
                "review_id": review_id
            }
            response = requests.post(f"http://web-api:4000/review/{id}", json=data)
            if response.status_code == 200: # Check this
                st.success("Skill added to user's profile successfully!")
            else:
                st.error(f"Failed to update review. HTTP Status: {response.status_code}")
        else:
            st.warning("Please provide both Review ID!")

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
