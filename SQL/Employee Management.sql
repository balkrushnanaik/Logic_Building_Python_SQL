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
CREATE TABLE emp_department AS
SELECT e.emp_id, e.emp_name, e.salary, e.city, e.hire_date, e.dept_id, d.dept_name
FROM employee as e
INNER JOIN department as d
ON e.dept_id = d.dept_id
WHERE dept_name = 'IT';

-- DROP TABLE Emp_Department;

-- 3. Display the top 5 highest-paid employees.

SELECT * FROM employee
ORDER BY salary DESC LIMIT 5;


-- 4. Count the number of employees in each department.
SELECT * FROM emp_department;
SELECT dept_name, COUNT(*) AS emp_in_each_dept
FROM Emp_Department
GROUP BY dept_name;




