import streamlit as st
import requests

st.title("Manage Trends")

# Add a new trend
st.subheader("Add a New Trend")
industry = st.text_input("Industry")
skills = st.text_area("Skill Alignments")
career = st.text_input("Career Alignments")
satisfaction = st.text_input("Satisfaction Alignments")

if st.button("Add Trend"):
    try:
        url = "http://web-api:4000/trends"
        response = requests.post(url, json={
            "industry": industry,
            "skill_alignments": skills,
            "career_alignments": career,
            "satisfaction_alignments": satisfaction,
        })
        if response.status_code == 201:
            st.success("Trend added successfully.")
        else:
            st.error(f"Failed to add trend. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {str(e)}")

# Update an existing trend
st.subheader("Update an Existing Trend")
trend_id = st.number_input("Trend ID to Update", step=1)
new_skills = st.text_area("Updated Skill Alignments")
new_career = st.text_input("Updated Career Alignments")

if st.button("Update Trend"):
    try:
        url = f"http://web-api:4000/trends/{trend_id}"
        response = requests.put(url, json={
            "skill_alignments": new_skills,
            "career_alignments": new_career,
        })
        if response.status_code == 200:
            st.success("Trend updated successfully.")
        else:
            st.error(f"Failed to update trend. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {str(e)}")

# Delete a trend
st.subheader("Delete a Trend")
delete_id = st.number_input("Trend ID to Delete", step=1)

if st.button("Delete Trend"):
    try:
        url = f"http://web-api:4000/trends/{delete_id}"
        response = requests.delete(url)
        if response.status_code == 200:
            st.success("Trend deleted successfully.")
        else:
            st.error(f"Failed to delete trend. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {str(e)}")
