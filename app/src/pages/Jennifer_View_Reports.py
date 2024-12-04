import streamlit as st
import requests

st.title("View Reports")

if st.button("Fetch Reports Created by Co-Op Advisors"):
    try:
        url = "http://web-api:4000/reports"
        response = requests.get(url)
        if response.status_code == 200:
            reports = response.json()
            if not reports:
                st.info("No reports are available.")
            else:
                st.success("Reports:")
                for report in reports:
                    st.write(f"**Report Name**: {report['report_name']}")
                    st.write(f"  **Industry Comparison**: {report['industry_compare']}")
                    st.write(f"  **Created By**: {report['created_by']}")
                    st.write(f"  **Timestamp**: {report['timestamp']}")
                    st.write("---")
        elif response.status_code == 404:
            st.warning("No reports found.")
        else:
            st.error(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {str(e)}")
