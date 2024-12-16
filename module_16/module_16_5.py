from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import HTMLResponse


users = []


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()

templates = Jinja2Templates(directory='templates')


@app.get('/user/{user_id}')
async def return_users_dict(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id]})


@app.post('/user/{username}/{age}')
async def insert_user(user: User, username: str, age: int) -> User:
    user.username = username
    user.age = age
    if users is None:
        user.id = 1
    else:
        user.id = len(users) + 1
    users.append(user)

    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str,age: int) -> User:
    try:
        put_user = users[user_id]
        put_user.username = username
        put_user.age = age
        return put_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.get('/')
async def all_message(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})
