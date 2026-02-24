from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.configs.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Checkin(Base):
    __tablename__ = "checkins"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    checkin_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    habit = relationship("Habit", back_populates="checkins")
    user = relationship("User", back_populates="checkins")


