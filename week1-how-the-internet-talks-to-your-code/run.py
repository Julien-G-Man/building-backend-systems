import uvicorn

# file = "main" 
# file = "http_methods" 
file = "student_management" 

if __name__ == "__main__":
    uvicorn.run(
        f"{file}:app", 
        host="127.0.0.1", 
        port=8000,
        reload=True
    )