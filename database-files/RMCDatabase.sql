DROP DATABASE IF EXISTS RMCDatabase;

CREATE DATABASE IF NOT EXISTS RMCDatabase;

USE RMCDatabase;

CREATE TABLE student
(
    id          integer AUTO_INCREMENT PRIMARY KEY,
    full_name varchar(30),
    openToConnect bool DEFAULT true,
    username    varchar(25) UNIQUE NOT NULL,
    profileType varchar(25),
    major varchar(25),
    home_college varchar(40),
    linkedin varchar(40)
);

CREATE TABLE company
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    industry varchar(30),
    name varchar(20)
);

CREATE TABLE coop_position
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    company_id integer,
    industry varchar(25),
    workload varchar(25),
    hourly_wage float(2, 2),
    title varchar(25),
    avg_rating float(1, 1),
    description varchar(5000),
    FOREIGN KEY (company_id) REFERENCES company(id)
);

CREATE TABLE student_coops
(
    student_id integer,
    coop_id integer,
    PRIMARY KEY (student_id, coop_id),
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (coop_id) REFERENCES coop_position(id)
);

CREATE TABLE review
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    student_id integer,
    review_text varchar(255),
    rating float(1, 1),
    position_id int,
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (position_id) REFERENCES coop_position(id)
);

CREATE TABLE skill
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    name varchar(25)
);

CREATE TABLE review_skills
(
    review_id integer,
    skill_id integer,
    PRIMARY KEY (review_id, skill_id),
    FOREIGN KEY (review_id) REFERENCES review(id),
    FOREIGN KEY (skill_id) REFERENCES skill(id)
);

CREATE TABLE student_skills
(
    student_id integer,
    skill_id integer,
    PRIMARY KEY (student_id, skill_id),
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (skill_id) REFERENCES skill(id)
);

CREATE TABLE admin
(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name varchar(25),
    role varchar(25),
    email varchar(25)
);

CREATE TABLE applications
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    admin_id integer,
    version varchar(25),
    description varchar(200),
    name varchar(25),
    FOREIGN KEY (admin_id) REFERENCES admin(id)
);

CREATE TABLE logs
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    app_id integer,
    timestamp datetime DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (app_id) REFERENCES applications(id)
);

CREATE TABLE data_analyst
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    email varchar(25),
    name varchar(25),
    role varchar(40)
);

CREATE TABLE tasks
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    report_id integer,
    created_by integer,
    name varchar(25),
    status varchar(15),
    assigned_to integer,
    timestamp datetime DEFAULT CURRENT_TIMESTAMP,
    description varchar(100),
    FOREIGN KEY (created_by) REFERENCES admin(id),
    FOREIGN KEY (assigned_to) REFERENCES data_analyst(id)
);

CREATE TABLE reports
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    company_id integer,
    created_by integer,
    report_name varchar(25),
    industry_compare varchar(50),
    timestamp datetime DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES company(id),
    FOREIGN KEY (created_by) REFERENCES data_analyst(id)
);

CREATE TABLE task_reports
(
    task_id integer,
    report_id integer,
    PRIMARY KEY (task_id, report_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (report_id) REFERENCES reports(id)
);

CREATE TABLE trends
(
    position_id integer AUTO_INCREMENT PRIMARY KEY,
    industry varchar(30),
    skill_alignments varchar(25),
    career_alignments varchar(25),
    satisfaction_alignments varchar(25),
    FOREIGN KEY (position_id) REFERENCES reports(id)
);