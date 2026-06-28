USE leetcode;

CREATE TABLE IF NOT EXISTS Customer (
    customer_id INT,
    product_key INT
);

INSERT INTO Customer (customer_id, product_key) VALUES
(1, 5),
(2, 6),
(3, 5),
(3, 6),
(1, 6);

CREATE TABLE IF NOT EXISTS Products(
    product_key INT
);
INSERT INTO Products VALUES
(5),
(6);


SELECT * FROM Customer;

SELECT Customer.customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(product_key)
    FROM Products
    );

