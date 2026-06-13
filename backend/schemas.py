from pydantic import BaseModel
#BaseModel acts like a filter and cleans things up (data)
class UserHealthCreate(BaseModel):
    age: int
    weight: float
    height: float
    sleep_hours: float
    exercise_hours: float
    #blood_pressure: float
    #blood_sugar_level: float
#Need more factors that isn't purely input-output numbers (later)
#Ex: Diet/Food, genetics, lifestyle
class UserHealthResponse(BaseModel):
    risk_score: float
    risk_level: str
    message: str