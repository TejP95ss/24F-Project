import streamlit as st
import requests

st.title("Trends Overview")

# Fetch and display aggregated trends
if st.button("Fetch Aggregated Trends"):
    try:
        url = "http://web-api:4000/trends"
        response = requests.get(url)
        if response.status_code == 200:
            trends = response.json()
            if not trends:
                st.info("No trends data available.")
            else:
                st.success("Aggregated Trends by Industry:")
                for trend in trends:
                    st.write(f"**Industry**: {trend['industry']}")
                    st.write(f"  **Skill Alignments**: {trend['skill_alignments']}")
                    st.write(f"  **Career Alignments**: {trend['career_alignments']}")
                    st.write(f"  **Satisfaction Alignments**: {trend['satisfaction_alignments']}")
                    st.write("---")
        elif response.status_code == 404:
            st.warning("No trends found in the database.")
        else:
            st.error(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {str(e)}")