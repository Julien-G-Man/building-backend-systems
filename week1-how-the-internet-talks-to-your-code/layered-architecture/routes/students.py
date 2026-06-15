from fastapi import APIRouter, Depends, Query 
from services.student_service import StudentService 
from repositories.student_repo import StudentRepository 
from models.schemas import StudentIn 
 
router = APIRouter() 
 
def get_service() -> StudentService: 
    return StudentService(repo=StudentRepository()) 
 
@router.get('') 
def list_students(page: int = Query(1, ge=1), 
                per_page: int = Query(20, ge=1, le=100), 
                svc: StudentService = Depends(get_service)): 
    return svc.list_students(page, per_page) 
 
@router.post('', status_code=201) 
def create_student(data: StudentIn, svc: StudentService = Depends(get_service)): 
    return svc.create_student(data.model_dump()) 
 
@router.get('/{sid}') 
def get_student(sid: int, svc: StudentService = Depends(get_service)): 
    return svc.get_student(sid) 
 
@router.delete('/{sid}', status_code=204) 
def delete_student(sid: int, svc: StudentService = Depends(get_service)): 
    svc.delete_student(sid)