from pydantic import BaseModel, Field
from typing import Literal
class UserHealthCreate(BaseModel):
    # Demographics and Metrics (Ensuring values are positive and realistic)
    age: int = Field(..., ge=1, le=120)
    weight: float = Field(..., ge=1.0)
    height: float = Field(..., ge=1.0)

    # Sleep Factors
    sleep_hours: float = Field(..., ge=0.0, le=24.0)
    sleep_consistency: int = Field(..., ge=1, le=3) # 1 to 3 scale
    late_night_scrolling: bool
    late_night_studying: bool
    caffeine_at_night: bool
    sugar_at_night: bool

    # Exercise Factors
    exercise_hours: float = Field(..., ge=0.0, le=24.0)
    mostly_sitting: bool

    # Diet Factors (Enforcing the 1 to 5 scale)
    fruits_vegetables_frequency: int = Field(..., ge=1, le=5)
    sugary_drinks_frequency: int = Field(..., ge=1, le=5)
    caffeinated_drinks_frequency: int = Field(..., ge=1, le=5)
    processed_food_frequency: int = Field(..., ge=1, le=5)
    energy_level: int = Field(..., ge=1, le=3) # 1 to 3 scale

    # Mental Health Factors (Enforcing limits)
    stress_level: int = Field(..., ge=1, le=3) # 1 to 3 scale
    overwhelmed_level: int = Field(..., ge=1, le=5)
    social_connection: int = Field(..., ge=1, le=5)

    # Substance Use Factors
    vape_cigarette: bool
    alcohol: bool
    cannabis: bool
    excessive_drug_usage: int = Field(..., ge=1, le=5)

    # Gender
    gender: Literal["male", "female"]


class UserHealthResponse(BaseModel):
    risk_score: float
    risk_level: str
    message: str
    bmi: float
    bmi_percentile: int

    # This allows Pydantic to read SQLAlchemy models directly
    class Config:
        from_attributes = True