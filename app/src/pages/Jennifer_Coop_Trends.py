import streamlit as st
import requests

# Title of the Page
st.title("Co-op Trends and Satisfaction")

# Input for Co-op Position ID
position_id = st.text_input("Enter the Co-op Position ID for Trends:", "")

# Fetch Co-op Trends Button
if st.button("Fetch Co-op Trends"):
    if position_id:
        try:
            # Make the API request to the Flask route
            response = requests.get(f"http://web-api:4000/trends/{position_id}")
            
            if response.status_code == 200:
                # Parse the JSON response
                trends = response.json()
                if trends:
                    st.subheader("Co-op Trends")
                    st.write(f"**Company Name:** {trends[0]['name']}")
                    st.write(f"**Position Title:** {trends[0]['title']}")
                    st.write(f"**Average Rating:** {trends[0]['avg_rating']}")
                else:
                    st.error("No trends data found for the given ID.")
            else:
                st.error(f"Failed to fetch trends. HTTP Status Code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a Co-op Position ID.")

# Fetch Company Satisfaction Button
if st.button("Fetch Company Satisfaction"):
    try:
        # Make the API request to the Flask route
        response = requests.get("http://web-api:4000/companies/satisfaction")
        
        if response.status_code == 200:
            # Parse the JSON response
            satisfaction = response.json()
            st.subheader("Company Satisfaction by Industry")
            for company in satisfaction:
                st.write(f"**Company Name:** {company['name']}")
                st.write(f"**Industry:** {company['industry']}")
                st.write(f"**Average Satisfaction:** {company['avg_satisfaction']}")
                st.write("---")
        else:
            st.error(f"Failed to fetch satisfaction data. HTTP Status Code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
