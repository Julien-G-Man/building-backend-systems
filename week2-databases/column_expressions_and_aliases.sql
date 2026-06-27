-- 17. Concatenate name parts, uppercase the result 
SELECT UPPER(name) AS full_name_upper, email FROM students; 
 
 -- 18. Compute how many years until graduation (assuming 4 year degree) 
SELECT name, year, (4 - year) AS years_remaining FROM students; 
 
 -- 19. Show GPA as a percentage out of 100 
SELECT name, ROUND((gpa / 4.0) * 100, 1) AS gpa_percent FROM students; 

 -- 20. Use CASE to label GPA ranges 
SELECT name, gpa, 
       CASE 
           WHEN gpa >= 3.5 THEN 'First Class' 
           WHEN gpa >= 3.0 THEN 'Second Class Upper' 
           WHEN gpa >= 2.5 THEN 'Second Class Lower' 
           ELSE 'Pass' 
       END AS classification 
FROM students;