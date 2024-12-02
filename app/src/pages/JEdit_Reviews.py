import streamlit as st
import requests

# Title of the Page
st.title("Add or Update Co-op Reviews")

# Select Functionality
option = st.radio("What would you like to do?", ["Add Review", "Update Review"])

# Add a Review
if option == "Add Review":
    st.header("Add a Review for a Position")
    position_id = st.text_input("Coop Position ID: ")
    student_id = st.text_input("Your Student ID: ")
    rating = st.slider("Rating (1-5)", 1, 5, 3)
    review_text = st.text_area("Write your review: ")

    if st.button("Submit Review"):
        if position_id and student_id and review_text:
            # Prepare data
            data = {
                "rating": rating,
                "review_text": review_text,
                "student_id": student_id
            }
            # Make POST request
            response = requests.post(f"http://web-api:4000/reviews/{position_id}", json=data)
            if response.status_code == 201:
                st.success("Review added successfully!")
            else:
                st.error(f"Failed to add review. HTTP Status: {response.status_code}")
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
            # Prepare data
            data = {
                "rating": rating,
                "review_text": review_text
            }
            # Make PUT request
            response = requests.put(f"http://web-api:4000/reviews/{review_id}", json=data)
            if response.status_code == 200:
                st.success("Review updated successfully!")
            else:
                st.error(f"Failed to update review. HTTP Status: {response.status_code}")
        else:
            st.warning("Please fill all fields!")