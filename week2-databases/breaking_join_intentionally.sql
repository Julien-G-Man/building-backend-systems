/*
These exercises produce wrong results deliberately. 
Understanding why they are wrong is more valuable than writing correct queries. 
*/

-- 9. Missing the ON clause — what does this produce? 
SELECT s.name, c.title FROM   students s, courses c; -- Count the rows. Now you understand what a Cartesian product is.  

-- 10. Joining on the wrong column 
SELECT s.name, c.title 
  FROM   students    s 
  JOIN   enrollments e ON e.student_id = s.year  -- wrong column 
  JOIN   courses     c ON c.id = e.course_id; -- What happens? Why? What does the result mean? 
 
 -- 11. Using INNER JOIN where LEFT JOIN is needed -- First add a student with no enrollments 
INSERT INTO students (name, email, year) VALUES ('Yaw Darko', 'yaw@uni.edu', 1); 
 
 -- Now run INNER JOIN and LEFT JOIN and compare the row counts 
SELECT COUNT(*) FROM students s JOIN      enrollments e ON e.student_id = s.id; 

SELECT COUNT(*) FROM students s LEFT JOIN enrollments e ON e.student_id = s.id; 