
CREATE TABLE students ( 
    id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    name        TEXT        NOT NULL, 
    email       TEXT        NOT NULL UNIQUE, 
    year        INTEGER     NOT NULL CHECK (year BETWEEN 1 AND 4), 
    gpa         NUMERIC(3,2) NOT NULL DEFAULT 0.00, 
    enrolled_at TIMESTAMPTZ NOT NULL DEFAULT NOW() 
); 

 
CREATE TABLE courses ( 
    id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    title       TEXT        NOT NULL, 
    code        VARCHAR(10)  NOT NULL UNIQUE, 
    credits     INTEGER     NOT NULL CHECK (credits BETWEEN 1 AND 6), 
    capacity    INTEGER     NOT NULL DEFAULT 30 
); 

 -- Enrollments: the junction table for the many-to-many relationship 
CREATE TABLE enrollments ( 
    id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    student_id  INTEGER     NOT NULL REFERENCES students(id) ON DELETE CASCADE, 
    course_id   INTEGER     NOT NULL REFERENCES courses(id)  ON DELETE CASCADE, 
    enrolled_at TIMESTAMPTZ NOT NULL DEFAULT NOW(), 
    UNIQUE (student_id, course_id)  -- a student cannot enroll twice 
); 

