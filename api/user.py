from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schema import User, ShowUser
from model import blog
from database import get_db
from repository import user as userRepo
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/sign_up")
def create_user(request: User, db: Session = Depends(get_db)):
    return userRepo.sign_up(db, request)

@router.get("/user/{id}", response_model=ShowUser)
def get_single_user(id:int, db: Session = Depends(get_db)):
    return userRepo.get_single_user(db, id)
    # return {"message": "User retrieve succesfully", "user": user},

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    

    return userRepo.user_login(db, request)
    # return {"message": "User retrieve succesfully", "user": user},