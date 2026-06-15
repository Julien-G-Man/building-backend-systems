from typing import Optional 
 
class StudentRepository: 
    def __init__(self): 
        self._store: dict[int, dict] = {} 
        self._next_id = 1 
 
    def find_all(self, skip=0, limit=20) -> list[dict]: 
        return list(self._store.values())[skip:skip+limit] 
 
    def find_by_id(self, sid: int) -> Optional[dict]: 
        return self._store.get(sid) 
 
    def find_by_email(self, email: str) -> Optional[dict]: 
        return next((s for s in self._store.values() if s['email']==email), None) 
 
    def save(self, data: dict) -> dict: 
        student = {'id': self._next_id, **data} 
        self._store[self._next_id] = student 
        self._next_id += 1 
        return student 
 
    def delete(self, sid: int) -> bool: 
        if sid not in self._store: return False 
        del self._store[sid] 
        return True 
 
    def count(self) -> int: 
        return len(self._store) 