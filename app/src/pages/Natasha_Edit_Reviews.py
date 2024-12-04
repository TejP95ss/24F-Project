import streamlit as st
import requests

st.title("Edit Your Review")

option = st.radio("What would you like to do?", ["Update Review", "Delete Review"])

# Update Existing Review --> should I delete this? 
# it's a user story, but already there in John's portion. 
# and I already have a put method
if option == "Update Review":
    st.header("Update Your Review")
    review_id = st.text_input("Review ID")
    rating = st.slider("New Rating (1-5)", 1, 5, 3)
    review_text = st.text_area("Update your review")

    if st.button("Update Review"):
        if review_id and review_text:
            data = {
                "rating": rating,
                "review_text": review_text
            }
            response = requests.put(f"http://web-api:4000/reviews/{review_id}", json=data)
            if response.status_code == 200:
                st.success("Review updated successfully!")
            else:
                st.error(f"Failed to update review. HTTP Status: {response.status_code}")
        else:
            st.warning("Please fill all fields!")

# Remove Skill from User Profile
elif option == "Delete Your Review":
    st.header("Delete Review")
    review_id = st.text_input("Review ID", key="remove_review_id")

    if st.button("Remove Skill"):
        if review_id:
            data = {
                "review_id": review_id
            }
            response = requests.delete(f"http://web-api:4000/user/{review_id}", json=data)
            if response.status_code == 200:
                st.success("Review removed from user's profile successfully!")
            else:
                st.error(f"Failed to remove review. HTTP Status: {response.status_code}")
        else:
            st.warning("Please provide both Review ID!")
