from database import base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Blog(base):
    __tablename__ = "Blog"

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    body = Column(String)
    # user_id = Column(Integer, ForeignKey("users.id"))

    # creator = relationship("User", back_populates="blogs")

class User(base):
    __tablename__ = "users"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    # blogs = relationship("Blog", back_populates="creator")