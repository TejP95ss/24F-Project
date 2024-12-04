import streamlit as st
import requests

# Title of the Page
st.title("View Reviews")

# Input for Co-op Position ID
position_id = st.text_input("Enter the Co-op Position ID:", "")

# Fetch Details Button
if st.button("Fetch Reviews"):
    if position_id:
        try:
            # Make the API request to the Flask route
            response = requests.get(f"http://web-api:4000/positions/{position_id}/review")
            
            if response.status_code == 200:
                # Parse the JSON response
                review_details = response.json()
                
                if review_details:
                    # Display the details in a readable format
                    st.subheader("Review")
                    st.write(f"**Review ID:** {review_details[0]['id']}")
                    st.write(f"**Rating:** {review_details[0]['rating']}")
                    st.write(f"**Review:** {review_details[0]['review_text']}")
                else:
                    st.error("No details found for the given ID.")
            else:
                st.error(f"Failed to fetch details. HTTP Status Code: {response}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a Co-op Position ID.")