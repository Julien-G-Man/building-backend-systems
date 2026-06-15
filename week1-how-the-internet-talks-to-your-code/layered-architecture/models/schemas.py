from pydantic import BaseModel

class StudentIn(BaseModel):
    name: str; email: str; year: int

class CourseIn(BaseModel):
    title: str; code: int; credits: int
    
