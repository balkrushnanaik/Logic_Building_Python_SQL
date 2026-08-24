CREATE DATABASE advanced_sql_concepts;
USE advanced_sql_concepts;

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    department VARCHAR(100),
    duration INT
);

INSERT INTO courses (course_id, course_name, department, duration)
VALUES
(101, 'Computer Engineering', 'Engineering', 4),
(102, 'Information Technology', 'Engineering', 4),
(103, 'Data Science', 'Computer Science', 3),
(104, 'Artificial Intelligence', 'Computer Science', 4),
(105, 'Mechanical Engineering', 'Engineering', 4),
(106, 'Civil Engineering', 'Engineering', 4),
(107, 'Electronics Engineering', 'Engineering', 4),
(108, 'Business Analytics', 'Management', 2),
(109, 'Cyber Security', 'Computer Science', 3),
(110, 'Cloud Computing', 'Computer Science', 3);

SELECT * FROM courses;