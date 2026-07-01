USE leetcode;

CREATE TABLE IF NOT EXISTS Activities (
    player_id INT,
    device_id INT,
    event_date DATE,
    games_played INT
);

INSERT INTO Activities (player_id, device_id, event_date, games_played) VALUES
(1, 2, '2016-03-01', 5),
(1, 2, '2016-03-02', 6),
(2, 3, '2017-06-25', 1),
(3, 1, '2016-03-02', 0),
(3, 4, '2018-07-03', 5);

SELECT * FROM Activities;

# SELECT ROUND(SUM(DATEDIFF(a1.event_date,a2.event_date) = 1) / COUNT(DISTINCT a1.player_id),2) AS fraction
# FROM Activities AS a1
# JOIN Activities AS a2
# ON a1.player_id = a2.player_id;

SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activities),2) AS fraction
FROM Activities
WHERE (player_id,DATE_SUB(event_date,INTERVAL 1 DAY)) IN (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activities
    GROUP BY player_id
    );






