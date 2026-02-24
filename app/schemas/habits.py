from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class HabitBase(BaseModel):
    name: str
    user_id: int

class HabitCreate(HabitBase):
    description: str = None

class HabitResponse(HabitBase):
    id: int
    name: str
    description: Optional[str] = None
    user_id: int
    current_streak: int
    longest_streak: int
    last_checkin_date: Optional[datetime] = None

    class Config:
        from_attributes = True
