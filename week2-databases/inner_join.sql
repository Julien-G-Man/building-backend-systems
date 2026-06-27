-- 1. Each student's name and the courses they are enrolled in 
SELECT s.name AS student, c.title AS course 
  FROM   students    s 
  JOIN   enrollments e ON e.student_id = s.id 
  JOIN   courses     c ON c.id = e.course_id 
  ORDER BY s.name, c.title; 
 
 -- 2. Only students enrolled in 'CS301' 
SELECT s.name, s.email 
  FROM   students    s 
  JOIN   enrollments e ON e.student_id = s.id 
  JOIN   courses     c ON c.id = e.course_id 
  WHERE  c.code = 'CS301'; 
 
 -- 3. All courses with the name and email of each enrolled student 
SELECT c.title, c.code, s.name, s.email 
  FROM   courses     c 
  JOIN   enrollments e ON e.course_id = c.id 
  JOIN   students    s ON s.id = e.student_id 
  ORDER BY c.title, s.name; 
 
 -- 4. Students enrolled in BOTH CS301 and CS302 
SELECT s.name 
  FROM   students    s 
  JOIN   enrollments e1 ON e1.student_id = s.id 
  JOIN   courses     c1 ON c1.id = e1.course_id AND c1.code = 'CS301' 
  JOIN   enrollments e2 ON e2.student_id = s.id JOIN   courses     c2 ON c2.id = e2.course_id AND c2.code = 'CS302';