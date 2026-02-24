from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.checkin import CheckinCreate, CheckinResponse
from app.models.checkin import Checkin
from app.models.habits import Habit
from app.models.users import User
from app.configs.database import get_db
from app.schemas.habits import HabitResponse
from datetime import date, datetime, timedelta
from sqlalchemy import func

router = APIRouter()

@router.post("/", response_model=CheckinResponse)
def create_checkin(checkin: CheckinCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == checkin.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found! Cannot check in to a non-existent User.")

    habit = db.query(Habit).filter((Habit.id == checkin.habit_id), (Habit.user_id == checkin.user_id)).first()
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found for this user.")

    # Prevent duplicate check-ins for today
    today = date.today()

    existing_checkin = db.query(Checkin).filter((Checkin.habit_id == checkin.habit_id), (Checkin.user_id == checkin.user_id), (func.date(Checkin.checkin_date) == today)).first()
    if existing_checkin:
        raise HTTPException(status_code=400, detail="You have already checked in for this habit today.")

    new_checkin = Checkin(habit_id=checkin.habit_id, checkin_date=datetime.utcnow(), user_id=checkin.user_id)
    db.add(new_checkin)

    # Update habit streaks
    if habit.last_checkin_date and habit.last_checkin_date.date() == today - timedelta(days=1):
        habit.current_streak += 1
    else:
        habit.current_streak = 1

    habit.last_checkin_date = datetime.utcnow()

    if habit.current_streak > habit.longest_streak:
        habit.longest_streak = habit.current_streak

    db.commit()
    db.refresh(new_checkin)
    db.refresh(habit)
    return new_checkin 
