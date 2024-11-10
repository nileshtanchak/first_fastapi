from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from schema import Blog, User
from database import get_db
from repository import blog as blogRepo
from jwt_token import get_current_user

router = APIRouter()

@router.post("/blog", status_code=201)
def get_about(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blogRepo.create_blog(db, request)

@router.get("/blog")
def get_blog(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
   return blogRepo.get_all_blog(db)

@router.get("/blog/{id}", status_code= 200)
def get_blog(id: int, response: Response, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blogRepo.single_blog(db, response, id)

@router.put("/blog/{id}", status_code=201)
def update_blog(id: int, request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blogRepo.update_blog(db, request, id)

@router.delete("/blog/{id}", status_code=200)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blogRepo.delete_blog(db, id)
