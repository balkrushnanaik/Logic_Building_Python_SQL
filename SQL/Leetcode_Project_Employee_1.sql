USE leetcode;
CREATE TABLE Project1 (
    project_id INT,
    employee_id INT,
    PRIMARY KEY (project_id, employee_id)
);

INSERT INTO Project1 (project_id, employee_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 4);

select * from Project1;

CREATE TABLE Employee1 (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    experience_years INT
);

INSERT INTO Employee1 (employee_id, name, experience_years) VALUES
(1, 'Khaled', 3),
(2, 'Ali', 2),
(3, 'John', 1),
(4, 'Doe', 2);

select * from Employee1;
-- Use the ROUND() function:
SELECT p.project_id, ROUND(AVG(experience_years),2) AS average_years
FROM Project1 AS p
JOIN Employee1 as e
ON p.employee_id = e.employee_id
GROUP BY p.project_id;



