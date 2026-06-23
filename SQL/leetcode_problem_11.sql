USE leetcode;

-- Create Employee table
CREATE TABLE Employee (
    empId INT PRIMARY KEY,
    name VARCHAR(50),
    supervisor INT,
    salary INT
);

-- Insert data into Employee table
INSERT INTO Employee (empId, name, supervisor, salary)
VALUES
(3, 'Brad', NULL, 4000),
(1, 'John', 3, 1000),
(2, 'Dan', 3, 2000),
(4, 'Thomas', 3, 4000);

-- Create Bonus table
CREATE TABLE Bonus (
    empId INT,
    bonus INT,
    FOREIGN KEY (empId) REFERENCES Employee(empId)
);

-- Insert data into Bonus table
INSERT INTO Bonus (empId, bonus)
VALUES
(2, 500),
(4, 2000);

SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b
ON e.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000;




