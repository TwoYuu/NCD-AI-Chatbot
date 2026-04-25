from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas, scoring
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
#Opens and closes database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/analyze", response_model=schemas.UserHealthResponse)
#analyze response from user
def analyze(data: schemas.UserHealthCreate, db: Session = Depends(get_db)):
    # Save to database
    db_data = models.UserHealth(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)

    # Calculate score
    risk_score = scoring.calculate_score(data)

    print("Risk Score:", risk_score)

    return db_data