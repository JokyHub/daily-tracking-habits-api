from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.habits import HabitCreate, HabitResponse
from app.models.habits import Habit
from app.models.users import User
from app.configs.database import get_db
from app.schemas.users import UserResponse


router = APIRouter()

@router.post("/", response_model=HabitResponse)
def create_habit(habit: HabitCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == habit.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found! Cannot create habit for non-existent user.")

    db_habit = db.query(Habit).filter((Habit.name == habit.name) & (Habit.user_id == habit.user_id)).first()
    if db_habit:
        raise HTTPException(status_code=400, detail="Habit already exists for this user!")
    
    new_habit = Habit(name=habit.name, user_id=habit.user_id)
    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)
    return new_habit

@router.get("/{user_id}", response_model=list[HabitResponse])
def read_habits_by_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found! Cannot retrieve habits for non-existent user.")
    habits = db.query(Habit).filter(Habit.user_id == user_id).all()
    return habits