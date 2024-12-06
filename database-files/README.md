# `database-files` Folder

## **Rate My Co-Op Database** 

## **Database Architecture**

### **Database Schema**
The database is designed to support comprehensive co-op experience tracking with tables for:

- Students
- Companies
- Co-op Positions
- Reviews
- Skills
- Administrators
- Data Analysts

### **Relational Model Overview**
The database is built using a MySQL relational model with carefully designed tables and relationships to support complex querying and data integrity.

### **Key Relationships and Constraints**

Primary and Foreign Key Design

- Each table uses an AUTO_INCREMENT integer id as a primary key
- Foreign keys establish relationships between tables, ensuring referential integrity
- Implemented with ON DELETE CASCADE and ON UPDATE CASCADE where appropriate to maintain data consistency


## **Core Tables and Their Relationships**

### **Student-Centric Relationships**

student table: Central to user profiles

- Linked to student_coops (many-to-many with co-op positions)
- Connected to student_skills (many-to-many skill association)
- Contains fields like openToConnect for networking features



### **Review and Skill Ecosystem**

review table connects students to co-op positions

- Foreign keys to student and coop_position
- Linked to review_skills for granular skill tagging


skill table allows complex skill tracking across reviews and student profiles

### **Company and Position Tracking**

- company table stores organization details
- coop_position links to company via foreign key
- Includes detailed position metadata like hourly_wage, avg_rating

### **Administrative and Analytical Layers**

- admin and data_analyst tables manage platform governance
- tasks and reports tables enable internal workflow and data analysis
- logs table provides audit trail functionality

## **Database Setup and Bootstrap** 
### **Prerequisites**

- MySQL Server
- MySQL Client or Management Tool (e.g. DataGrip)

### **Installation Steps**

1. Create Database
mysql -u [your_username] -p

2. Run Database Setup Script
Open the SQL script and execute it in your MySQL client. This will:

- Drop existing RMCDatabase if it exists
- Create a new RMCDatabase
- Create all necessary tables with appropriate relationships


3. Verify Installation

USE RMCDatabase;

SHOW TABLES;  -- Confirm all tables are created