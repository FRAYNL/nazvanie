from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    phone: int
    place: int



@app.post("/")
async def add_user(use: User):
    return user

