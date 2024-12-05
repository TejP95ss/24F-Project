import streamlit as st
import requests

# Title of the Page
st.title("Co-op Position Details")

# Input for Co-op Position ID
position_id = st.text_input("Enter the Co-op Position ID:", "")

# Fetch Details Button
if st.button("Fetch Details"):
    if position_id:
        try:
            # Make the API request to the Flask route
            response = requests.get(f"http://web-api:4000/positions/{position_id}")
            
            if response.status_code == 200:
                # Parse the JSON response
                position_details = response.json()
                
                if position_details:
                    # Display the details in a readable format
                    st.subheader("Position Details")
                    st.write(f"**Title:** {position_details[0]['title']}")
                    st.write(f"**Company ID:** {position_details[0]['company_id']}")
                    st.write(f"**Hourly Wage:** ${position_details[0]['hourly_wage']}/hr")
                    st.write(f"**Workload:** {position_details[0]['workload']} hours/week")
                    st.write(f"**Description:** {position_details[0]['description']}")
                else:
                    st.error("No details found for the given ID.")
            else:
                st.error(f"Failed to fetch details. HTTP Status Code: {response}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a Co-op Position ID.")
