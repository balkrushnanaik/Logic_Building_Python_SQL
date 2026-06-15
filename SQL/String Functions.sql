USE joins_and_functions;

CREATE TABLE IF NOT EXISTS Employees (
    Emp_ID INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Email VARCHAR(100),
    City VARCHAR(50)
);

INSERT INTO Employees VALUES
(101, 'Rahul', 'Sharma', 'rahul.sharma@gmail.com', 'Pune'),
(102, 'Priya', 'Patil', 'priya.patil@yahoo.com', 'Mumbai'),
(103, 'Amit', 'Joshi', 'amit.joshi@hotmail.com', 'Nashik'),
(104, 'Sneha', 'Kulkarni', 'sneha.k@gmail.com', 'Nagpur'),
(105, 'Rohan', 'Deshmukh', 'rohan.desh@gmail.com', 'Thane'),
(106, 'Neha', 'Jadhav', 'neha.j@gmail.com', 'Aurangabad'),
(107, 'Karan', 'Pawar', 'karan.p@gmail.com', 'Kolhapur'),
(108, 'Pooja', 'More', 'pooja.more@yahoo.com', 'Satara'),
(109, 'Vikas', 'Shinde', 'vikas.s@gmail.com', 'Solapur'),
(110, 'Anjali', 'Patel', 'anjali.p@gmail.com', 'Pune');

SELECT * FROM Employees;