USE leetcode;

CREATE TABLE Activity (
    machine_id INT,
    process_id INT,
    activity_type VARCHAR(10),
    timestamp DECIMAL(5,3)
);

INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES
(0, 0, 'start', 0.712),
(0, 0, 'end',   1.520),
(0, 1, 'start', 3.140),
(0, 1, 'end',   4.120),
(1, 0, 'start', 0.550),
(1, 0, 'end',   1.550),
(1, 1, 'start', 0.430),
(1, 1, 'end',   1.420),
(2, 0, 'start', 4.100),
(2, 0, 'end',   4.512),
(2, 1, 'start', 2.500),
(2, 1, 'end',   5.000);

SELECT * FROM Activity;


# SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp),3) AS processing_time
# FROM Activity AS a1
# INNER JOIN Activity AS a2
# ON a1.machine_id = a2.machine_id
# AND a1.process_id = a2.process_id
# AND a1.timestamp < a2.timestamp
# GROUP BY a1.machine_id;

SELECT a.machine_id,
       ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a,
     Activity b
WHERE
    a.machine_id = b.machine_id
AND
    a.process_id = b.process_id
AND
    a.activity_type = 'start'
AND
    b.activity_type = 'end'
GROUP BY machine_id;

