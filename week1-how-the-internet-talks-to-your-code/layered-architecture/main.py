from fastapi import FastAPI
from routes.students import router as student_router


app = FastAPI(title="Student Management API", version='1.0.0')

app.include_router(student_router, prefix='/v1/students', tags=['Students'])

app.get("/")
def root():
    return {"message": "API is live"}