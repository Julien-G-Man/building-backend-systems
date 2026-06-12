"""
A student resource API that uses every method and status code 
correctly. The data is in-memory for now; no database yet.
"""

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
students: dict[int, dict] = {}
next_id = 1


class StudentCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    course: Optional[str] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    course: Optional[str] = None
    
    
@app.get('/students')
def list_students():
    return list(students.values())

@app.post('/students', status_code=201)
def create_student(data: StudentCreate):
    global next_id
    student = {'id': next_id, **data.model_dump()}
    students[next_id] = student; next_id += 1
    return JSONResponse(201, student, headers={'Location': f"/students/{student['id']}"})

@app.get('/students/{sid}')
def get_student(sid: int):
    if sid not in students:
        raise HTTPException(404, 'Not found')
    return students[sid]

@app.patch('/students/{sid}')
def update_student(sid: int, data: StudentUpdate):
    if sid not in students:
        raise HTTPException(404, 'Not found')
    students[sid].update(data.model_dump(exclude_none=True))
    return students[sid]

@app.delete('/students/{sid}', status_code=204)
def delete_student(sid: int):
    if sid not in students:
        raise HTTPException(404, 'Not found')
    del students[sid]
    
