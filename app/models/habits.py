from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.configs.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, nullable=False)
    description = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to users.id

    current_streak = Column(Integer, default=0, nullable=False)
    longest_streak = Column(Integer, default=0, nullable=False)
    last_checkin_date = Column(DateTime, nullable=True)

    user = relationship("User")
    checkins = relationship("Checkin", back_populates="habit", cascade="all, delete")


