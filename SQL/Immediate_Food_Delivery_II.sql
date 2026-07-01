USE leetcode;

CREATE TABLE Delivery (
    delivery_id INT,
    customer_id INT,
    order_date DATE,
    customer_pref_delivery_date DATE
);

INSERT INTO Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES
(1, 1, '2019-08-01', '2019-08-02'),
(2, 2, '2019-08-02', '2019-08-02'),
(3, 1, '2019-08-11', '2019-08-12'),
(4, 3, '2019-08-24', '2019-08-24'),
(5, 3, '2019-08-21', '2019-08-22'),
(6, 2, '2019-08-11', '2019-08-13'),
(7, 4, '2019-08-09', '2019-08-09');


SELECT ROUND(SUM(IF(order_date = customer_pref_delivery_date,1,0))*100/COUNT(DISTINCT customer_id),2) AS immediate_percent
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
    );








