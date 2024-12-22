from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()


@app.get('/users')
async def return_users_dict() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def insert_user(user: User, username: str, age: int) -> User:
    user.username = username
    user.age = age
    user.id = max((i.id for i in users), default=0) + 1
    users.append(user)

    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str,age: int) -> User:
    try:
        put_user = None
        for i in users:
            if i.id == user_id:
                put_user = i
        put_user.username = username
        put_user.age = age
        return put_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    try:
        for i in users:
            if i.id == user_id:
                ind = users.index(i)
                users.pop(ind)
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
