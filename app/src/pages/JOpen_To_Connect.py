import streamlit as st
import requests

st.title("Students Open to Connect")

if st.button("Fetch Open-to-Connect Students"):
    try:
        url = "http://web-api:4000/students/open_to_connect"
        response = requests.get(url)
        if response.status_code == 200:
            students = response.json()
            if not students:
                st.info("No students are currently open to connect.")
            else:
                st.success("Students Open to Connect:")
                for student in students:
                    st.write(f"- **Name**: {student['full_name']}")
                    st.write(f"  **LinkedIn**: {student['linkedin']}")
                    st.write("---")
        elif response.status_code == 404:
            st.warning("No students found who are open to connect.")
        else:
            st.error(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {str(e)}")
