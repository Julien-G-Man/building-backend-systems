from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Student Management API", version='1.0.0')

students_db:    dict[int, dict] = {} 
courses_db:     dict[int, dict] = {} 
enrollments_db: list[dict]      = [] 
counters = {'students': 1, 'courses': 1} 

class StudentIn(BaseModel):
    name: str; email: str; year: int

class CourseIn(BaseModel):
    title: str; code: int; credits: int
    

app.get('v1/students')
def list_students(page: int = Query(1, ge=1), 
                per_page: int = Query(20, ge=1, le=100)):
    all_s = list(students_db.values())
    start = (page - 1) * per_page
    return {'data': all_s[start:start+per_page], 'page': page, 
            'total': len(all_s), 'has_more': start+per_page < len(all_s)}
    
    
app.post('v1/students', status_code=201)
def create_student(data: StudentIn):
    sid = counters['students']
    students_db[sid] = {'id': sid, **data.model_dump()}
    counters['students'] += 1
    return students_db[sid]


@app.get('/v1/students/{sid}') 
def get_student(sid: int): 
    if sid not in students_db: 
        raise HTTPException(404, 'Student not found') 
    return students_db[sid] 

 
@app.get('/v1/students/{sid}/courses') 
def get_student_courses(sid: int): 
    if sid not in students_db: 
        raise HTTPException(404, 'Student not found')
    cids = [e['course_id'] for e in enrollments_db if e['student_id'] == sid] 
    return  [courses_db[c] for c in cids if c in courses_db]

 
@app.post('/v1/students/{sid}/courses/{cid}', 
status_code=201) 
def enroll(sid: int, cid: int): 
    if sid not in students_db: 
        raise HTTPException(404, 'Student not found') 
    if cid not in courses_db:  
        raise HTTPException(404, 'Course not found') 
    already = any(e['student_id']==sid and e['course_id']==cid for e in enrollments_db) 
    if already: 
        raise HTTPException(409, 'Already enrolled') 
    enrollments_db.append({'student_id': sid, 'course_id': cid}) 
    return {'student_id': sid, 'course_id': cid}


app.delete('v1/students/{sid}', status_code=204)
def delete_student(sid: int):
    if sid not in students_db:
        raise HTTPException(404, 'Student does not exist')
    for e in enrollments_db:
        if e['student_id'] == sid:
            enrollments_db.remove(e)
    del students_db['student_id']