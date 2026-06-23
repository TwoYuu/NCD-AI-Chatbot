from sqlalchemy import Column, Integer, Float, String, Boolean
from database import Base

class UserHealth(Base):
    #_tablename_ defines name of the database table?
    __tablename__ = "user_health"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    sleep_hours = Column(Float)
    sleep_consistency = Column(Integer)

    #Night Habit Factors
    late_night_scrolling = Column(Boolean)
    late_night_studying = Column(Boolean)
    caffeine_at_night = Column(Boolean)
    sugar_at_night = Column(Boolean)
    #Exercise/Physical
    exercise_hours = Column(Float)
    mostly_sitting = Column(Boolean)
    #Diet
    fruits_vegetables_frequency = Column(Integer)
    sugary_drinks_frequency = Column(Integer)
    caffeinated_drinks_frequency = Column(Integer)
    processed_food_frequency = Column(Integer)
    energy_level = Column(Integer)
    #Mental Health
    stress_level = Column(Integer)
    overwhelmed_level = Column(Integer)
    social_connection = Column(Integer)
    #Substance Use
    vape_cigarette = Column(Boolean)
    alcohol = Column(Boolean)
    cannabis = Column(Boolean)
    excessive_drug_usage = Column(Integer)
    #Family Genetics
    risk_score = Column(Float)
    risk_level = Column(String)