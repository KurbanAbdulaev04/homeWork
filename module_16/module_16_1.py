from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root() -> str:
    return 'Главная страница'

@app.get('/user/admin')
async def user_admin() -> str:
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def id_user(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user')
async def user_params(username: str='User', age: int=18):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'