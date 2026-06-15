from fastapi import HTTPException, Query
from repositories.student_repo import StudentRepository 


class StudentService: 
    def __init__(self, repo: StudentRepository): 
        self.repo = repo 
 
    def list_students(self, page: int, per_page: int) -> dict: 
        skip  = (page - 1) * per_page 
        items = self.repo.find_all(skip=skip, limit=per_page) 
        return {'data': items, 'page': page, 'total': self.repo.count()} 
 
    def get_student(self, sid: int) -> dict: 
        s = self.repo.find_by_id(sid) 
        if not s: raise HTTPException(404, 'Student not found') 
        return s 
 
    def create_student(self, data: dict) -> dict: 
        # Business rule: email must be unique 
        if self.repo.find_by_email(data['email']): 
            raise HTTPException(409, 'Email already registered') 
        return self.repo.save(data) 
 
    def delete_student(self, sid: int) -> None: 
        if not self.repo.delete(sid): 
            raise HTTPException(404, 'Student not found')