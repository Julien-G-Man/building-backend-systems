"""
Understanding serialization using Pydantic schemas
Week 1 - Day 5
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

class Student(BaseModel):
    name:  str   = Field(min_length=2, max_length=100)
    email: str   = Field(pattern=r'^[\w.+-]+@[\w]+\.[\w.]+$')
    year:  int   = Field(ge=1, le=4)
    gpa:   float = Field(ge=0.0, le=4.0, default=0.0)
    joined: Optional[datetime] = None
    
    @field_validator('name')
    @classmethod
    def name_must_be_alpha(cls, v: str) -> str:
        if not all(c.isalpha() or c.isspace() for c in v):
            raise ValueError('Name must contain only letters and spaces')
        return v.strip().title()
    

# Valid — should work
s1 = Student(name='julien glory', email='jul@gmail.com', year=2)
print(s1.model_dump()) 
print(s1.model_dump_json()) 

# String year - Pydantic coerces '2' to 2 
s2 = Student(name='Test Name', email='t@uni.edu', year='2') 
print(type(s2.year))  # int, not str

# Datetime as string - Pydantic parses ISO 8601 automatically 
s3 = Student(name='Test Name', email='t@uni.edu', year=1, 
             joined='2024-09-01T08:00:00') 
print(type(s3.joined))  # datetime, not str


 
# Now uncomment these one at a time and read every error: 
# Student(name='Test', email='t@uni.edu', year=5)       # year out of range 
# Student(name='Test123', email='t@uni.edu', year=1)    # name with numbers 
# Student(name='T', email='t@uni.edu', year=1)          # name too short