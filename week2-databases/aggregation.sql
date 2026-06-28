-- 1. Total number of students 
SELECT COUNT(*) AS total_students FROM students; 

-- 2. Average, min, and max GPA across all students 
SELECT ROUND(AVG(gpa),2) AS avg_gpa, MIN(gpa) AS min_gpa, MAX(gpa) AS max_gpa FROM   students; 

-- 3. Number of students per year
SELECT year, COUNT(*) AS student_count 
FROM   students 
GROUP BY year 
ORDER BY year;

-- 4. Average GPA per year 
SELECT year, ROUND(AVG(gpa),2) AS avg_gpa, COUNT(*) AS students 
FROM   students 
GROUP BY year 
ORDER BY year;

-- 5. Number of enrollments per course 
SELECT c.title, COUNT(e.id) AS enrolled 
FROM   courses     c 
LEFT JOIN   enrollments e ON e.course_id = c.id 
GROUP BY c.id, c.title 
ORDER BY enrolled DESC; 

-- 6. Years where average GPA is above 3.2 
SELECT year, ROUND(AVG(gpa),2) AS avg_gpa 
FROM   students 
GROUP BY year 
HAVING  AVG(gpa) > 3.2; 

-- 7. Courses with more than 2 enrolled students 
SELECT c.title, COUNT(e.id) AS enrolled 
FROM   courses     c 
JOIN   enrollments e ON e.course_id = c.id 
GROUP BY c.id, c.title 
HAVING  COUNT(e.id) > 2;

-- 8. Students enrolled in more than 2 courses 
SELECT s.name, COUNT(e.id) AS course_count 
FROM   students    s 
JOIN   enrollments e ON e.student_id = s.id 
GROUP BY s.id, s.name 
HAVING  COUNT(e.id) > 2 
ORDER BY course_count DESC;

-- 9. Year 2 students only — average GPA per year using WHERE + GROUP BY 
SELECT year, ROUND(AVG(gpa),2) 
FROM   students 
WHERE  year = 2 
GROUP BY year;

-- 10. The most enrolled course 
SELECT c.title, COUNT(e.id) AS enrolled 
FROM   courses     c 
JOIN   enrollments e ON e.course_id = c.id 
GROUP BY c.id, c.title 
ORDER BY enrolled DESC LIMIT 1; 

-- 11. The student enrolled in the most courses 
SELECT s.name, COUNT(e.id) AS course_count 
FROM   students    s 
JOIN   enrollments e ON e.student_id = s.id 
GROUP BY s.id, s.name 
ORDER BY course_count DESC LIMIT 1; 


-- 12. Average number of courses per student 
SELECT ROUND(AVG(course_count), 2) AS avg_courses_per_student 
FROM  ( 
      SELECT student_id, COUNT(*) AS course_count 
      FROM   enrollments 
      GROUP BY student_id 
  ) AS per_student; 


-- 13. Courses where enrollment is at 75% capacity or above 
SELECT c.title, c.capacity, COUNT(e.id) AS enrolled, 
       ROUND(COUNT(e.id)::NUMERIC / c.capacity * 100, 1) AS pct_full 
FROM   courses     c 
LEFT JOIN   enrollments e ON e.course_id = c.id 
GROUP BY c.id, c.title, c.capacity 
HAVING  COUNT(e.id)::NUMERIC / c.capacity >= 0.75 
ORDER BY pct_full DESC;

