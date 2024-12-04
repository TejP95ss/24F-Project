import streamlit as st
import requests

# Title
st.title("Co-op Trends and Company Insights")

# Section: Co-op Trends
st.subheader("Co-op Position Trends")
position_id = st.text_input("Enter Co-op Position ID:", "")

if st.button("Fetch Co-op Trends"):
    if position_id:
        try:
            response = requests.get(f"http://web-api:4000/trends/{position_id}")
            if response.status_code == 200:
                trends = response.json()
                if trends:
                    st.write(f"**Company Name:** {trends[0]['name']}")
                    st.write(f"**Position Title:** {trends[0]['title']}")
                    st.write(f"**Average Rating:** {trends[0]['avg_rating']}")
                else:
                    st.error("No trends data found for the provided Position ID.")
            else:
                st.error(f"Failed to fetch trends. Status Code: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a Position ID.")

# Section: Company Satisfaction
st.subheader("Company Satisfaction by Industry")
if st.button("Fetch Company Satisfaction"):
    try:
        response = requests.get("http://web-api:4000/companies/satisfaction")
        if response.status_code == 200:
            satisfaction = response.json()
            for company in satisfaction:
                st.write(f"**Company Name:** {company['name']}")
                st.write(f"**Industry:** {company['industry']}")
                st.write(f"**Average Satisfaction:** {company['avg_satisfaction']}")
                st.write("---")
        else:
            st.error(f"Failed to fetch company satisfaction. Status Code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {e}")
