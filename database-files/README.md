# `database-files` Folder

** Rate My Co-Op Database ** 
** Project Overview **
Rate My Co-Op is a platform designed to revolutionize the co-op search process for students by providing transparent, meaningful insights into co-op experiences. Our goal is to transform the co-op search from a random process into a strategic career move.

** Key Features **

- Anonymous, structured reviews of co-op experiences
- Detailed student and company profiles
- Skill and career alignment tracking
- Networking capabilities for co-op seekers

Problem Statement
Current co-op search platforms like NUWorks provide basic information about positions but lack:

In-depth insights about learning opportunities
Real student experiences
Career growth potential
Targeted matching based on student interests and skills

Database Schema
The database is designed to support comprehensive co-op experience tracking with tables for:

Students
Companies
Co-op Positions
Reviews
Skills
Administrators
Data Analysis

Database Setup and Bootstrap
Prerequisites

MySQL Server
MySQL Client or Management Tool

Installation Steps

Create Database
bashCopymysql -u [your_username] -p

Run Database Setup Script
Open the SQL script and execute it in your MySQL client. This will:

Drop existing RMCDatabase if it exists
Create a new RMCDatabase
Create all necessary tables with appropriate relationships


Verify Installation
sqlCopyUSE RMCDatabase;
SHOW TABLES;  -- Confirm all tables are created


Recommended Post-Installation

Set up appropriate user permissions
Create database backups
Implement additional security measures

Development Roadmap

Implement user authentication
Develop API endpoints for data interaction
Create frontend interfaces
Implement advanced filtering and matching algorithms
Develop reporting and trend analysis features

Contributing

Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Create a Pull Request