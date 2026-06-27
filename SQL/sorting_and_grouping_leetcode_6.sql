USE leetcode;


CREATE TABLE MyNumbers (
    num INT
);

INSERT INTO MyNumbers (num) VALUES
(8),
(8),
(3),
(3),
(1),
(4),
(5),
(6);

SELECT * FROM MyNumbers;

SELECT MAX(num) AS num
FROM MyNumbers
WHERE MyNumbers.num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num)=1
    );