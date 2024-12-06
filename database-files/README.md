# `database-files` Folder

## ** Rate My Co-Op Database ** 
## ** Project Overview **
Rate My Co-Op is a platform designed to revolutionize the co-op search process for students by providing transparent, meaningful insights into co-op experiences. Our goal is to transform the co-op search from a random process into a strategic career move.

## ** Key Features **

- Anonymous, structured reviews of co-op experiences
- Detailed student and company profiles
- Skill and career alignment tracking
- Networking capabilities for co-op seekers

## ** Problem Statement **
Current co-op search platforms like NUWorks provide basic information about positions but lack:

- In-depth insights about learning opportunities
- Real student experiences
- Career growth potential
- Targeted matching based on student interests and skills

## ** Database Schema **
The database is designed to support comprehensive co-op experience tracking with tables for:

- Students
- Companies
- Co-op Positions
- Reviews
- Skills
- Administrators
- Data Analysis

## ** Database Setup and Bootstrap** 
## ** Prerequisites **

- MySQL Server
- MySQL Client or Management Tool

## ** Installation Steps **

1. Create Database
mysql -u [your_username] -p

2. Run Database Setup Script
Open the SQL script and execute it in your MySQL client. This will:

3. Drop existing RMCDatabase if it exists
Create a new RMCDatabase
Create all necessary tables with appropriate relationships


4. Verify Installation
USE RMCDatabase;
SHOW TABLES;  -- Confirm all tables are created