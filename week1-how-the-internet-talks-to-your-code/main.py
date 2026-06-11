from fastapi import FastAPI 

app = FastAPI() 
 
@app.get('/') 
def root(): return {'message': 'Welcome'} 
 
@app.get('/health') 
def health(): return {'status': 'ok'} 
 
@app.post('/echo') 
def echo(): return {'echo': 'received'}
