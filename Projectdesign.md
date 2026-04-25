Here’s a clean, GitHub-ready document you can drop straight into a `README.md` or `docs/backend_setup.md`.

---

# 🧠 NCD Risk Chatbot – Backend Setup Guide

## Overview

This document outlines how to build the backend for an NCD (Non-Communicable Disease) risk analysis chatbot using:

* FastAPI (Python web framework)
* SQLite (lightweight database)
* SQLAlchemy (ORM)

The backend is responsible for:

* Receiving user health data
* Calculating a risk score
* Storing results
* Returning structured responses

---

## 📁 Project Structure

```
app/
 ├── main.py        # API entry point
 ├── database.py    # Database connection
 ├── models.py      # Database tables
 ├── schemas.py     # Request/response models
 └── scoring.py     # Risk scoring logic
```

---

## ⚙️ Installation

Install required dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

---

## 🗄️ Database Setup (`database.py`)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./health.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Enable better concurrency
with engine.connect() as conn:
    conn.exec_driver_sql("PRAGMA journal_mode=WAL;")

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
```

---

## 🧾 Database Model (`models.py`)

```python
from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from database import Base

class HealthRecord(Base):
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True, index=True)

    age = Column(Integer)
    gender = Column(String)
    height = Column(Float)
    weight = Column(Float)

    sleep_hours = Column(Float)
    exercise_days = Column(Integer)

    score = Column(Integer)
    risk_level = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
```

---

## 📦 Schemas (`schemas.py`)

```python
from pydantic import BaseModel

class HealthInput(BaseModel):
    age: int
    gender: str
    height: float
    weight: float
    sleep_hours: float
    exercise_days: int

class HealthResponse(BaseModel):
    score: int
    risk_level: str
```

---

## 📊 Scoring Logic (`scoring.py`)

```python
def calculate_score(data):
    score = 0

    # Sleep scoring
    if data.sleep_hours < 6:
        score += 2
    elif data.sleep_hours < 7:
        score += 1

    # Exercise scoring
    if data.exercise_days < 2:
        score += 2
    elif data.exercise_days < 4:
        score += 1

    # BMI calculation
    bmi = data.weight / ((data.height / 100) ** 2)

    if bmi > 30:
        score += 3
    elif bmi > 25:
        score += 2

    # Risk classification
    if score >= 8:
        risk = "high"
    elif score >= 4:
        risk = "medium"
    else:
        risk = "low"

    return score, risk
```

---

## 🚀 Main API (`main.py`)

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import engine, SessionLocal
from scoring import calculate_score

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency: database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/analyze", response_model=schemas.HealthResponse)
def analyze(data: schemas.HealthInput, db: Session = Depends(get_db)):
    score, risk = calculate_score(data)

    record = models.HealthRecord(
        age=data.age,
        gender=data.gender,
        height=data.height,
        weight=data.weight,
        sleep_hours=data.sleep_hours,
        exercise_days=data.exercise_days,
        score=score,
        risk_level=risk
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "score": score,
        "risk_level": risk
    }
```

---

## ▶️ Running the Server

```bash
uvicorn main:app --reload
```

Access the API docs at:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Request

```json
{
  "age": 16,
  "gender": "male",
  "height": 170,
  "weight": 75,
  "sleep_hours": 5,
  "exercise_days": 1
}
```

---

## 📈 Scaling Considerations

This setup supports:

* ~100 to 1,000 users
* Light to moderate traffic

### Improvements already included:

* SQLite WAL mode (better concurrency)
* Clean data schema
* Lightweight scoring logic

---

## ⚠️ Important Notes

### 1. Health Data Safety

* Avoid storing personally identifiable information (name, email)
* Treat all data as sensitive

### 2. Medical Disclaimer

This system:

* Provides risk estimation only
* Does NOT replace professional medical advice

---

## 🔜 Next Steps

* Add more health inputs (diet, waist ratio, etc.)
* Implement input validation (realistic ranges)
* Add `/history` endpoint
* Introduce AI explanation layer (chatbot)

---

## ✅ Summary

You now have:

* A working backend API
* A structured database
* A scoring engine
* A scalable foundation for your chatbot

---

If you want, the next step can be turning this into a **chat-style API (multi-message conversation instead of one request)** or adding **AI-generated explanations safely on top of your scoring system**.
