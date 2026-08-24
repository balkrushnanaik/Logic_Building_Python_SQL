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

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    city VARCHAR(50),
    course_id INT,
    marks DECIMAL(5,2),
    fees DECIMAL(10,2),
    admission_date DATE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO students
(student_id, name, age, gender, city, course_id, marks, fees, admission_date)
VALUES

(1, 'Aarav Sharma', 20, 'Male', 'Pune', 101, 85, 75000, '2024-06-15'),

(2, 'Priya Patil', 21, 'Female', 'Mumbai', 101, 92, 78000, '2024-07-10'),

(3, 'Rahul Verma', 19, 'Male', 'Nashik', 101, 72, 72000, '2025-06-20'),

(4, 'Sneha Joshi', 22, 'Female', 'Pune', 101, 88, 75000, '2025-07-05'),

(5, 'Rohan Kulkarni', 23, 'Male', 'Nagpur', 101, 65, 70000, '2023-06-18'),

(6, 'Ananya Deshmukh', 20, 'Female', 'Pune', 101, 92, 78000, '2024-06-25'),

(7, 'Vikas More', 21, 'Male', 'Mumbai', 101, 45, 68000, '2023-07-12'),

(8, 'Aisha Khan', 19, 'Female', 'Aurangabad', 101, 78, 73000, '2025-06-22'),

(9, 'Aditya Shah', 24, 'Male', 'Pune', 102, 81, 65000, '2024-06-14'),

(10, 'Neha Pawar', 20, 'Female', 'Mumbai', 102, 74, 68000, '2024-07-08'),

(11, 'Amit Joshi', 22, 'Male', 'Nashik', 102, 59, 62000, '2023-06-19'),

(12, 'Kavya Patil', 21, 'Female', 'Pune', 102, 91, 70000, '2025-06-16'),

(13, 'Akash Jadhav', 20, 'Male', 'Kolhapur', 102, 68, 65000, '2025-07-01'),

(14, 'Pooja Shinde', 23, 'Female', 'Pune', 102, 83, 67000, '2024-06-28'),

(15, 'Sahil Mehta', 19, 'Male', 'Mumbai', 102, 42, 60000, '2023-07-15'),

(16, 'Riya Gupta', 22, 'Female', 'Nashik', 103, 95, 85000, '2024-06-12'),

(17, 'Arjun Naik', 21, 'Male', 'Pune', 103, 88, 82000, '2024-07-04'),

(18, 'Simran Kaur', 20, 'Female', 'Mumbai', 103, 76, 80000, '2025-06-21'),

(19, 'Raj Malhotra', 23, 'Male', 'Delhi', 103, 67, 78000, '2023-06-17'),

(20, 'Meera Nair', 21, 'Female', 'Pune', 103, 95, 85000, '2025-07-09'),

(21, 'Abhishek Patil', 22, 'Male', 'Nashik', 103, 54, 75000, '2024-06-30'),

(22, 'Isha Sharma', 19, 'Female', 'Pune', 103, 82, 81000, '2025-06-25'),

(23, 'Omkar Desai', 20, 'Male', 'Mumbai', 104, 90, 90000, '2024-06-11'),

(24, 'Snehal More', 21, 'Female', 'Pune', 104, 87, 88000, '2024-07-02'),

(25, 'Karan Singh', 22, 'Male', 'Delhi', 104, 73, 85000, '2023-06-20'),

(26, 'Nikita Pawar', 20, 'Female', 'Nashik', 104, 96, 92000, '2025-06-14'),

(27, 'Siddharth Joshi', 24, 'Male', 'Pune', 104, 61, 82000, '2023-07-10'),

(28, 'Tanvi Kulkarni', 21, 'Female', 'Mumbai', 104, 87, 88000, '2025-07-05'),

(29, 'Yash Thakur', 19, 'Male', 'Pune', 105, 79, 70000, '2024-06-18'),

(30, 'Komal Jadhav', 22, 'Female', 'Nashik', 105, 84, 72000, '2024-07-11'),

(31, 'Rohit Sharma', 23, 'Male', 'Mumbai', 105, 56, 68000, '2023-06-15'),

(32, 'Divya Patil', 20, 'Female', 'Pune', 105, 71, 70000, '2025-06-19'),

(33, 'Manish Gupta', 21, 'Male', 'Nagpur', 105, 63, 67000, '2025-07-03'),

(34, 'Swati Deshmukh', 22, 'Female', 'Pune', 105, 89, 75000, '2024-06-27'),

(35, 'Nilesh More', 24, 'Male', 'Nashik', 106, 52, 60000, '2023-06-13'),

(36, 'Pallavi Shah', 21, 'Female', 'Pune', 106, 77, 64000, '2024-07-06'),

(37, 'Saurabh Patil', 22, 'Male', 'Mumbai', 106, 69, 62000, '2025-06-23'),

(38, 'Sneha Kulkarni', 20, 'Female', 'Pune', 106, 91, 68000, '2025-07-08'),

(39, 'Vijay Pawar', 23, 'Male', 'Nashik', 106, 44, 58000, '2024-06-16'),

(40, 'Mansi Joshi', 19, 'Female', 'Pune', 107, 86, 73000, '2024-07-12'),

(41, 'Harsh Shah', 21, 'Male', 'Mumbai', 107, 75, 70000, '2023-06-21'),

(42, 'Aditi More', 20, 'Female', 'Pune', 107, 93, 75000, '2025-06-17'),

(43, 'Nikhil Patil', 22, 'Male', 'Nashik', 107, 58, 67000, '2025-07-04'),

(44, 'Sakshi Jadhav', 21, 'Female', 'Pune', 107, 81, 72000, '2024-06-29'),

(45, 'Ritesh Sharma', 24, 'Male', 'Mumbai', 108, 66, 55000, '2024-07-07'),

(46, 'Kajal Gupta', 22, 'Female', 'Pune', 108, 88, 60000, '2025-06-15'),

(47, 'Aniket Desai', 20, 'Male', 'Nashik', 108, 74, 58000, '2025-07-01'),

(48, 'Rashmi Patil', 21, 'Female', 'Pune', 108, 94, 62000, '2024-06-20'),

(49, 'Vishal More', 23, 'Male', 'Mumbai', 109, 82, 80000, '2023-06-18'),

(50, 'Shreya Joshi', 20, 'Female', 'Pune', 109, 91, 85000, '2024-07-05'),

(51, 'Amol Pawar', 22, 'Male', 'Nashik', 109, 57, 78000, '2025-06-22'),

(52, 'Priti Shah', 21, 'Female', 'Pune', 109, 86, 82000, '2025-07-10'),

(53, 'Aman Verma', 19, 'Male', 'Mumbai', 109, 49, 75000, '2024-06-14'),

(54, 'Anjali Nair', 22, 'Female', 'Pune', 109, 96, 85000, '2023-07-08'),

(55, 'Rakesh Patil', 23, 'Male', 'Nagpur', 101, NULL, 76000, '2026-06-15'),

(56, 'Priyanka More', 20, 'Female', 'Pune', 102, 73, NULL, '2026-06-20'),

(57, 'Anil Sharma', 21, 'Male', 'Mumbai', 103, NULL, 83000, '2026-07-01'),

(58, 'Anusha Patil', 22, 'Female', 'Nashik', 104, 89, NULL, '2026-07-05'),

(59, 'Rajesh Kumar', 24, 'Male', 'Pune', 105, 38, 69000, '2026-06-25'),

(60, 'Aarohi Joshi', 20, 'Female', 'Pune', 109, 90, 84000, '2026-07-10');


SELECT * FROM students;