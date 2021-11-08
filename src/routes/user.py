from fastapi import APIRouter
from src.config.database import conn
from ..models.user import users
from ..schema.user import User
from ..libs.libs import encrypt_password
from typing import List

user = APIRouter() 



@user.get("/users", response_model=List[User])
async def get_users():
    userList =  conn.execute(users.select()).fetchall()
    return userList
    
@user.post("/users", response_model=User)
async def create_user(user: User):
    try:
      password_enc = encrypt_password(user.password)
      new_user = {"username": user.username, "password": password_enc, "email": user.email}
      conn.execute(users.insert().values(new_user))
      userD = conn.execute(users.select().where(users.c.username == user.username)).fetchone()
    except Exception as e:
      print(e)
      return {"message": str(e)}
    return userD