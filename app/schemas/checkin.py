from pydantic import BaseModel, EmailStr
from datetime import datetime

class CheckinBase(BaseModel):
    habit_id: int
    date: datetime
class CheckinCreate(CheckinBase):
    pass

class CheckinResponse(CheckinBase):
    id: int
    habit_id: int
    date: datetime

    class Config:
        orm_mode = True
