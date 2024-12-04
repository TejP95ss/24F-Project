import streamlit as st
import requests
from modules.nav import SideBarLinks

# Title of the Page
st.title("Explore Our Student Database")
option = st.radio("What would you like to do?", ["Fetch Student List", "Find Specific Student"])

if option == "Fetch Student List":
    st.header("Fetch Student List")

    if st.button("Fetch Student List"):
        try:
            # Make the API request to the Flask route
            response = requests.get(f"http://web-api:4000/user")
            
            if response.status_code == 200:
                # Parse the JSON response
                student_details = response.json()
                
                if student_details:
                    # Display the details in a readable format
                    st.subheader("Student Details")
                    st.write(f"**Username:** {student_details[0]['username']}")
                    st.write(f"**Willing to Connect?:** {student_details[0]['openToConnect']}") # Figure out how to change TF to YN
                    st.write(f"**LinkedIn:** ${student_details[0]['linkedin']}")
                    st.write(f"**Major:** {student_details[0]['major']}")
                else:
                    st.error("No details found for the given ID.")
            else:
                st.error(f"Failed to fetch details. HTTP Status Code: {response}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Update Profile
elif option == "Change Connect Preferences":
    st.header("Change Your Connection Preferences")
    openToConnect = st. # Option to put yes or no

    if st.button("Update Profile"):
        if openToConnect:
            data = {
                "openToConnect": openToConnect
            }
            response = requests.put(f"http://web-api:4000/user/{id}", json=data)
            if response.status_code == 200:
                st.success("Preferences updated successfully!")
            else:
                st.error(f"Failed to update preferences. HTTP Status: {response.status_code}")
        else:
            st.warning("Please fill all fields!")





# Input for Co-op Position ID
position_id = st.text_input("Enter a Student ID:", "")

# Fetch Details Button
if st.button("Fetch Details"):
    if id:
        try:
            # Make the API request to the Flask route
            response = requests.get(f"http://web-api:4000/user/{id}")
            
            if response.status_code == 200:
                # Parse the JSON response
                student_details = response.json()
                
                if student_details:
                    # Display the details in a readable format
                    st.subheader("Student Details")
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
        st.warning("Please enter a Student Position ID.")