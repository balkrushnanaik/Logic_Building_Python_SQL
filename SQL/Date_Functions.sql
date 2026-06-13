USE joins_and_functions;

#  Date Functions

# NOW()
SELECT NOW() AS Current_DateTime;

# CURDATE()
SELECT CURDATE() AS CurrentDate;

# CURTIME()
SELECT CURTIME() as CurrentTime;

CREATE TABLE P_Orders (
    Order_ID INT PRIMARY KEY,
    Customer_Name VARCHAR(50),
    Product_Name VARCHAR(50),
    Order_Date DATE,
    Delivery_Date DATE,
    Amount DECIMAL(10,2)
);

INSERT INTO P_Orders VALUES
(101, 'Amit', 'Laptop', '2025-01-15', '2025-01-20', 55000),
(102, 'Priya', 'Mobile', '2025-02-10', '2025-02-14', 30000),
(103, 'Rahul', 'Keyboard', '2025-03-05', '2025-03-08', 1500),
(104, 'Sneha', 'Mouse', '2025-04-12', '2025-04-15', 800),
(105, 'Karan', 'Monitor', '2025-05-20', '2025-05-25', 12000),
(106, 'Neha', 'Tablet', '2025-06-08', '2025-06-12', 25000),
(107, 'Rohan', 'Printer', '2025-07-18', '2025-07-22', 7000),
(108, 'Pooja', 'SSD', '2025-08-25', '2025-08-28', 5000),
(109, 'Vikas', 'Speaker', '2025-09-10', '2025-09-14', 3500),
(110, 'Anjali', 'Camera', '2025-10-05', '2025-10-10', 45000),
(111, 'Arjun', 'Laptop Bag', '2025-11-12', '2025-11-16', 2000),
(112, 'Meera', 'Webcam', '2025-12-20', '2025-12-24', 2500),
(113, 'Sanjay', 'Router', '2026-01-08', '2026-01-12', 3000),
(114, 'Divya', 'Smart Watch', '2026-02-14', '2026-02-18', 10000),
(115, 'Nitin', 'Headphones', '2026-03-25', '2026-03-30', 4000);

SELECT * FROM P_Orders;

# Date()
SELECT P_Orders.Order_ID,
       P_Orders.Customer_Name,
       DATE(P_Orders.Order_Date) AS Only_Order_Date
FROM P_Orders;

# Extract()
SELECT P_Orders.Order_ID,
       P_Orders.Customer_Name,
       EXTRACT(YEAR FROM P_Orders.Order_Date) AS Order_Year
FROM P_Orders;

# Date_Add()
SELECT
    P_Orders.Order_ID,
    P_Orders.Customer_Name,
    DATE_ADD(P_Orders.Order_Date, INTERVAL 7 DAY) AS After_Extend
FROM P_Orders;

# Date_Sub()
SELECT
    P_Orders.Order_ID,
    P_Orders.Customer_Name,
    DATE_SUB(P_Orders.Order_Date, INTERVAL 7 DAY) AS After_Reduce
FROM P_Orders;

# DATEDIFF()
SELECT
    P_Orders.Order_ID,
    P_Orders.Customer_Name,
    P_Orders.Order_Date,
    DATEDIFF('2025-07-11', Order_Date) AS Days_Until_Jully11
FROM P_Orders;


