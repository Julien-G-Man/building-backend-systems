-- Accidental Cartesian product — do NOT run this on large tables 
SELECT * FROM students, courses;  -- returns 5 × 4 = 20 rows -- The correct version with an explicit JOIN condition 

SELECT s.name, c.title 
    FROM   students s 
    JOIN   enrollments e ON e.student_id = s.id 
    JOIN   courses     c ON c.id          = e.course_id; 