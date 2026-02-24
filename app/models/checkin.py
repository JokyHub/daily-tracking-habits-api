from sqlalchemy import Column, Integer, String, DateTime
from app.configs.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Checkin(Base):
    __tablename__ = "checkins"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

    habit = relationship("Habit")


