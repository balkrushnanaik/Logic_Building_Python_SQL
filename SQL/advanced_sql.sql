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

/*
 Absolutely. Since you’ve completed the first 50 covering **SELECT, WHERE, ORDER BY, GROUP BY, HAVING, aggregates, and basic JOINs**, the next step should introduce concepts you’ll actually need for **Data Analyst / SQL interview preparation**.

Here are **50 new SQL problems on different concepts**, including `CASE`, `NULL`, `LIKE`, `IN`, `EXISTS`, subqueries, CTEs, window functions, string/date functions, self joins, and set operators.

### 🟢 Level 6 — CASE, NULL & Conditional Logic

Assume:

`students(student_id, name, age, gender, city, course_id, marks, fees)`

51. Display each student's name and a new column `result` as **Pass** if marks ≥ 40, otherwise **Fail**.

52. Display each student's name and categorize marks:

* 80–100 → Excellent
* 60–79 → Good
* 40–59 → Average
* Below 40 → Poor

53. Display each student's name and classify their age:

* Below 18 → Minor
* 18–22 → Young
* Above 22 → Adult

54. Display student name, marks, and a `grade` column:

* 90+ → A+
* 80–89 → A
* 70–79 → B
* 60–69 → C
* Below 60 → D

55. Display students with their fees and classify them as `High Fee`, `Medium Fee`, or `Low Fee`.

56. Find the number of students who passed and failed.

57. Find the number of students in each marks category.

58. Calculate the average marks of male and female students using `CASE`.

59. Calculate the total fees collected separately for male and female students.

60. Display students whose marks are `NULL`.

---

### 🟡 Level 7 — NULL, LIKE, IN & Advanced Filtering

61. Display students whose city is either Pune, Mumbai, or Nashik using `IN`.

62. Display students whose city is **not** Pune, Mumbai, or Nashik.

63. Display students whose names start with `A`.

64. Display students whose names end with `a`.

65. Display students whose names contain the letter `r`.

66. Display students whose names have exactly 5 characters.

67. Display students whose city starts with the letter `P`.

68. Display students whose marks are between 50 and 80 **and** whose city is Pune.

69. Display students whose course_id is not NULL.

70. Display students whose fees are NULL and replace NULL fees with `0` in the output.

---

### 🟠 Level 8 — Subqueries

71. Find students who scored more than the **average marks of all students**.

72. Find students who scored the **highest marks**.

73. Find students who scored less than the average marks.

74. Find students whose fees are greater than the average fees.

75. Find students who belong to the same course as student ID `10`.

76. Find students who have the same city as student ID `5`.

77. Find the second-highest marks using a subquery.

78. Find the third-highest marks using a subquery.

79. Find students whose marks are greater than the marks of **all students from Pune**.

80. Find students whose marks are greater than **at least one student from Mumbai**.

---

### 🔵 Level 9 — EXISTS, NOT EXISTS & Correlated Subqueries

Using:

`students(student_id, name, city, course_id, marks, fees)`

`courses(course_id, course_name, department, duration)`

81. Display courses for which at least one student is enrolled using `EXISTS`.

82. Display courses for which no student is enrolled using `NOT EXISTS`.

83. Display students whose course exists in the `courses` table using `EXISTS`.

84. Find students who have marks greater than the average marks of **their own course**.

85. Find the highest-scoring student from each course using a correlated subquery.

86. Find students whose fees are greater than the average fees of their course.

87. Find courses where at least one student has scored more than 90.

88. Find courses where **all students** have scored more than 40.

89. Find students who have the highest marks within their city.

90. Find students whose marks are higher than the average marks of students from their city.

---

### 🟣 Level 10 — String & Date Functions

Assume you also have:

`students(student_id, name, city, course_id, marks, fees, admission_date)`

91. Display each student's name in uppercase.

92. Display each student's name in lowercase.

93. Display the length of each student's name.

94. Display the first 3 characters of each student's name.

95. Concatenate the student's name and city into a single column.

96. Remove leading and trailing spaces from student names.

97. Display the year in which each student was admitted.

98. Display the month in which each student was admitted.

99. Find students who were admitted in the year 2025.

100. Find the number of students admitted in each year.

---

### 🔴 Level 11 — Window Functions ⭐⭐⭐

These are **very important for Data Analyst interviews**.

Use:

`students(student_id, name, city, course_id, marks, fees)`

101. Assign a unique row number to every student based on marks descending.

102. Rank students based on their marks using `RANK()`.

103. Rank students based on their marks using `DENSE_RANK()`.

104. Find the top 3 students from the entire college using `ROW_NUMBER()`.

105. Find the top 3 students from **each course**.

106. Find the highest-scoring student from each course using `RANK()`.

107. Display each student's marks along with the average marks of their course.

108. Display each student's marks and the difference between their marks and their course average.

109. Calculate the running total of fees based on student ID.

110. Calculate the cumulative average marks ordered by student ID.

---

### 🟤 Level 12 — LAG, LEAD & Advanced Window Functions

111. Display each student's marks along with the marks of the previous student.

112. Display each student's marks along with the marks of the next student.

113. Calculate the difference between each student's marks and the previous student's marks.

114. Find students whose marks are higher than the previous student's marks.

115. Find the second-highest student in each course using `DENSE_RANK()`.

116. Find the top 2 highest-fee-paying students from each course.

117. Find the lowest-scoring student from each course.

118. Calculate the percentage contribution of each student's fees to the total fees.

119. Calculate the percentage contribution of each course's fees to the total fees.

120. Display each course's total fees along with the previous course's total fees.

---

### 🚀 Most Important Problems for You

Because you're preparing for **Data Analytics**, I would particularly recommend solving these first:

| Priority | Problems | Concept                          |
| -------- | -------- | -------------------------------- |
| ⭐⭐⭐      | 51–59    | `CASE WHEN`                      |
| ⭐⭐⭐      | 71–80    | Subqueries                       |
| ⭐⭐⭐      | 81–90    | Correlated subqueries / `EXISTS` |
| ⭐⭐⭐      | 97–100   | Date functions                   |
| ⭐⭐⭐⭐     | 101–110  | Window functions                 |
| ⭐⭐⭐⭐     | 111–120  | `LAG`, `LEAD`, ranking           |

**Your SQL progression is now:**

`SELECT → WHERE → GROUP BY → HAVING → JOIN → CASE → Subqueries → EXISTS → String/Date Functions → Window Functions`

That is a much stronger progression for **Data Analyst SQL interviews** than continuing only with basic `JOIN` questions.

 */
 ### 🟢 Level 6 — CASE, NULL & Conditional Logic

    /*
     Syntax :
    CASE
    WHEN condition THEN value
    WHEN condition THEN value
    ELSE value
END
     */

# Assume:
#
# `students(student_id, name, age, gender, city, course_id, marks, fees)`
#
# 51. Display each student's name and a new column `result` as **Pass** if marks ≥ 40, otherwise **Fail**.
    SELECT
    name,
    marks,
    CASE
        WHEN marks >= 40 THEN 'Pass'
        ELSE 'Fail'
    END AS result
FROM students;
#
# 52. Display each student's name and categorize marks:
#
# * 80–100 → Excellent
# * 60–79 → Good
# * 40–59 → Average
# * Below 40 → Poor
   SELECT
       name,
       marks,
       CASE
           WHEN marks >= 80 THEN 'Excellent'
           WHEN marks >= 60 THEN 'Good'
           WHEN marks >= 40 THEN 'Average'
           ELSE 'Poor'
   END AS Result
   FROM students
   ORDER BY marks DESC;


#
# 53. Display each student's name and classify their age:
#
# * Below 18 → Minor
# * 18–22 → Young
# * Above 22 → Adult
    SELECT
        name,
        age,
        CASE
            WHEN age < 18 THEN 'Minor'
            WHEN age BETWEEN 18 AND 22 THEN 'Young'
            ELSE 'Adult'
        END AS Classified_Age
    FROM students;
#
# 54. Display student name, marks, and a `grade` column:
#
# * 90+ → A+
# * 80–89 → A
# * 70–79 → B
# * 60–69 → C
# * Below 60 → D
SELECT
    name,
    marks,
    CASE
        WHEN marks >= 90 THEN 'A+'
        WHEN marks BETWEEN 80 AND 89 THEN 'A'
        WHEN marks BETWEEN 70 AND 79 THEN 'B'
        WHEN marks BETWEEN 60 AND 69 THEN 'C'
        ELSE 'D'
    END AS grade
FROM students;
# 55. Display students with their fees and classify them as `High Fee`, `Medium Fee`, or `Low Fee`.
SELECT
    name,
    fees,
    CASE
        WHEN fees >= 50000 THEN 'High Fee'
        WHEN fees >= 30000 THEN 'Medium Fee'
        ELSE 'Low Fee'
    END AS Fee_Category
FROM students;
# 56. Find the number of students who passed and failed.
SELECT
    SUM(CASE
        WHEN marks >= 40 THEN 1
        ELSE 0
    END) AS Passed_Students,

    SUM(CASE
        WHEN marks < 40 THEN 1
        ELSE 0
    END) AS Failed_Students
FROM students;
# 57. Find the number of students in each marks category.
SELECT
    CASE
        WHEN marks >= 90 THEN 'A+'
        WHEN marks >= 80 THEN 'A'
        WHEN marks >= 70 THEN 'B'
        WHEN marks >= 60 THEN 'C'
        ELSE 'D'
    END AS Marks_Category,
    COUNT(*) AS Number_of_Students
FROM students
GROUP BY
    CASE
        WHEN marks >= 90 THEN 'A+'
        WHEN marks >= 80 THEN 'A'
        WHEN marks >= 70 THEN 'B'
        WHEN marks >= 60 THEN 'C'
        ELSE 'D'
    END;
# 58. Calculate the average marks of male and female students using `CASE`.
SELECT
    AVG(CASE
        WHEN gender = 'Male' THEN marks
    END) AS Average_Male_Marks,

    AVG(CASE
        WHEN gender = 'Female' THEN marks
    END) AS Average_Female_Marks
FROM students;
# 59. Calculate the total fees collected separately for male and female students.
SELECT
    SUM(CASE
        WHEN gender = 'Male' THEN fees
        ELSE 0
    END) AS Total_Male_Fees,

    SUM(CASE
        WHEN gender = 'Female' THEN fees
        ELSE 0
    END) AS Total_Female_Fees
FROM students;

# 60. Display students whose marks are `NULL`.
SELECT *
FROM students
WHERE marks IS NULL;


#  ### 🟡 Level 7 — NULL, LIKE, IN & Advanced Filtering
# ---
# 61. Display students whose city is either Pune, Mumbai, or Nashik using `IN`.
SELECT *
FROM students
WHERE city IN ('Pune','Mumbai','Nashik');
# 62. Display students whose city is **not** Pune, Mumbai, or Nashik.
SELECT *
FROM students
WHERE city NOT IN ('Pune','Mumbai','Nashik')  ;
# 63. Display students whose names start with `A`.
SELECT *
FROM students
WHERE name LIKE 'A%';
# 64. Display students whose names end with `a`.
SELECT *
FROM students
WHERE name LIKE 'a%';
# 65. Display students whose names contain the letter `r`.
SELECT *
FROM students
WHERE name LIKE '%r%';
# 66. Display students whose names have exactly 5 characters.
SELECT *
FROM students
WHERE LENGTH(name) = 5;
# 67. Display students whose city starts with the letter `P`.
SELECT *
FROM students
WHERE city LIKE 'P%';
#
# 68. Display students whose marks are between 50 and 80 **and** whose city is Pune.
 SELECT *
 FROM students
 WHERE marks between 50 AND 80 AND city = 'Pune';
# 69. Display students whose course_id is not NULL.
 SELECT *
 FROM students
 WHERE course_id IS NOT NULL;
# 70. Display students whose fees are NULL and replace NULL fees with `0` in the output.
SELECT name,
       COALESCE(fees, 0) AS fees
FROM students
WHERE fees IS NULL;
# ---

# ### 🟠 Level 8 — Subqueries
#
# 71. Find students who scored more than the **average marks of all students**.
    SELECT *
    FROM
        students
    WHERE marks > (
        SELECT AVG(marks)
        FROM students
 );

#
# 72. Find students who scored the **highest marks**.
   SELECT *
FROM students
WHERE marks = (
    SELECT MAX(marks)
    FROM students
);
#
# 73. Find students who scored less than the average marks.
 SELECT *
    FROM
        students
    WHERE marks < (
        SELECT AVG(marks)
        FROM students
 );
# 74. Find students whose fees are greater than the average fees.
 SELECT name, fees
    FROM
        students
    WHERE fees > (
        SELECT AVG(fees)
        FROM students
 );
# 75. Find students who belong to the same course as student ID `10`.
SELECT *
FROM students
WHERE course_id = (
    SELECT course_id
    FROM students
    WHERE student_id = 10
);
# 76. Find students who have the same city as student ID `5`.
SELECT *
FROM students
WHERE city = (
    SELECT city
    FROM students
    WHERE student_id = 5
);
# 77. Find the second-highest marks using a subquery.
SELECT MAX(marks) AS second_highest_marks
FROM students
WHERE marks < (
    SELECT MAX(marks)
    FROM students
);
# 78. Find the third-highest marks using a subquery.
SELECT MAX(marks) AS third_highest_marks
FROM students
WHERE marks < (
    SELECT MAX(marks)
    FROM students
    WHERE marks < (
        SELECT MAX(marks)
        FROM students
    )
);
# 79. Find students whose marks are greater than the marks of **all students from Pune**.
SELECT *
FROM students
WHERE marks > ALL (
    SELECT marks
    FROM students
    WHERE city = 'Pune'
);
# 80. Find students whose marks are greater than **at least one student from Mumbai**.
SELECT *
FROM students
WHERE marks > ANY (
    SELECT marks
    FROM students
    WHERE city = 'Mumbai'
);
# ---

# ### 🔵 Level 9 — EXISTS, NOT EXISTS & Correlated Subqueries
#
# Using:
#
# `students(student_id, name, city, course_id, marks, fees)`
    SELECT * FROM students;
#
# `courses(course_id, course_name, department, duration)`
    SELECT * FROM courses;
#
# 81. Display courses for which at least one student is enrolled using `EXISTS`.
SELECT *
FROM courses c
WHERE EXISTS (
    SELECT 1
    FROM students s
    WHERE s.course_id = c.course_id
);
# 82. Display courses for which no student is enrolled using `NOT EXISTS`.
#
# 83. Display students whose course exists in the `courses` table using `EXISTS`.
#
# 84. Find students who have marks greater than the average marks of **their own course**.
#
# 85. Find the highest-scoring student from each course using a correlated subquery.
#
# 86. Find students whose fees are greater than the average fees of their course.
#
# 87. Find courses where at least one student has scored more than 90.
#
# 88. Find courses where **all students** have scored more than 40.
#
# 89. Find students who have the highest marks within their city.
#
# 90. Find students whose marks are higher than the average marks of students from their city.
#
# ---