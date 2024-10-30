from fastapi import FastAPI, Path
from typing import Annotated

new_app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@new_app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}
# http://127.0.0.1:8000/


@new_app.get("/user/admin")
async def admin_panel() -> dict:
    return {"message": "Вы вошли как администратор"}
# http://127.0.0.1:8000/user/admin


@new_app.get("/user/{user_id}")
async def get_user_number(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=1)) -> dict:
    if str(user_id) in users:
        return {"message": f"Вы вошли как пользователь № {user_id}"}
    else:
        return {"message": f"Пользователя № {user_id} не существует"}
# http://127.0.0.1:8000/user/1


@new_app.get("/user/{username}/{age}")
async def get_user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: int = Path(ge=18, le=120, description='Enter age', example=24)
) -> dict:
    return {"User": username, "Age": age}
# http://127.0.0.1:8000/user/Ivanko/19


@new_app.get("/users")
async def get_users() -> dict:
    return users


@new_app.post('/user/{username}/{age}')
async def post_user(username: str, age: str) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@new_app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: str) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"


@new_app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    user_id = str(user_id)
    del users[user_id]
    return f"User {user_id} has been deleted"
