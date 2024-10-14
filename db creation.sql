CREATE DATABASE hospital_management;

USE hospital_management;

CREATE TABLE patients (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL
);

CREATE TABLE doctors (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    speciality VARCHAR(100) NOT NULL
);
