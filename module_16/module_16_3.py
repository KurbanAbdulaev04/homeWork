from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def return_users_dict() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def insert_user(username: Annotated[str, Path(min_length=3, max_length=100,
                                                    description='Enter your name', example='User')],
                      age: int = Path(ge=18, le=120, description='Enter your age', example='20')) -> str:
    id_up = str(int(max(users, key=int)) + 1)
    users[id_up] = f'Имя: {username}, возраст: {age}'
    return f'User {id_up} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: Annotated[str, Path(min_length=3, max_length=100,
                                                    description='Enter your name', example='User')],
                      age: int = Path(ge=18, le=120, description='Enter your age', example='20')) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'Message with {user_id} was delete'
