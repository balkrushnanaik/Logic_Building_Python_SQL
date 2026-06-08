/*
### 2. Student Database

Create queries to:
6. Display students scoring more than 80 marks.
7. Find the average marks of all students.
8. Display the highest and lowest marks.
9. Count students from each city.
10. Find students whose names start with 'A'.

*/

SELECT * FROM student;
-- 6. Display students scoring more than 80 marks.
SELECT * FROM student
WHERE marks > 80;

-- 7. Find the average marks of all students.
SELECT AVG(marks) AS Average_Marks
FROM student;

