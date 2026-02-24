from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.configs.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Checkin(Base):
    __tablename__ = "checkins"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    date = Column(DateTime, nullable=False)

    habit = relationship("Habit")


