from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models, configs

router = APIRouter()

@router.get("/users")
def user_check():
    return {"message": "User endpoint is working!"}

# @router.post("/", response_model=schemas.users.UserResponse)
# def create_user(user: schemas.users.UserCreate, db: Session = Depends(configs.get_db)):
#     db_user = db.query(models.User).filter((models.User.username == user.username) | (models.User.email == user.email)).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username or email already registered")
    
#     hashed_password = user.password + "notreallyhashed"  # Placeholder for hashing
#     new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

