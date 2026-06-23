USE leetcode;

CREATE TABLE IF NOT EXISTS Employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department CHAR(1),
    managerId INT
);

INSERT INTO Employees (id, name, department, managerId)
VALUES
(101, 'John',  'A', NULL),
(102, 'Dan',   'A', 101),
(103, 'James', 'A', 101),
(104, 'Amy',   'A', 101),
(105, 'Anne',  'A', 101),
(106, 'Ron',   'B', 101);

SELECT * FROM Employees;

SELECT e1.name
FROM Employees AS e1
INNER JOIN Employees AS e2
ON e1.id = e2.managerId
GROUP BY e2.managerId
HAVING COUNT(e2.managerId) >= 5;


