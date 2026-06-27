-- 13. Students in years 2 or 3 using IN 
SELECT name, year FROM students WHERE year IN (2, 3); 
 
 -- 14. Students in years 2 or 3 using BETWEEN 
SELECT name, year FROM students WHERE year BETWEEN 2 AND 3; 
 
 -- 15. Add a nullable column to students and test IS NULL 
ALTER TABLE students ADD COLUMN phone TEXT; 
UPDATE students SET phone = '+233501234567' WHERE id = 1; 
 
SELECT name FROM students WHERE phone IS NULL;

SELECT name FROM students WHERE phone IS NOT NULL; 
 
 -- 16. Why NULL is dangerous — this returns 0 rows, not what you expect 

SELECT name FROM students WHERE phone = NULL;  -- WRONG: use IS NULL