import streamlit as st
import requests

st.title("Create and Update Profile")
option = st.radio("What would you like to do?", ["Create Profile", "Update Profile"])

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

# Update a Review
elif option == "Update Review":
    st.header("Update an Existing Review")
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