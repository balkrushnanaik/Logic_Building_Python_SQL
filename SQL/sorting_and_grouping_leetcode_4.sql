USE leetcode;

CREATE TABLE IF NOT EXISTS Courses (
    student CHAR(1),
    class VARCHAR(50)
);

INSERT INTO Courses (student, class) VALUES
('A', 'Math'),
('B', 'English'),
('C', 'Math'),
('D', 'Biology'),
('E', 'Math'),
('F', 'Computer'),
('G', 'Math'),
('H', 'Math'),
('I', 'Math');

SELECT * FROM Courses;

SELECT
    Courses.class
FROM
    Courses
GROUP BY
    class
HAVING
    COUNT(student) >= 5;
