from pydantic import BaseModel

class UserHealthCreate(BaseModel):
    age: int
    weight: float
    height: float
    sleep_hours: float
    exercise_hours: float

class UserHealthResponse(UserHealthCreate):
    id: int

    class Config:
        from_attributes = True
class UserHealthResponse(BaseModel):
    risk_score = float
    risk_level = str
    message = str