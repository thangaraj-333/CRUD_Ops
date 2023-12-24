from fastapi import APIRouter,HTTPException
from config.db import con
from models.index import users
from schemas.user import User
user = APIRouter()

@user.get("/")
async def read_data():
    return con.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id:int):
     con.execute(users.select().where(users.c.id==id))
     if not con:
            raise HTTPException(status_code=404,detail="Task not found")
     return con.execute(users.select().where(users.c.id==id)).fetchall()

@user.post("/")
async def write_data(user: User):
    con.execute(users.insert().values(
        id=user.id,
        title=user.title,
        description=user.description
    ))
    return con.execute(users.select()).fetchall()

@user.put("/{id}")
async def update_data(id: int,user: User):
    con.execute(users.update(
        id=user.id,
        title=user.title,
        description=user.description
    ).where(users.c.id==id))
    if not con:
         raise HTTPException(status_code=404,detail="Task not found")
    return con.execute(users.select()).fetchall()

@user.delete("/")
async def delete_data():
    con.execute(users.delete().where(users.c.id == id))
    if not con:
         raise HTTPException(status_code=404,detail="Task not found")
    return con.execute(users.select()).fetchall()