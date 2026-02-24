from pydantic import BaseModel, EmailStr
from datetime import datetime


class HabitBase(BaseModel):
    name: str
    user_id: int

class HabitCreate(HabitBase):
    description: str = None

class HabitResponse(HabitBase):
    id: int
    name: str
    description: str = None
    user_id: int
    current_streak: int
    longest_streak: int
    last_checkin_date: datetime = None

    class Config:
        orm_mode = True
