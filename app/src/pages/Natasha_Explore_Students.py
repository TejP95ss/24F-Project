import streamlit as st
import requests
from modules.nav import SideBarLinks

# Title of the Page
st.title("Explore Student Database")
option = st.radio("What would you like to do?", ["Fetch Student List", "Find Specific Student"])

# Fetch List of All Students
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
                    st.write(f"**ID:** {student_details[0]['id']}")
                    st.write(f"**Willing to Connect?:** {student_details[0]['openToConnect']}") # Figure out how to change TF to YN
                    st.write(f"**LinkedIn:** ${student_details[0]['linkedin']}")
                    st.write(f"**Major:** {student_details[0]['major']}")
                else:
                    st.error("An Error Occurred.")
            else:
                st.error(f"Failed to fetch details. HTTP Status Code: {response}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Fetch List of a specific student using their ID
elif option == "Find Specific Student":
    st.header("Find Specific Student")
    id = st.text_input("Enter a Student ID:", "")

    if st.button("Find Specific Student"):
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
                        st.write(f"**Username:** {student_details[0]['username']}")
                        st.write(f"**ID:** {student_details[0]['id']}")
                        st.write(f"**Willing to Connect?:** {student_details[0]['openToConnect']}") # Figure out how to change TF to YN
                        st.write(f"**LinkedIn:** ${student_details[0]['linkedin']}")
                        st.write(f"**Major:** {student_details[0]['major']}")
                    else:
                        st.error("No details found for the given ID.")
                else:
                    st.error(f"Failed to fetch details. HTTP Status Code: {response}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
            st.warning("Please enter a Student ID.")

