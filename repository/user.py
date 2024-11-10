from sqlalchemy.orm import Session
from model import blog
from schema import User
from fastapi import Response, status, HTTPException
from hashing import Hash
from jwt_token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

def get_single_user(db: Session, id:int):
    user = db.query(blog.User).filter(blog.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not exists")
    
    return user

def sign_up(db:Session, request: User):
    all_user = db.query(blog.User).all()
    print("All Users:", all_user)

    # Check if the email already exists
    if all_user:
        for user in all_user:
            print("Entered the for loop")
            if user.email == request.email:
                raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED, detail=f"User {request.email} already exists")
    
    # Create a new user if the email does not exist
    new_user = blog.User(
        email=request.email,
        password=Hash.bcrypt_password(request.password),  # Assuming you're storing the password like this
        name=request.name  # Adjust fields according to your `User` model
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User created successfully", "User": new_user}

def user_login(db:Session, request: OAuth2PasswordRequestForm):
    user = db.query(blog.User).filter(blog.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with {request.email} email not found")
    
    if not Hash.verify_password(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user Password is incorrect")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"token": access_token, "user": {"id": user.id, "name": user.name, "email": user.email}}
