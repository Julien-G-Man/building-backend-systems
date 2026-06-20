INSERT INTO students (name, email, year, gpa) VALUES 
    ('Amara Diallo',    'amara@uni.edu',   2, 3.45),
    ('Kwame Mensah',    'kwame@uni.edu',   3, 3.10), 
    ('Fatima Al-Hassan','fatima@uni.edu',  1, 3.80), 
    ('Kofi Acheampong', 'kofi@uni.edu',    4, 2.95), 
    ('Ngozi Okonkwo',   'ngozi@uni.edu',   2, 3.60); 
 
INSERT INTO courses (title, code, credits, capacity) VALUES 
    ('Introduction to Databases',    'CS301', 3, 40), 
    ('Software Engineering',         'CS302', 3, 35), 
    ('Linear Algebra',               'MA201', 3, 50), 
    ('Computer Networks',            'CS401', 3, 30); 
 
INSERT INTO enrollments (student_id, course_id) VALUES 
    (1,1),(1,2),(1,3), 
    (2,1),(2,4), 
    (3,1),(3,2),(3,3),(3,4), 
    (4,2),(4,4), 
    (5,1),(5,3); 