/*
### 1. Employee Management

Create queries to:

1. Display all employees whose salary is greater than ₹50,000.
2. Find employees working in the "IT" department.
3. Display the top 5 highest-paid employees.
4. Count the number of employees in each department.
5. Find departments having more than 10 employees.


*/
SELECT * FROM employee;
SELECT * FROM department;

-- 1. Display all employees whose salary is greater than ₹50,000.
SELECT * FROM employee
WHERE salary > 50000;

-- 2. Find employees working in the "IT" department.
SELECT *
FROM employee as e
INNER JOIN department as d
ON e.dept_id = d.dept_id
WHERE dept_name = 'IT';

-- 3. Display the top 5 highest-paid employees.

SELECT * FROM employee
ORDER BY salary DESC LIMIT 5;








