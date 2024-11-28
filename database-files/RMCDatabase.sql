DROP DATABASE IF EXISTS RMCDatabase;

CREATE DATABASE IF NOT EXISTS RMCDatabase;

USE RMCDatabase;

CREATE TABLE student
(
    id          integer AUTO_INCREMENT PRIMARY KEY,
    openToConnect bool DEFAULT true,
    username    varchar(25) UNIQUE NOT NULL,
    profileType varchar(25),
    major varchar(25),
    home_college varchar(40),
    linkedin varchar(30)
);

