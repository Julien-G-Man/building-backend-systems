-- 1. Return all columns from students 
SELECT * FROM students; 

-- 2. Return only name and email 
SELECT name, email FROM students; 

-- 3. Return all students in year 2 
SELECT name, year FROM students WHERE year = 2; 

-- 4. Return students with a GPA above 3.3 
SELECT name, gpa FROM students WHERE gpa > 3.3; 

-- 5. Return students whose name starts with 'K' 
SELECT name FROM students WHERE name LIKE 'K%'; 

-- 6. Return students in year 2 OR with GPA above 3.5 
SELECT name, year, gpa FROM students WHERE year = 2 OR gpa > 3.5; 

-- 7. Return students in year 2 AND with GPA above 3.3 
SELECT name, year, gpa FROM students WHERE year = 2 AND gpa > 3.3;