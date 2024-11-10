# main.py

from fastapi import FastAPI
from model import blog as model
from database import engine
from api import blog, user

app = FastAPI()

model.base.metadata.create_all(engine)

app.include_router(blog.router, tags=['blogs'])
app.include_router(user.router, tags=['Auth'])