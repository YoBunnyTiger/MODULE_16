from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict


app = FastAPI()

users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


class User(BaseModel):
    username: str
    age: int


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    del users[user_id]
    return f"User {user_id} has been deleted"
