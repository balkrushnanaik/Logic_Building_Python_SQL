CREATE DATABASE joins_and_functions;
USE joins_and_functions;

CREATE TABLE Customers (
    Customer_ID INT PRIMARY KEY,
    Customer_Name VARCHAR(50),
    City VARCHAR(30),
    Email VARCHAR(50)
);

INSERT INTO Customers VALUES
(101, 'Amit Sharma', 'Pune', 'amit@gmail.com'),
(102, 'Priya Patel', 'Mumbai', 'priya@gmail.com'),
(103, 'Rahul Verma', 'Delhi', 'rahul@gmail.com'),
(104, 'Sneha Joshi', 'Nagpur', 'sneha@gmail.com'),
(105, 'Karan Mehta', 'Pune', 'karan@gmail.com'),
(106, 'Neha Singh', 'Jaipur', 'neha@gmail.com'),
(107, 'Rohan Gupta', 'Surat', 'rohan@gmail.com'),
(108, 'Pooja Desai', 'Ahmedabad', 'pooja@gmail.com'),
(109, 'Vikas Yadav', 'Lucknow', 'vikas@gmail.com'),
(110, 'Anjali Kulkarni', 'Nashik', 'anjali@gmail.com'),
(111, 'Arjun Patil', 'Kolhapur', 'arjun@gmail.com'),
(112, 'Meera Nair', 'Kochi', 'meera@gmail.com'),
(113, 'Sanjay Kumar', 'Patna', 'sanjay@gmail.com'),
(114, 'Divya Rao', 'Hyderabad', 'divya@gmail.com'),
(115, 'Nitin Shah', 'Vadodara', 'nitin@gmail.com');

CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Customer_ID INT,
    Product_Name VARCHAR(50),
    Quantity INT,
    Amount DECIMAL(10,2)
);

INSERT INTO Orders VALUES
(1001, 101, 'Laptop', 1, 55000),
(1002, 102, 'Mobile', 2, 40000),
(1003, 103, 'Headphones', 3, 6000),
(1004, 105, 'Keyboard', 2, 3000),
(1005, 106, 'Monitor', 1, 12000),
(1006, 108, 'Mouse', 5, 2500),
(1007, 109, 'Printer', 1, 8000),
(1008, 110, 'Tablet', 2, 30000),
(1009, 111, 'Camera', 1, 45000),
(1010, 113, 'Speaker', 2, 7000),
(1011, 115, 'SSD', 2, 10000),
(1012, 120, 'Laptop Bag', 3, 4500),
(1013, 121, 'Webcam', 2, 5000),
(1014, 122, 'Router', 1, 2500),
(1015, 123, 'Smart Watch', 2, 12000);

SELECT * FROM Customers;
SELECT * FROM orders;

#  Inner Join
SELECT *
FROM Customers AS c
INNER Join orders as o
ON c.Customer_ID = o.Customer_ID;

# Left Join
SELECT *
FROM Customers AS c
LEFT JOIN orders AS o
ON c.Customer_ID = o.Customer_ID;

#  Right Join
SELECT *
FROM Customers AS c
RIGHT JOIN orders as o
ON c.Customer_ID = o.Customer_ID;

# Full Join
# SELECT *
# FROM Customers AS c
# FULL JOIN

#  Cross Join:
CREATE TABLE Students (
    Student_ID INT,
    Student_Name VARCHAR(50)
);

INSERT INTO Students VALUES
(1, 'Amit'),
(2, 'Priya'),
(3, 'Rahul');

CREATE TABLE Courses (
    Course_ID INT,
    Course_Name VARCHAR(50)
);

INSERT INTO Courses VALUES
(101, 'SQL'),
(102, 'Python'),
(103, 'Power BI');

SELECT * FROM Students;
SELECT * FROM Courses;

SELECT * FROM Students
CROSS JOIN Courses;
