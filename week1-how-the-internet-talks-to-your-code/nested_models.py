from pydantic import BaseModel, Field
from enum import Enum

class Department(str, Enum):
    CS = 'computer_science'
    COE = 'computer_engineering'
    BUS = 'business'
    
class Instructor(BaseModel):
    name:       str 
    email:      str 
    department: Department
    
class CourseIn(BaseModel):
    title:      str         = Field(min_length=3) 
    code:       str         = Field(pattern=r'^[A-Z]{2,4}\d{3}$') 
    credits:    int         = Field(ge=1, le=6)
    instructor: Instructor
    tags:       list[str]   = []
    

course = CourseIn(**{
    'title': 'Databases', 
    'code': 'CS260', 
    'credits': 3,
    'instructor': {'name': 'Dr. Mensah', 
                   'email': 'drm@gmail.com',
                   'department': 'computer_science'},
    'tags': ['sql', 'postgresql'],
})


print(course.model_dump())              # dictionary
print(course.model_dump_json(indent=2)) # JSON string