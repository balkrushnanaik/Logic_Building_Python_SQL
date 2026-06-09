USE logic_building;

SELECT * FROM student;

/*
 ### 2. Student Database

Create queries to:
6. Display students scoring more than 80 marks.
7. Find the average marks of all students.
8. Display the highest and lowest marks.
9. Count students from each city.
10. Find students whose names start with 'A'.

---
 */

 -- 8. Display the highest and lowest marks.
SELECT * FROM student
ORDER BY marks DESC
LIMIT 3;

SELECT *FROM student
ORDER BY marks ASC
LIMIT 3;

-- 9. Count students from each city.
SELECT city,COUNT(*) AS Students_from_each_city
FROM student
GROUP BY city;

-- 10. Find students whose names start with 'A'.
SELECT *
FROM student
WHERE student_name LIKE 'A%';
