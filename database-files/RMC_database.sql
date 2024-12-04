DROP DATABASE IF EXISTS RMCDatabase;

CREATE DATABASE IF NOT EXISTS RMCDatabase;

USE RMCDatabase;

CREATE TABLE IF NOT EXISTS student
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

CREATE TABLE IF NOT EXISTS company
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    industry varchar(30),
    name varchar(20)
);

CREATE TABLE IF NOT EXISTS coop_position (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    company_id INTEGER,
    industry VARCHAR(25),
    workload VARCHAR(25),
    hourly_wage DECIMAL(4, 2),
    title VARCHAR(50),
    avg_rating DECIMAL(2, 1),
    description VARCHAR(5000),
    FOREIGN KEY (company_id) REFERENCES company(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS student_coops (
    student_id INTEGER,
    coop_id INTEGER,
    PRIMARY KEY (student_id, coop_id),
    FOREIGN KEY (student_id) REFERENCES student(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (coop_id) REFERENCES coop_position(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS review (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    student_id INTEGER,
    review_text VARCHAR(255),
    rating DECIMAL(2, 1),
    position_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES student(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (position_id) REFERENCES coop_position(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS skill
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    name varchar(50)
);

CREATE TABLE IF NOT EXISTS review_skills (
    review_id INTEGER NOT NULL,
    skill_id INTEGER NOT NULL,
    PRIMARY KEY (review_id, skill_id),
    FOREIGN KEY (review_id) REFERENCES review(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skill(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS student_skills (
    student_id INTEGER,
    skill_id INTEGER,
    PRIMARY KEY (student_id, skill_id),
    FOREIGN KEY (student_id) REFERENCES student(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skill(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS admin
(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name varchar(25),
    role varchar(40),
    email varchar(35)
);

CREATE TABLE IF NOT EXISTS applications (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    admin_id INTEGER,
    version VARCHAR(25),
    description VARCHAR(200),
    name VARCHAR(40),
    FOREIGN KEY (admin_id) REFERENCES admin(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS logs (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    app_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (app_id) REFERENCES applications(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS data_analyst
(
    id integer AUTO_INCREMENT PRIMARY KEY,
    email varchar(25),
    name varchar(25),
    role varchar(40)
);

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    report_id INTEGER,
    created_by INTEGER,
    name VARCHAR(40),
    status VARCHAR(15),
    assigned_to INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(200),
    FOREIGN KEY (created_by) REFERENCES admin(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (assigned_to) REFERENCES data_analyst(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (report_id) REFERENCES reports(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS reports (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    company_id INTEGER,
    created_by INTEGER,
    report_name VARCHAR(50),
    industry_compare VARCHAR(50),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES company(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (created_by) REFERENCES data_analyst(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS task_reports (
    task_id   INTEGER NOT NULL,
    report_id INTEGER NOT NULL,
    PRIMARY KEY (task_id, report_id),
    FOREIGN KEY (task_id) REFERENCES tasks(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (report_id) REFERENCES reports(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS trends (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    position_id INTEGER,
    industry VARCHAR(30),
    skill_alignments VARCHAR(100),
    career_alignments VARCHAR(40),
    satisfaction_alignments VARCHAR(40),
    FOREIGN KEY (position_id) REFERENCES reports(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
