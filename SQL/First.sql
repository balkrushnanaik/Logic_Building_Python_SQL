CREATE DATABASE logic_building;
USE logic_building;
 
 /*
# 1. Student Information System

Create a table to store student details such as roll number, name, department, age, city, and marks.
Insert at least 10 records.
Write queries to:

* Display all students
* Find students from Pune
* Find students with marks greater than 80
* Sort students by marks in descending order

*/

CREATE TABLE student(
roll_number INT PRIMARY KEY,
name VARCHAR(100),
department VARCHAR(100),
age INT,
city VARCHAR(100)
);

INSERT INTO student VALUES 
(21, 'Soumya', 'Computer', 22, 'Pune'),
(22, 'Ramya', 'Computer', 22, 'Pune'),
(23, 'Namya', 'Computer', 25, 'Pune'),
(24, 'Aarya', 'Computer', 29, 'Pune'),
(25, 'Karya', 'Computer', 21, 'Pune'),
(26, 'Sara', 'Computer', 22, 'Pune'),
(27, 'kranti', 'Computer', 22, 'Pune'),
(28, 'Nandini', 'Computer', 22, 'Pune'),
(29, 'Vaibhav', 'Computer', 25, 'Pune'),
(30, 'Lokesh', 'Computer', 26, 'Pune');

SELECT * FROM student;

SELECT * FROM student
WHERE city = 'Pune';




