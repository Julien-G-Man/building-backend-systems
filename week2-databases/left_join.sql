-- 5. All students, including those with no enrollments 
SELECT s.name, e.course_id 
  FROM   students    s 
  LEFT JOIN   enrollments e ON e.student_id = s.id 
  ORDER BY s.name; 
 
 -- 6. ONLY students with no enrollments 
SELECT s.name 
  FROM   students    s 
  LEFT JOIN   enrollments e ON e.student_id = s.id 
  WHERE  e.id IS NULL; 

 -- 7. All courses including those with no enrolled students 
SELECT c.title, COUNT(e.id) AS enrolled_count 
  FROM   courses     c 
  LEFT JOIN   enrollments e ON e.course_id = c.id 
  GROUP BY c.id, c.title 
  ORDER BY enrolled_count DESC; 
 
 -- 8. Courses under capacity (enrolled < capacity) 
SELECT c.title, c.capacity, COUNT(e.id) AS enrolled 
  FROM   courses     c 
  LEFT JOIN   enrollments e ON e.course_id = c.id 
  GROUP BY c.id, c.title, c.capacity 
  HAVING  COUNT(e.id) < c.capacity 
  ORDER BY (c.capacity - COUNT(e.id)) DESC; 