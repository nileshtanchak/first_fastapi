from pydantic import BaseModel
from typing import List


class User(BaseModel):
    name: str
    email: str
    password: str

class Blog(BaseModel):
    title: str
    body: str
    # creator: User
    class Config():
        from_attributes = True

class ShowUser(BaseModel):
    name: str
    email: str
    # blogs: List[Blog] = []

    class Config():
        from_attributes = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None