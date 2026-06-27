USE leetcode;

-- Create Teacher Table

CREATE TABLE IF NOT EXISTS Teacher (
    teacher_id INT,
    subject_id INT,
    dept_id INT
);

-- Insert Data

INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES
(1, 2, 3),
(1, 2, 4),
(1, 3, 3),
(2, 1, 1),
(2, 2, 1),
(2, 3, 1),
(2, 4, 1);

SELECT * FROM Teacher;

SELECT Teacher.teacher_id, COUNT(DISTINCT Teacher.subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
