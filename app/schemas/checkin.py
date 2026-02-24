from pydantic import BaseModel, EmailStr
from datetime import datetime

class CheckinBase(BaseModel):
    habit_id: int
    user_id: int

class CheckinCreate(CheckinBase):
    pass

class CheckinResponse(CheckinBase):
    # id: int
    # habit_id: int
    # user_id: int
    checkin_date: datetime

    class Config:
        from_attributes = True
