from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.users import UserCreate, UserResponse
from app.models.users import User
from app.configs.database import get_db


router = APIRouter()

# @router.get("/users")
# def user_check():
#     return {"message": "User endpoint is working!"}

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    db_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username or email already registered! Please choose another one.")
    
    hashed_password = user.password + "notreallyhashed"  # Placeholder for hashing
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user