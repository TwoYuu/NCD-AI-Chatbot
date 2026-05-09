from sqlalchemy import Column, Integer, Float, String
from database import Base

class UserHealth(Base):
    __tablename__ = "user_health"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    sleep_hours = Column(Float)
    exercise_hours = Column(Float)

    risk_score = Column(Float)
    risk_level = Column(String)