-- 8. All students sorted by GPA, highest first 
SELECT name, gpa FROM students ORDER BY gpa DESC; 
 
 -- 9. The top 3 students by GPA 
SELECT name, gpa FROM students ORDER BY gpa DESC LIMIT 3; 
 
 -- 10. Sort by year ASC, then GPA DESC within each year 
SELECT name, year, gpa FROM students ORDER BY year ASC, gpa DESC; 
 
 -- 11. The most recently enrolled student 
SELECT name, enrolled_at FROM students ORDER BY enrolled_at DESC LIMIT 1; 
 
 -- 12. Simulate page 2 of results (5 per page) 
SELECT name FROM students ORDER BY id LIMIT 5 OFFSET 5;