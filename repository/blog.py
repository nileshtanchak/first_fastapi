from sqlalchemy.orm import Session
from model import blog
from schema import Blog
from fastapi import Response, status


def get_all_blog(db: Session):
    blog_data = db.query(blog.Blog).all()
    return {"message": "Data retrive successfully", "data":blog_data}

def create_blog(db: Session, request: Blog):
    new_blog = blog.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def single_blog(db: Session, response: Response, id:int):
    blog_data = db.query(blog.Blog).filter(blog.Blog.id == id).first()
    if not blog_data:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Data not found", "data":blog_data}
    else :
        return {"message": "Data retrive successfully", "data":blog_data}
    
def delete_blog(db: Session, id:int):
    blog_data = db.query(blog.Blog).filter(blog.Blog.id == id).delete(synchronize_session=False)
    
    db.commit()
    # db.refresh(blog_data)
    return "Deleted Successfully"

def update_blog(db: Session, request: Blog, id:int):
    blog_data = db.query(blog.Blog).filter(blog.Blog.id == id).update({"title": request.title}, synchronize_session=False)
    
    db.commit()
    # db.refresh(blog_data)
    return "Updated Successfully"