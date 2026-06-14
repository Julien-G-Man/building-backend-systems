"""
Customise validation error responses
"""

from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse 
from fastapi.exceptions import RequestValidationError 
from pydantic import BaseModel, Field 
 
app = FastAPI()


@app.exception_handler(RequestValidationError) 
async def validation_handler(request: Request, exc: RequestValidationError): 
    errors = [{'field': ' -> '.join(str(p) for p in e['loc']), 
               'message': e['msg'], 'type': e['type']} for e in exc.errors()] 
    return JSONResponse(status_code=422, content={'errors': errors}) 


class StudentIn(BaseModel): 
    name:  str = Field(min_length=2) 
    email: str 
    year:  int = Field(ge=1, le=4) 
 
 
@app.post('/students') 
def create(data: StudentIn): 
    return data.model_dump()