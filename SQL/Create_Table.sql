USE logic_building;
# Ctrl + Enter = Execute Query
# Ctrl + Shift + Enter = Execute all queries in the file
#
# Ctrl + / = Comment
/*
Ctrl + shift + / = Block Comment
*/

CREATE TABLE IF NOT EXISTS students(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT CHECK ( age >= 0 and age <=100 ),
    college_name VARCHAR(100),
    branch VARCHAR(100),
    percentage DECIMAL(5,2),
    dob date
);

SELECT * FROM students;