CREATE DATABASE basic_problems;
USE basic_problems;

/*
 Absolutely. Here are **50 basic SQL problem statements**, arranged from easy to slightly more challenging. These are good for practicing **SELECT, WHERE, ORDER BY, GROUP BY, HAVING, aggregate functions, and basic JOINs**.

### 🟢 Level 1 — SELECT & Basic Queries

Assume a table named `students`:

`student_id, name, age, gender, city, course, marks, fees`

1. Display all records from the `students` table.
2. Display only the `name` and `city` of all students.
3. Display the names and marks of all students.
4. Find the total number of students.
5. Find the average marks of all students.
6. Find the highest marks obtained by a student.
7. Find the lowest marks obtained by a student.
8. Find the total fees collected from all students.
9. Display students whose marks are greater than 70.
10. Display students whose marks are less than 40.

### 🟡 Level 2 — WHERE Conditions

11. Display students who are from `Pune`.
12. Display students who are enrolled in the `Computer Engineering` course.
13. Display students whose age is greater than 20.
14. Display students whose age is between 18 and 22.
15. Display students who scored between 60 and 80 marks.
16. Display students who are not from `Mumbai`.
17. Display students whose gender is `Female`.
18. Display students whose fees are greater than ₹50,000.
19. Display students from either `Pune` or `Mumbai`.
20. Display students who are from `Pune` and have marks greater than 75.

### 🟠 Level 3 — ORDER BY, DISTINCT & LIMIT

21. Display all students sorted by marks in ascending order.
22. Display all students sorted by marks in descending order.
23. Display students sorted by name alphabetically.
24. Display the top 5 students based on marks.
25. Display the 3 students with the lowest marks.
26. Display all unique cities from the `students` table.
27. Display all unique courses.
28. Display students sorted first by city and then by marks descending.
29. Display the student with the highest marks.
30. Display the student with the lowest marks.

### 🔵 Level 4 — Aggregate Functions & GROUP BY

31. Find the number of students in each city.
32. Find the average marks for each course.
33. Find the highest marks in each course.
34. Find the lowest marks in each course.
35. Find the total fees collected for each course.
36. Find the number of students in each course.
37. Find the average age of students in each city.
38. Find courses where the average marks are greater than 70.
39. Find cities having more than 5 students.
40. Find courses where total fees collected are greater than ₹5,00,000.

### 🟣 Level 5 — Basic JOIN Practice

Assume another table:

`courses`

`course_id, course_name, department, duration`

And modify `students` to include:

`student_id, name, age, city, course_id, marks, fees`

41. Display each student's name along with their course name.
42. Display students along with their course department.
43. Display students who belong to the `Computer Engineering` department.
44. Display the number of students enrolled in each course.
45. Display the average marks for each course.
46. Display the highest-scoring student from each course.
47. Display courses that have no students enrolled.
48. Display students whose course duration is greater than 3 years.
49. Display the total fees collected for each course.
50. Display the course name, number of students, average marks, and total fees collected for each course.

### 📌 Recommended order for you

Since you're practicing SQL for **Data Analytics**, solve them in this order:

**1–10 → SELECT + aggregate functions**
**11–20 → WHERE + AND/OR/BETWEEN**
**21–30 → ORDER BY + DISTINCT + LIMIT**
**31–40 → GROUP BY + HAVING** ⭐
**41–50 → JOIN + GROUP BY** ⭐⭐

If you want, I can also give you a **realistic `students` dataset with 100+ rows** specifically designed to solve all 50 problems.

 */
 ## 🟢 Level 1 — SELECT & Basic Queries

# Assume a table named `students`:
#
# `student_id, name, age, gender, city, course, marks, fees`
    CREATE TABLE students(
        student_id INT PRIMARY KEY,
        name VARCHAR(50),
        age INT CHECK ( age > 0 and age <=100 ),
        gender CHAR(10),
        city VARCHAR(50),
        course VARCHAR(50),
        marks INT,
        fees float
    );
INSERT INTO students
(student_id, name, age, gender, city, course, marks, fees)
VALUES
(1, 'Aarav Sharma', 20, 'Male', 'Pune', 'Computer Engineering', 85, 85000),
(2, 'Priya Patil', 21, 'Female', 'Mumbai', 'Information Technology', 92, 90000),
(3, 'Rohan Jadhav', 19, 'Male', 'Nashik', 'Computer Engineering', 76, 85000),
(4, 'Sneha Kulkarni', 22, 'Female', 'Pune', 'Electronics', 68, 75000),
(5, 'Aditya Deshmukh', 20, 'Male', 'Nagpur', 'Mechanical Engineering', 72, 70000),
(6, 'Ananya Joshi', 21, 'Female', 'Mumbai', 'Computer Engineering', 88, 85000),
(7, 'Vivek Pawar', 23, 'Male', 'Pune', 'Civil Engineering', 61, 65000),
(8, 'Neha Shinde', 20, 'Female', 'Nashik', 'Information Technology', 79, 90000),
(9, 'Rahul More', 22, 'Male', 'Ahmednagar', 'Computer Engineering', 91, 85000),
(10, 'Pooja Gaikwad', 19, 'Female', 'Pune', 'Electronics', 73, 75000),

(11, 'Akash Chavan', 21, 'Male', 'Mumbai', 'Mechanical Engineering', 65, 70000),
(12, 'Isha Bhosale', 20, 'Female', 'Pune', 'Information Technology', 94, 90000),
(13, 'Sahil Wagh', 22, 'Male', 'Nashik', 'Civil Engineering', 58, 65000),
(14, 'Kavya Pawar', 21, 'Female', 'Nagpur', 'Computer Engineering', 87, 85000),
(15, 'Omkar Kadam', 20, 'Male', 'Pune', 'Computer Engineering', 71, 85000),
(16, 'Riya Sutar', 23, 'Female', 'Mumbai', 'Electronics', 83, 75000),
(17, 'Yash Thakur', 19, 'Male', 'Ahmednagar', 'Information Technology', 69, 90000),
(18, 'Snehal More', 22, 'Female', 'Pune', 'Civil Engineering', 77, 65000),
(19, 'Kunal Patil', 21, 'Male', 'Nashik', 'Mechanical Engineering', 82, 70000),
(20, 'Sakshi Joshi', 20, 'Female', 'Mumbai', 'Computer Engineering', 96, 85000),

(21, 'Harsh Vaidya', 22, 'Male', 'Pune', 'Information Technology', 74, 90000),
(22, 'Tanvi Shinde', 19, 'Female', 'Nagpur', 'Electronics', 89, 75000),
(23, 'Manish Kale', 23, 'Male', 'Mumbai', 'Civil Engineering', 55, 65000),
(24, 'Aditi Deshmukh', 21, 'Female', 'Pune', 'Computer Engineering', 81, 85000),
(25, 'Soham Pawar', 20, 'Male', 'Nashik', 'Information Technology', 90, 90000),
(26, 'Meera Kulkarni', 22, 'Female', 'Ahmednagar', 'Mechanical Engineering', 67, 70000),
(27, 'Nikhil Jadhav', 21, 'Male', 'Pune', 'Computer Engineering', 78, 85000),
(28, 'Shruti Chavan', 20, 'Female', 'Mumbai', 'Information Technology', 86, 90000),
(29, 'Prathamesh More', 19, 'Male', 'Nagpur', 'Civil Engineering', 63, 65000),
(30, 'Mansi Gaikwad', 22, 'Female', 'Pune', 'Electronics', 75, 75000),

(31, 'Tejas Patil', 21, 'Male', 'Nashik', 'Computer Engineering', 93, 85000),
(32, 'Swara Bhosale', 20, 'Female', 'Mumbai', 'Mechanical Engineering', 70, 70000),
(33, 'Ruturaj Pawar', 23, 'Male', 'Pune', 'Information Technology', 84, 90000),
(34, 'Komal Wagh', 19, 'Female', 'Ahmednagar', 'Civil Engineering', 59, 65000),
(35, 'Atharva Shinde', 22, 'Male', 'Nagpur', 'Computer Engineering', 88, 85000),
(36, 'Siddhi More', 21, 'Female', 'Pune', 'Electronics', 80, 75000),
(37, 'Abhishek Joshi', 20, 'Male', 'Mumbai', 'Information Technology', 95, 90000),
(38, 'Vaishnavi Kale', 22, 'Female', 'Nashik', 'Computer Engineering', 73, 85000),
(39, 'Akshay Kadam', 21, 'Male', 'Pune', 'Mechanical Engineering', 62, 70000),
(40, 'Gauri Patil', 20, 'Female', 'Mumbai', 'Civil Engineering', 76, 65000),

(41, 'Shubham Deshmukh', 23, 'Male', 'Pune', 'Computer Engineering', 89, 85000),
(42, 'Rutuja Pawar', 21, 'Female', 'Nagpur', 'Information Technology', 91, 90000),
(43, 'Ganesh Chavan', 20, 'Male', 'Nashik', 'Electronics', 64, 75000),
(44, 'Manasi Jadhav', 22, 'Female', 'Pune', 'Computer Engineering', 97, 85000),
(45, 'Sanket More', 19, 'Male', 'Ahmednagar', 'Mechanical Engineering', 57, 70000),
(46, 'Dipali Shinde', 21, 'Female', 'Mumbai', 'Information Technology', 83, 90000),
(47, 'Akash Pawar', 22, 'Male', 'Pune', 'Civil Engineering', 71, 65000),
(48, 'Pallavi Kulkarni', 20, 'Female', 'Nashik', 'Computer Engineering', 92, 85000),
(49, 'Vishal Gaikwad', 23, 'Male', 'Nagpur', 'Information Technology', 68, 90000),
(50, 'Kiran Patil', 21, 'Female', 'Pune', 'Electronics', 79, 75000);
#
# 1. Display all records from the `students` table.
    SELECT * FROM students;
# 2. Display only the `name` and `city` of all students.
    SELECT name, city FROM students;
# 3. Display the names and marks of all students.
    SELECT name, marks FROM students;
# 4. Find the total number of students.
    SELECT COUNT(*) AS Total_Students
    FROM students;
# 5. Find the average marks of all students.
    SELECT AVG(students.marks) AS Average_Marks
    FROM students;
# 6. Find the highest marks obtained by a student.
    SELECT MAX(students.marks)  AS Highest_Marks
    FROM students;
# 7. Find the lowest marks obtained by a student.
    SELECT MIN(students.marks)  AS Lowest_Marks
    FROM students;
# 8. Find the total fees collected from all students.
    SELECT SUM(students.fees) AS Total_Fees
    FROM students;
# 9. Display students whose marks are greater than 70.
    SELECT * FROM students
    WHERE marks > 70;
# 10. Display students whose marks are less than 60.
SELECT * FROM students
WHERE marks < 60;

### 🟡 Level 2 — WHERE Conditions

# 11. Display students who are from `Pune`.
    SELECT *
    FROM students
    WHERE city = 'Pune';
# 12. Display students who are enrolled in the `Computer Engineering` course.
    SELECT *
    FROM students
    WHERE course = 'Computer Engineering';
# 13. Display students whose age is greater than 20.
    SELECT *
    FROM students
    WHERE age > 20;
# 14. Display students whose age is between 18 and 22.
    SELECT *
    FROM students
    WHERE age BETWEEN 18 and 22;
# 15. Display students who scored between 60 and 80 marks.
    SELECT *
    FROM students
    WHERE marks BETWEEN 60 and 80;
# 16. Display students who are not from `Mumbai`.
    SELECT *
    FROM students
    WHERE city <> 'Mumbai';
# 17. Display students whose gender is `Female`.
    SELECT *
    FROM students
    WHERE gender = 'Female';
# 18. Display students whose fees are greater than ₹50,000.
    SELECT *
    FROM students
    WHERE fees > 50000;
# 19. Display students from either `Pune` or `Mumbai`.
SELECT *
FROM students
WHERE city = 'Pune' OR city = 'Mumbai';
# 20. Display students who are from `Pune` and have marks greater than 75.
SELECT *
FROM students
WHERE city = 'Pune' AND marks > 75;


### 🟠 Level 3 — ORDER BY, DISTINCT & LIMIT

# 21. Display all students sorted by marks in ascending order.
    SELECT *
    FROM students
    ORDER BY marks; # By default assending
# 22. Display all students sorted by marks in descending order.
     SELECT *
    FROM students
    ORDER BY marks DESC ;
# 23. Display students sorted by name alphabetically.
    SELECT *
    FROM students
    ORDER BY name;
# 24. Display the top 5 students based on marks.
    SELECT *
    FROM students
    ORDER BY marks DESC
    LIMIT 5;
# 25. Display the 3 students with the lowest marks.
    SELECT *
    FROM students
    ORDER BY marks
    LIMIT 3;
# 26. Display all unique cities from the `students` table.
   SELECT DISTINCT students.city
   FROM students;
# 27. Display all unique courses.
    SELECT DISTINCT students.course
    FROM students;
# 28. Display students sorted first by city and then by marks descending.
    SELECT *
    FROM students
    ORDER BY city ASC,  marks DESC;
# 29. Display the student with the highest marks.
    SELECT *
    FROM students
    ORDER BY marks DESC ;
# 30. Display the student with the lowest marks.
SELECT *
FROM students
ORDER BY marks;

### 🔵 Level 4 — Aggregate Functions & GROUP BY

# 31. Find the number of students in each city.
    SELECT city, COUNT(student_id) AS Total_Students
    FROM students
    GROUP BY city;
# 32. Find the average marks for each course.
    SELECT students.course, AVG(marks) AS Average_Marks
    FROM students
    GROUP BY course;
# 33. Find the highest marks in each course.
    SELECT course, MAX(marks) AS Highest_Marks
    FROM students
    GROUP BY course;
# 34. Find the lowest marks in each course.
    SELECT course, MIN(marks) AS Lowest_Marks
    FROM students
    GROUP BY course;
# 35. Find the total fees collected for each course.
    SELECT course, SUM(fees) AS Total_Fee
    FROM students
    GROUP BY course;
# 36. Find the number of students in each course.
# 37. Find the average age of students in each city.
# 38. Find courses where the average marks are greater than 70.
# 39. Find cities having more than 5 students.
# 40. Find courses where total fees collected are greater than ₹5,00,000.
