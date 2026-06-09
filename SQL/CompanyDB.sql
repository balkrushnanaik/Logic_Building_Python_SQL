CREATE DATABASE Logic_Building;

USE Logic_Building;

-- Department Table
CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

-- Employee Table
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    salary DECIMAL(10,2),
    city VARCHAR(50),
    hire_date DATE,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Student Table
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    marks INT,
    city VARCHAR(50),
    dob DATE
);

-- Customer Table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50)
);

-- Product Table
CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    quantity INT
);

-- Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- Order Details Table
CREATE TABLE Order_Details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

----------------------------------------------------
-- INSERT DATA
----------------------------------------------------

-- Department
INSERT INTO Department VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Marketing');

-- Employee
INSERT INTO Employee VALUES
(101, 'Amit', 60000, 'Pune', '2022-01-15', 1),
(102, 'Priya', 55000, 'Mumbai', '2021-05-10', 2),
(103, 'Rahul', 75000, 'Nashik', '2020-08-20', 1),
(104, 'Sneha', 45000, 'Pune', '2023-03-12', 3),
(105, 'Karan', 90000, 'Nagpur', '2019-11-25', 1),
(106, 'Neha', 65000, 'Mumbai', '2022-09-18', 4),
(107, 'Rohan', 50000, 'Pune', '2021-12-01', 2),
(108, 'Pooja', 70000, 'Aurangabad', '2020-06-05', 3);

-- Student
INSERT INTO Student VALUES
(1, 'Anjali', 85, 'Pune', '2004-05-10'),
(2, 'Rohit', 72, 'Mumbai', '2005-08-12'),
(3, 'Akash', 91, 'Nashik', '2004-11-15'),
(4, 'Meera', 68, 'Pune', '2005-01-22'),
(5, 'Aditi', 88, 'Nagpur', '2004-07-19'),
(6, 'Sagar', 77, 'Mumbai', '2005-09-30');

-- Customer
INSERT INTO Customer VALUES
(1, 'Raj', 'Pune'),
(2, 'Simran', 'Mumbai'),
(3, 'Arjun', 'Nashik'),
(4, 'Kavya', 'Nagpur');

-- Product
INSERT INTO Product VALUES
(1, 'Laptop', 55000, 10),
(2, 'Mouse', 500, 100),
(3, 'Keyboard', 1200, 50),
(4, 'Monitor', 15000, 20),
(5, 'Printer', 8000, 15);

-- Orders
INSERT INTO Orders VALUES
(1001, 1, '2025-01-10', 56000),
(1002, 2, '2025-01-15', 1700),
(1003, 1, '2025-02-05', 15000),
(1004, 3, '2025-02-12', 8000),
(1005, 4, '2025-03-01', 55000);

-- Order Details
INSERT INTO Order_Details VALUES
(1, 1001, 1, 1),
(2, 1001, 2, 2),
(3, 1002, 3, 1),
(4, 1002, 2, 1),
(5, 1003, 4, 1),
(6, 1004, 5, 1),
(7, 1005, 1, 1);

----------------------------------------------------
-- VERIFY DATA
----------------------------------------------------

SELECT * FROM Department;
SELECT * FROM Employee;
SELECT * FROM Student;
SELECT * FROM Customer;
SELECT * FROM Product;
SELECT * FROM Orders;
SELECT * FROM Order_Details;