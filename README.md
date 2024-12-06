# **Rate My Coop**
Team Member Names: Aarushi Thejaswi, Arushee Tirunagari, Niharika Banerjee, Alexander Kylander-Kreiner, Tej Patel

Project Demo Video Link: https://www.dropbox.com/scl/fi/prls1bto8tzhjnb5x40sg/RateMyCoop_DB_Project.mp4?rlkey=e20ooe3txsqxcxr7ue1as9te3&st=29e1835d&dl=0 

--

Instructions for starting the docker container:
docker compose down
docker compose up -d

--

**Rate My Coop** is a web application inspired by **Rate My Professor**, designed to help co-op students share experiences, find relevant co-op opportunities, and connect with peers. This platform provides a space for students to discover detailed information about co-op positions, rate their experiences, and build meaningful professional connections.

---

## **Features**

### **For First-Time Co-op Seekers**
1. **Get Detailed Information about a Co-op Position**:
   - Access comprehensive details about specific co-op positions, including job descriptions, workload, hourly wages, and company information.

2. **Add Skills to Your Profile**:
   - Add technical or soft skills to your profile to showcase your abilities and improve discoverability for relevant co-op opportunities.

3. **Delete Skills from Your Profile**:
   - Remove outdated or irrelevant skills from your profile to keep it updated.

4. **Update LinkedIn Profile URL**:
   - Customize and update your LinkedIn URL as needed, ensuring your professional profile stays accessible.

5. **Get a List of Students Open to Connect**:
   - Explore a list of students who are open to networking and connecting, making it easier to seek advice or build connections.

---

### **For Experienced Co-op Students and Reviewers**
1. **View Reviews for a Specific Co-op Position**:
   - Access reviews from previous co-op students about specific positions, helping you make informed decisions about your next opportunity.

2. **Get Details about a Specific Co-op Student**:
   - Retrieve detailed information about a specific co-op student, including their profile, reviews, and availability to connect.

3. **Get a List of Co-op Students**:
   - View a complete list of co-op students on the platform to identify potential peers or mentors.

4. **Add a User Profile**:
   - Create a new user profile with contact information, preferences, and professional details.

5. **Update Open-to-Connect Status**:
   - Manage your networking availability by toggling your "open to connect" status.

6. **Delete a Review**:
   - Remove reviews that are outdated or no longer relevant.

7. **Update an Existing Review**:
   - Edit previously submitted reviews to ensure they are accurate and up-to-date.

---

### ** For System Administrators**
1. **Access Student Data**
   - Retrieve the IDs for every student using the platform
2. **Access Connecting Students**
   - Retrieve information for students looking to connect on Linkedin
3. **Co-op Details**
   - Get the total number of co-ops active students have participated in
4. **Manage Backup Data**
   - Manually reload a previous version of the application
5. **Process New Hires**
   - Add newly hired analysts and their information into the system
6. **Manage Submitted Reviews**
   - Remove any submitted review to ensure the quality of reviews on the platform

### ** For Co-OP Advisorss**

1. **View Aggregated Trends by Industry**
  - Gain insights into industry-specific trends, including skill alignments, career alignments, and satisfaction alignments, to better understand the evolving needs of co-op placements.

2. **Add New Trends**
  - Input new trends into the system, ensuring the database reflects the latest information about industry expectations and skill demands.

3. **Update Existing Trends**
  - Modify existing trend data to keep it accurate and relevant, helping co-op seekers align their skills with industry needs.

4. **Delete Trends**
 - Remove outdated or irrelevant trends to maintain a streamlined and up-to-date trends database.
 
5. **Fetch Reports Assigned to Data Analysts**
  - Access reports created by data analysts, providing detailed comparisons of industries, co-op performance metrics, and other critical  data for advising co-op seekers.







### **Prerequisites**
- Python (3.8 or higher)
- Docker and Docker Compose
- Streamlit (for the frontend)
- MySQL (managed via Docker)

