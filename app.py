from fastapi import FastAPI
from src.routes.user import user

app = FastAPI() 

@app.get("/") 
def root(): 
    return {"message": "Hello World"} 


app.include_router(user, prefix="/api")