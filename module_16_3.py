from fastapi import FastAPI, Path
from typing import Dict, Annotated

app = FastAPI()

users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]
):
    user_id = str(max(map(int, users.keys())) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[str, Path(regex="^[1-9][0-9]*$", description="Enter User ID", example="1")],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanProfi")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=28)]
):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[str, Path(regex="^[1-9][0-9]*$", description="Enter User ID", example="1")]
):
    del users[user_id]
    return f"User {user_id} has been deleted"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path(description="Enter User ID", example="1")]):
    del users[user_id]
    return f"User {user_id} has been deleted"
