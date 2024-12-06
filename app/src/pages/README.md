# `pages` Folder

This folder contains all the pages that will be part of the application. 

--
## **Gavin**

These pages are designed to help Gavin, a system administrator, manage user data, monitor activity, and add staff.

### **1. Gavin_Analyst_Management
Process and manage data for system analysts.

#### **Features**:
- Allows the addition of a new hire, with user input for name, email, and position.
- Allows the modification of employee emails given an email and ID

---

### **2. Gavin_Databases
Manage reviews submitted into the system.

#### **Features**:
- Allows the removal of reviews in the system.
- Input a review ID to remove it.

---

### **3. Gavin_Student_Data
View information about student users in the system.

#### **Features**:
- Displays data about 
    - Active student user IDs
    - Students ready to connect
    - Co-op counts for students on the platform

---

## **John**

These pages are designed to help John, a first-time co-op seeker, gather information, manage his profile, and connect with others.

---

### **1. John_Coop_Info**
View detailed information about a specific co-op position.

#### **Features**:
- Displays pay, workload, description, and company info.
- Enter the co-op ID and click "Fetch Details" to view.

---

### **2. John_Edit_Skills**
Add or remove skills from John's profile.

#### **Features**:
- Add new skills to showcase abilities.
- Remove outdated or irrelevant skills.

---

### **3. John_Update_Linkedin**
Update the LinkedIn URL in John's profile.

#### **Features**:
- Enter a new URL and click "Update" to save changes.

---

### **4. John_Open_To_Connect**
Find students who are open to networking.

#### **Features**:
- View names and LinkedIn links of open-to-connect students.


## **Jennifer**

These pages are designed to help Jennifer, a co-op program analyst, gather co-op trend information, manage trends, and view reports made by other co-op advisors.

---
### **1. Jennifer_Trends_Overview**
View aggregated trends for deeper insights into program alignment.

#### **Features**:
- Fetch aggregated trends by industry.
- Display details, including:
  - Skill alignments.
  - Career alignments.
  - Satisfaction alignments.

---

### **2. Jennifer_Manage_Trends**
Manage co-op program trends by adding, updating, or deleting entries.

#### **Features**:
- Add a New Trend:
  -  Input industry, skill alignments, career alignments, and satisfaction alignments.
  - Click "Add Trend" to save. 
- Update an Existing Trend:
  - Enter the trend ID, updated skill alignments, and career alignments.
  - Click "Update Trend" to apply changes.
- Delete a Trend:
  - Input the trend ID and click "Delete Trend" to remove it.

---

### **3. Jennifer_View_Reports**
Access reports created by co-op advisors for program evaluation.

#### **Features**:
- Fetch reports by co-op advisors.
- View details for each report:
  - Report name.
  - Industry comparison.
  - Created by.
  - Timestamp.

---

## **Natasha**

These pages are designed to help Natasha, a past co-op student, create and update her profile, edit her reviews, explore the student database, and view co-op reviews.

---
### **1. Natasha_Profile_Updates**
Create user profile and update connect preferences.

#### **Features**:
- Create Profile with inputs:
    - username
    - profile type
    - connection preference.
- Update "open to connect" as true or false.

---

### **2. Natasha_Edit_Reviews**
Update review ratings or text, or delete a review entirely.

#### **Features**:
- Update Review:
  - Input review id, new rating, and updated review text.
  - Click "Update Review" to save. 
- Delete Review:
  - Input review ID and click "Delete Review" to remove it.

---

### **3. Natasha_Explore_Students**
Allows the user to look through the student database or search for a specific student.

#### **Features**:
- Fetch list of all students in the database.
- Fetch information about a certain student based on student ID.

---

### **4. Natasha_View_Reviews**
View all reviews for a specific co-op.

#### **Features**:
- Enter co-op position ID. Returns a list of all reviews for that co-op, including:
    - Review ID
    - Rating
    - Review text

---
