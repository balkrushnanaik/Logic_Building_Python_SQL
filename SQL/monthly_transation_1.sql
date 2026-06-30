USE leetcode;

CREATE TABLE IF NOT EXISTS Transaction (
    id INT PRIMARY KEY,
    country VARCHAR(10),
    state VARCHAR(20),
    amount INT,
    trans_date DATE
);

INSERT INTO Transaction (id, country, state, amount, trans_date)
VALUES
(121, 'US', 'approved', 1000, '2018-12-18'),
(122, 'US', 'declined', 2000, '2018-12-19'),
(123, 'US', 'approved', 2000, '2019-01-01'),
(124, 'DE', 'approved', 2000, '2019-01-07');

SELECT * FROM Transaction;

SELECT DATE_FORMAT(Transaction.trans_date, '%Y-%m') AS "month",
       country,
       COUNT(trans_date) AS "trans_count",
       SUM(state='approved') AS "approved_count",
       SUM(amount) AS "trans_total_amount",
       SUM(CASE WHEN state='approved' THEN amount ELSE 0 END) AS "approved_total_amount"
FROM Transaction
GROUP BY DATE_FORMAT(Transaction.trans_date, '%Y-%m'),country
ORDER BY month;