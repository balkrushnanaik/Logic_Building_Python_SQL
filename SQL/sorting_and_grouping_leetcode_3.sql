USE leetcode;

CREATE TABLE Sales (
    sale_id INT,
    product_id INT,
    year INT,
    quantity INT,
    price INT
);

INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2008, 10, 5000),
(2, 100, 2009, 12, 5000),
(7, 200, 2011, 15, 9000);

SELECT * FROM Sales;

SELECT Sales.product_id,year AS first_year, Sales.quantity, Sales.price
FROM Sales
WHERE (product_id,year) IN (
    SELECT product_id, MIN(year) AS f_year
    FROM Sales
    GROUP BY product_id
    );


