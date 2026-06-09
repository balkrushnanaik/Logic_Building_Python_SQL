/*
### 3. Product Inventory

Create queries to:
11. Display products with stock less than 20.
12. Find the total value of inventory (Price × Quantity).
13. Display products sorted by price in descending order.
14. Find the most expensive product.
15. Increase the price of all products by
10%.
 */
 USE logic_building;
SELECT * FROM product;

-- 11. Display products with stock less than 20.
SELECT * FROM product
WHERE quantity < 20;

-- 12. Find the total value of inventory (Price × Quantity).
SELECT SUM(price * quantity) AS total_inventory_value
FROM product;

-- 13. Display products sorted by price in descending order.
SELECT * FROM product
ORDER BY price DESC;

-- 14. Find the most expensive product.
SELECT * FROM product
ORDER BY price DESC
LIMIT 1;

-- 15. Increase the price of all products by 10%.
UPDATE product
SET price = price + (price * 0.10);

SELECT * FROM product;


