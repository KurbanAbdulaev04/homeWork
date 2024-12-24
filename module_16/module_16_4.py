from fastapi import FastAPI, HTTPException, Path
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
async def insert_user(username: str = Path(min_length=5, max_length=20, example='UrbanUser', description='Enter username'),
                      age: int = Path(ge=18, le=120, description='Enter your age', example='24')) -> User:
    user_id = max((i.id for i in users), default=0) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)

    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='1'),
                      username: str = Path(min_length=5, max_length=20, example='UrbanUser', description='Enter username'),
                      age: int = Path(ge=18, le=120, description='Enter your age', example='24')) -> User:
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
async def delete_user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='1')) -> User:
    try:
        for i in users:
            if i.id == user_id:
                ind = users.index(i)
                return users.pop(ind)

    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
