from fastapi import FastAPI


new_app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


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
async def delete_user(user_id: int) -> dict:
    del users[user_id]
    return users
